#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading


# print threading.currentThread()
# print threading.enumerate()
count = 0
lock = threading.Lock()


def adder():
    global count
    with lock:
        count += 1
    time.sleep(.5)
    with lock:
        count += 1


ths = list()
for i in range(500):
    th = threading.Thread(target=adder)
    th.start()
    ths.append(th)

for th in ths:
    th.join()

print count
import thread
thread.exit()