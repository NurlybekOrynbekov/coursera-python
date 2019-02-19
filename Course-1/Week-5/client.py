import socket
import time

class Client:
    
    def __init__(self, host, port, timeout=None):
        self.socket = socket.create_connection((host, port), timeout=timeout)

    def put(self, key, value, timestamp=None):
        self.socket.sendall('put {} {} {}\n'.format(key, value, timestamp or int(str(time.time()))).encode('utf8'))
        data = self.socket.recv(1024).decode('utf8')
        if data == 'error\nwrong command\n\n':
            raise ClientError
    
    def get(self, key):
        self.socket.sendall('get {}\n'.format(key).encode('utf8'))
        data = self.socket.recv(1024).decode('utf8')

        if data == 'error\nwrong command\n\n':
            raise ClientError

        if data == 'ok\n\n': 
            return {}

        data = data.replace('\n', ' ').split()[1:]
        data = [(data[x], float(data[x+1]), int(data[x+2])) for x in range(0, len(data), 3)]
        result = {}
        for d in data:
            if d[0] not in result:
                result[d[0]] = [(d[2], d[1])]
            else :
                result[d[0]].append((d[2], d[1]))
        return result


class ClientError(Exception):
    pass