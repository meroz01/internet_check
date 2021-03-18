import socket
from time import sleep, asctime, localtime , time
from datetime import datetime
from random import choice

from settings import Settings


class Checker:
    current_host = ''
    tts = 1
    datetime_last_internet = ''

    def __init__(self, single_line):
        self.hosts = Settings.hosts
        self.single_line = single_line
        print('Listening to internet connection...\n')

    def check_connection(self):
        while True:
            timestamp = datetime.today().strftime('\n[%d/%m/%Y %H:%M:%S]')

            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(10)

                self.current_host = choice(self.hosts)
                res = s.connect_ex((self.current_host, 80))
                ip = socket.gethostbyname(self.current_host)

                self.datetime_last_internet = ''

                if res == 0:
                    self.print_result(ip, '.')
                    sleep(self.tts)
                else:
                    print(f'{timestamp}')
                    sleep(self.tts)
            except:
                if not self.datetime_last_internet:
                    print(f'{timestamp}')
                    self.datetime_last_internet = timestamp

                print('X', end='', flush=True)
                sleep(self.tts)

    def print_result(self, ip, success):
        local_time = asctime(localtime(time()))
        if self.single_line:
            print(success, end='', flush=True)
        else:
            print(f'{success} {ip} | {local_time} | {self.current_host}')
