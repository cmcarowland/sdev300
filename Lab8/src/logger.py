"""adsklfj"""
import os
from datetime import datetime
from enum import Enum

class LogTypes(Enum):
    INFO = 0
    WARN = 1
    LOW = 2
    MED = 3
    HIGH = 4

class LogItem:
    def __init__(self, level : LogTypes, des : str, dt : datetime, ip : str):
        self.level = level
        self.description = des
        self.date = dt.date()
        self.time = dt.time().strftime("%H:%M:%S")
        self.ip = ip

    def __str__(self) -> str:
        return f'[{self.level.name}] {self.description} : {self.date}, {self.time}, {self.ip}'

class Log:
    def __init__(self):
        self.log = []

    def add_log(self, log_item : LogItem):
        self.log.append(log_item)
        self.save_log()

    def save_log(self):
        old_log = ''
        if os.path.exists('log.txt'):
            with open('log.txt', 'r', encoding='utf=8') as ifile:
                old_log = ifile.read()

        self.log.reverse()
        for l in self.log:
            old_log = str(l) + '\n' + old_log

        self.log = []
        with open('log.txt', 'w', encoding='utf-8') as ofile:
            ofile.write(old_log)
