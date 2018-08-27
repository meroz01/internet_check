import socket, time

class Checker:
    def __init__(self, single_line):
        self.host = 'google.com'
        self.tts = 1
        self.single_line = single_line
        print('Listening to internet connection...\n')

    def check_connection(self):
        while True:
            try:
                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                res = s.connect_ex((self.host, 80))
                ip = socket.gethostbyname(self.host)

                if res == 0:
                    self.print_result(ip, '>')
                    time.sleep(self.tts)
                else:
                    self.print_result(ip, 'x')
                    time.sleep(self.tts)
            except:
                self.print_result(ip, 'X')
                time.sleep(self.tts)


    def print_result(self, ip, success):
        localtime = time.asctime(time.localtime(time.time()))
        if self.single_line:
            print(success, end='', flush=True)
        else:
            print(f'{success} {ip} | {localtime} | {self.host}')


if __name__ == '__main__':
    c = Checker(True)
    c.check_connection()
