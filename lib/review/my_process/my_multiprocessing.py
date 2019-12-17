#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing
from multiprocessing.dummy import Pool


pool1 = multiprocessing.Pool()
pool2 = Pool()

pool1.map()
pool2.map()
