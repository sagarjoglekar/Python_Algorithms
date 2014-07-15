class dummyclass:

	data = "Valar Morgulis"
	

	def  __init__(self, append):

		self.data = self.data + append
		self.fib = {}

	def stringtoken(self): 
		return self.data

	def fibonacci(self, n):
		if n <= 2:
			return 1
		else:
			return (self.fibonacci(n-1) + self.fibonacci(n-2) )

	def DPfibonacci(self,n):
		if n in self.fib: return self.fib[n]
		if n <= 2:
			f = 1
		else:
			f = (self.DPfibonacci(n-1) + self.DPfibonacci(n-2) )
			
		self.fib[n] = f;
		return f 

	def bottomupDPfibonacci(self,n):
		for k in range(1,n+1):

			if n <= 2:
				f = 1
			else:
				f = ( self.fib[n-1] + self.fib[n-2] )
			
			self.fib[n] = f;
		return self.fib[n] 








