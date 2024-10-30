class matrix:
	def __init__(self, N, M): # N=rows, M=cols
		if(N < 1 or M<1):
			raise AssertionError("N or M must be greater than 0")
		self.storage = [[0 for i in range(M)] for j in range(N)]
		self.N=N
		self.M=M
		# print(self.storage)

	# acces by index
	def get(self, row_idx, col_idx):
		if(row_idx<0 or row_idx>=self.N or col_idx<0 or col_idx>=self.M):
			return None
		return self.storage[row_idx][col_idx]
	
	# acces by index
	def set(self, row_idx, col_idx, value):
		if(row_idx<0 or row_idx>=self.N or col_idx<0 or col_idx>=self.M):
			raise AssertionError("illegal value for row_idx or col_idx")
		self.storage[row_idx][col_idx]=value
	
	def transpose(self):
		temp = self.storage
		self.storage = [[0 for i in range(self.N)] for j in range(self.M)]
		for i in range(self.N):
			for j in range(self.M):
				self.storage[j][i] = temp[i][j]
		self.N, self.M = self.M, self.N
		

	def multiply(self, to_multiply):

		if isinstance(to_multiply, matrix):
			to_multiply = to_multiply.storage
		
		to_multiply_rows = len(to_multiply)
		to_multiply_cols = len(to_multiply[0])

		if self.M != to_multiply_rows:
			raise AssertionError("Sizes don't match!")
	
		c = [[0 for i in range(to_multiply_cols)] for j in range(self.N)]
		for i in range(self.N):
			ci = c[i] # row, indexed by column
			for k in range(self.M):
				bk = to_multiply[k] # row, indexed by column
				aik = self.storage[i][k]
				for j in range(to_multiply_cols):
					ci[j] += aik * bk[j]
    
		self.storage = c

	def apply_to_all(self, apply):
		for i in range(0,self.N):
			for j in range(0, self.M):
				self.storage[i][j] = apply(self.storage[i][j])


m = matrix(2,3)
print(m.storage)
m.transpose()
print(m.storage)
m.apply_to_all(lambda x: x+1)
print(m.storage)
m.set(0,0,2)
m.set(1,1,2)
m.set(2,1,0)
print(m.storage)

m.multiply([[1,2,3],[2,3,4]])
print(m.storage)