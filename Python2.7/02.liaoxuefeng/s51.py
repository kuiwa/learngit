#!/usr/bin/env python
# -*- coding: utf-8 -*-

#�����ļ���Ŀ¼
import os
print os.name
#ϵͳ����
print os.environ
#��������
print os.getenv('PATH')
#���PATH����
print os.path.abspath('.')
#�鿴��ǰĿ¼�ľ���·��
new_dir = os.path.join(os.path.abspath('.'), 'testdir')
#�ڵ�ǰ·��������һ��Ŀ¼
print new_dir
os.mkdir('new_dir')
#����Ŀ¼
os.rmdir('new_dir')
#ɾ��Ŀ¼
split_dir = os.path.split(new_dir)
print split_dir
#��ӡ���Ľ������ÿ��\ǰ�������һ��ת���ַ�\
print os.path.splitext('path/to/file.txt')

import shutil
shutil.copyfile('readme.txt', 'test.txt')
os.rename('test.txt','test.py')
os.remove('test.py')

x = 1
for x in os.listdir('.'):
	if os.path.isfile(x) and os.path.splitext(x)[1]=='.py':
		print x