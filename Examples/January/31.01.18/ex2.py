# Override => перегрузка
# Overwrite => перезапись

class Car(object):
	def __init__(self, year, color):
		self.year = year
		self.color = color
		self.wheels = 4
		self.distanse = 0

	def ride(self):
		self.distanse += 500

class Lambo(Car):
	def __init__(self, year, color, volume):
		self.volume = volume
		self.name = 'Lambo'
		super(Lambo, self).__init__(year,color)

	def ride(self, n=None):
		if n is None:
			super(Lambo, self).ride()
		else:
			self.distanse += n

	def fly(self):
		return True


if __name__ == '__main__':
	c = Car(2001,'red')
	print(c.year, c.color, c.wheels)

	l = Lambo(2017, 'white', 6.3)
	print(l.name,l.year, l.color, l.wheels, l.distanse, l.fly())

	l.ride(100)
	# l.ride()

	print(l.name,l.year, l.color, l.wheels, l.distanse,l.volume)