#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


print 'Got this: "%s"' % raw_input()
data = sys.stdin.readline()[:-1]
print 'The meaning of life is:', data, int(data) * 2
