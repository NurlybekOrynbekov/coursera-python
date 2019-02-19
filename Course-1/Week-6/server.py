import asyncio


class WrongCommand(Exception):
    pass


class ClientServerProtocol(asyncio.Protocol):

    info = {}

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        try:
            resp = self.decode_command(data.decode())
        except WrongCommand:
            resp = 'error\nwrong command\n\n'
        finally:
            self.transport.write(resp.encode())

    def decode_command(self, data):
        if 'put' in data:
            command, key, val, time = data.split()
            result = self.put(key, val, time)
            return result
        elif 'get' in data:
            command, key = data.split()
            return self.get(key)
        else:
            raise WrongCommand

    def get(self, key):
        responce = 'ok\n'
        if key == '*':
            for x in self.info:
                for val in self.info[x]:
                    responce += f'{x} {val}\n'
        elif key in self.info:
            for val in self.info[key]:
                responce += f'{key} {val}\n'
        responce += '\n'
        return responce

    def put(self, key, val, time):
        if key not in self.info:
            self.info[key] = [f'{val} {time}']
        else:
            self.info[key].append(f'{val} {time}')
        print(self.info)
        return 'ok\n\n'


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
