# -*- coding: utf-8 -*-

class addPerson(object):
	def __init__(self,nm,ph):
		self.name = nm
		self.phone = ph
		print 'Created instance for', self.name
	def updatePhone(self,newph):
		self.phone = newph
		print 'Updated phone for ',self.phone
	
class addInfo(addPerson):
	def __init__(self,nm,ph,id,em):
		addPerson.__init__(self,nm,ph)
		self.empid = id
		self.email = em
		
	def updateEmail(self,newem):
		self.email = newem
		print 'Updated e-mail address for:', self.email
		
zs = addInfo('ZhangSan', '123445', '01','Zs@gmail')
print zs
print 'Instance property: [%s], [%s], [%s], [%s]' % (zs.name, zs.phone, zs.empid, zs.email)
zs.updatePhone('250')
zs.updateEmail('hell@gmail')