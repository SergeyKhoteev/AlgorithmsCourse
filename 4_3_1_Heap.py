
class Heap:


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
		length = len(self.body) - 1
		while True:
			if length - (parent_index * 2) >= 1:
				child_1 = self.body[parent_index * 2]
				child_2 = self.body[parent_index * 2 + 1]
				if self.body[parent_index] > child_1 and self.body[parent_index] > child_2:
					break
				else:
					if child_1 >= child_2:
						self.body[parent_index * 2] = self.body[parent_index]
						self.body[parent_index] = child_1
						parent_index = parent_index * 2
						continue
					else:
						self.body[parent_index * 2 + 1] = self.body[parent_index]
						self.body[parent_index] = child_2
						parent_index = parent_index * 2 + 1
						continue
			elif length - parent_index * 2 == 0:
				child_1 = self.body[parent_index * 2]
				if child_1 > self.body[parent_index]:
					self.body[parent_index * 2] = self.body[parent_index]
					self.body[parent_index] = child_1
					break
				else:
					break
			elif length - parent_index * 2 < 0:
				break
		return response

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


def main():
	heap = Heap()
	k = int(input())
	for l in range(k):
		command = input().split()
		if command[0] == 'Insert':
			heap.insert(int(command[1]))
		if command[0] == 'ExtractMax':
	 		print(heap.extract_max())


def test():
	heap = Heap()
	result_list = []
	for i in range(1000):
		heap.insert(i+1)
		result_list.append(heap.extract_max())
		if i > 0:
			assert result_list[i] - result_list[i-1] == 1
	heap.insert(15)
	heap.insert(15)
	heap.insert(15)
	print(heap.extract_max())

if __name__ == '__main__':
	main()
