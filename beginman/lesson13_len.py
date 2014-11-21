# -*- coding: utf-8 -*-

import os
f = open('lesson13.txt', 'r')
# 统计单词的个数，以空格为分隔
print len([word for line in f for word in line.split()])
# 统计文件大小
print os.stat('lesson13.txt').st_size
# 返回文件头部，如果无此条，下面字符统计无法进行，始终显示为0，因为迭代器已访问完了文件的所有行
f.seek(0)
# 统计字符数量
print sum([len(word) for line in f for word in line.split()])
f.close()