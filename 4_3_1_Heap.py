from random import randint

class Heap():


	def __init__(self):
		self.body = ['root', ]


	def insert(self, num: int):
		self.body.append(num)
		child_index = len(self.body) - 1
		if not self.child_is_min(child_index):
			self.shift_up(child_index)


	def extract_max(self):
		parent_index = 1
		response = self.body[parent_index]

		self.body[parent_index] = self.body[-1]
		del self.body[-1]

		child_1_index = parent_index * 2
		# if child_1_index > len(self.body) - 1:
		# 	child_1 = None 
		child_2_index = parent_index * 2 + 1
		# if child_2_index > len(self.body) - 1:
		# 	child_2 = None

		if self.body[parent_index] < self.body[child_1_index] or self.body[parent_index] < self.body[child_2_index]:
			parent = self.body[parent_index]
			if self.body[child_1_index] > self.body[child_2_index]:
				self.body[parent_index] = self.body[child_1_index]
				self.body[child_1_index] = parent
			else:
				self.body[parent_index] = self.body[child_2_index]
				self.body[child_2_index] = parent

		print(response)

	def child_is_min(self, index):
		child = index
		parent = int(child / 2)
		if parent < 1:
			parent = 1
		if self.body[child] <= self.body[parent]:
			return True
		else:
			return False

	def shift_up(self, index):
		while not self.child_is_min(index):
			child_index = index
			parent_index = int(child_index / 2)
			if parent_index < 1:
				parent_index = 1
			parent = self.body[parent_index]
			self.body[parent_index] = self.body[child_index]
			self.body[child_index] = parent
			index = parent_index



a = Heap()
print('done')
for i in range(32):
	a.insert(randint(1, 50))
print(a.body)
a.extract_max()
print(a.body)
