from math import *

class unc_num:

	def __init__(self, num, unc):
		self.num = num
		self.unc = unc
		self.make_consistent()

	def make_consistent(self):
		self.define_pos()
		self.unc = round(self.unc, -self.pos)
		self.num = round(self.num, -self.pos)

	def define_pos(self):
		if log10(self.unc) > 0:
			self.pos = floor(log10(self.unc))
		else:
			self.pos = floor(log10(self.unc))

	def print_self(self):
		print(str(self.num) + " " + str(self.unc))

if __name__ == "__main__":
	a = unc_num(5.12123, 0.03333)
	a.print_self()