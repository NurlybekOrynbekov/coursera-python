import asyncio


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.dict = dict()

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, data):
        if 'put' in data:
            command, key, val, time = data.split()
            if key not in self.dict:
                self.dict[key] = []
            self.dict[key].append(f'{val} {time}')
            return 'ok\n\n'
        elif 'get' in data:
            responce = 'ok\n'
            command, key = data.split()
            if key == '*':
                for x in self.dict:
                    for val in self.dict[x]:
                        responce += f'{x} {val}\n'
            elif key in self.dict:
                for val in self.dict[key]:
                    responce += f'{key} {val}\n'
            else:
                responce += '\n'
            print(data + ' => ' + responce)
            return responce
        else:
            return 'error\nwrong command\n\n'


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
