#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess


pip = subprocess.Popen('reader.py', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
pip.stdin.write('lumber jack\n')

print pip.stdout.readline()[:-1]
pip.stdin.write('12\n')
pip.stdin.close()
print pip.communicate()[0][:-1]