from datetime import datetime
import socket, time
from random import choice


class Checker:
    host = ''

    def __init__(self, single_line):
        self.hosts = ['google.com',
                      'wp.pl',
                      'allegro.pl',
                      'amazon.com',
                      'facebook.com',
                      'ipecho.net',
                      '8.8.8.8']
        self.tts = 1
        self.single_line = single_line
        self.datetime_last_internet = ''
        print('Listening to internet connection...\n')

    def check_connection(self):
        while True:
            d = datetime.today().strftime('\n[%d/%m/%Y %H:%M:%S]')
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                self.host = choice(self.hosts)
                res = s.connect_ex((self.host, 80))
                ip = socket.gethostbyname(self.host)

                self.datetime_last_internet = ''

                if res == 0:
                    self.print_result(ip, '.')
                    time.sleep(self.tts)
                else:
                    print(f'{d}')
                    # self.print_result(ip, 'x')
                    time.sleep(self.tts)
            except:
                if not self.datetime_last_internet:
                    print(f'{d}')
                    self.datetime_last_internet = d

                print('X', end='', flush=True)
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
