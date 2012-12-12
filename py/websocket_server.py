#coding: utf-8

import SocketServer

class WebSocketHandler(SocketServer.BaseRequestServer):
    def handle(self):
        self.CLIENT_TERMINATED =False;
        data = self.request.recv(1024);
        self.handshake(data);

        while True:
            data = self.request.recv(1024);
            self.received_data(data);

    def received_data(self, data):
        
