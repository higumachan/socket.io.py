#coding: utf-8

import SocketServer

class WebSocketHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.CLIENT_TERMINATED =False;
        print "Open"
        self.handshake();

        while True:
            data = self.request.recv(1024);
            self.received_data(data);

    def received_data(self, data):
        data = self.decode(data);
        function, args = data.split(":");
        self.__getattr__(function, *args);
               
    def handshake(self):
        handshake_data = self.request.recv(1024);
        handshake_dict = self.shake2dict(handshake_data);
        seckey = handshake_dict["Sec-WebSocket-Key"];
        seckey += ""
        ackey = self._get_ackey(seckey);

        response = self.get_hand_hake_response(ackey);
        
        self.request.send(response);

    def _get_ackey(self, seckey);
        return (hashlib.sha1(seckey).digest().encode("base64"));

    def get_hand_hake_response(self, ackey):
        result = 'HTTP/1.1 101 Switching Protocols\r\n';
        result += 'Upgrade: websocket\r\n';
        result += 'Connection: Upgrade\r\n';
        result += 'Sec-WebSocket-Accept: %s\r\n\r\n' % (ackey,);
        return result;

    def send(self, data):
        if (self._is_handshaked == True):
            data = data.encode("utf8");
            header = "\x81";
            header += chr(len(data));
            self._connect.send(header + data);

    def decode(self, data):
        header = data[:2];
        mask = data[2:6]
        body = data[6:];
        return "".join([chr(ord(body[i]) ^ ord(mask[i % 4])) for i in range(len(body))]);

if __name__ == "__main__":
    HOST, PORT = "localhost", 7135;
    server = SocketServer.TCPServer((HOST, PORT), WebSocketHandler);
    server.serve_forever();

