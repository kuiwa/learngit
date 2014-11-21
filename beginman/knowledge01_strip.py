# -*- coding: utf-8 -*-

theString = '	saaaay yes no yaaaaas'
print theString.strip()
print theString.strip().strip('say')
print theString.strip().strip('say')
print theString.strip().strip('say ')
print theString.strip().lstrip('say')
print theString.strip().rstrip('say')