# -*- coding: utf-8 -*-

class addPerson(object):
	def __init__(self,nm,ph):
		self.name = nm
		self.phone = ph
		print 'Created instance for', self.name
	def updatePhone(self,newph):
		self.phone = newph
		print 'Updated phone for ',self.phone
		
josn = addPerson('JSON','156208444')
ben = addPerson('Ben', '1523892442')
print 'Instance property:[%s][%s]' % (ben.name, ben.phone)
ben.updatePhone('110')
print ben.phone