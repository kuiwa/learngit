# -*- coding: utf-8 -*-

books = [
		{"name": u"C#从入门到精通", "price": 23.7, "store": u"卓越"},
		{"name": u"ASP.NET高级编程", "price": 44.5, "store": u"卓越"},
		{"name": u"Python核心编程", "price": 24.7, "store": u"当当"},
		{"name": u"JavaScript大全", "price": 45.7, "store": u"当当"},
		{"name": u"Django简明教程", "price": 26.7, "store": u"新华书店"},
		{"name": u"深入Python", "price": 55.7, "store": u"新华书店"},
		]
# 查找最低价格，原始方法		
price = []
for item in books:
	for p in item:
		if p == "price":
			price.append(item[p])
			
print min(price)

# 列表解析
print min(itemA[p2] for itemA in books for p2 in itemA if p2 == 'price')

# Python相关书籍检索
for itemB in books:
	for p in itemB:
		if itemB['name'].find('Python')>=0:
			print itemB[p]

print [itemC[p] for itemC in books for p in itemC if itemC['name'].find('Python')>=0]