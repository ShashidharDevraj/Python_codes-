class A(object):
	def go(self):
		print("go A go")
	def stop(self):
		print("stop A stop")
	def pause(self):
		# raise Exception("Not Implemented")
		print ("Pause A pause")


class B(A):
	def go(self):
		super(B, self).go()
		print("go B go")


class C(A):
	def go(self):
		super(C, self).go()
		print("go C go")

	def stop(self):
		super(C, self).stop()
		print("stop C stop")
		

class D(B,C):
	def go(self):
		super(D,self).go()
		print ("go D go")

	def stop(self):
		super(D, self).stop()
		print ("Stop D stop")

	def pause(self):
		super(D,self).pause()
		print ("Pause D pause")


class E(B,C):
	pass

a = A()
b = B()
c = C()
d = D()
e = E()



# a.go()
# b.go()
# c.go()
# c.stop()
# d.go()
# d.stop()
# e.go()
e.pause()
