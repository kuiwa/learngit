#!/usr/bin/env python
# -*- coding: utf-8 -*-

#����
#logging
#level=debug/info/warning/error
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n