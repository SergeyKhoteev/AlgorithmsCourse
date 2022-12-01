from random import randint


class Heap_min():

	### Inits instanse with list, where first item - length
	def __init__(self):
		self.array = [0, ]


	### Insertion of new item in to the heap
	def insert(self, value):
		self.array.append(value)
		self.array[0] += 1
		self.sift_up()


	### Compares child with its parent.
	### If child smaller than parent, swaps and starts comparision again.
	def sift_up(self):
		child = self.array[0]
		while child > 1:
			parent = child // 2
			if self.array[parent] > self.array[child]:
				self.value_changer(parent, child)
				child = parent
			else:
				break

	### Simple method to swap values
	def value_changer(self, index_1, index_2):
		value_1 = self.array[index_1]
		self.array[index_1] = self.array[index_2]
		self.array[index_2] = value_1


	### Checks main rule of the heap.
	### Asserts that cildren always less or equal than parent
	def self_assessment(self):
		limit = self.array[0]
		for i in range(1, limit):
			if i * 2 <= limit:
				assert self.array[i] <= self.array[i * 2], f'{heap.array[i]} <= {heap.array[i * 2]}'
			if i * 2 + 1 <= limit:
				assert self.array[i] <= self.array[i * 2 + 1], f'{heap.array[i]} is not <= {heap.array[i * 2 + 1]}'


	### Returns minimum in the heap. Swaps first and last items and pops minimum.
	### Last item to be sift down.
	def extract_min(self):
		self.value_changer(1, -1)
		minimum = self.array.pop()
		self.array[0] -= 1
		self.sift_down(1)
		return minimum


	### Compares parent with its child. If childs smaller than parent, swaps with the smallest
	def sift_down(self, parent_index):
		limit = self.array[0]
		while parent_index * 2 <= limit:
			parent = self.array[parent_index]
			child_1_index = parent_index * 2
			child_1 = self.array[child_1_index]
			if parent_index * 2 + 1 <= limit:
				child_2_index = parent_index * 2 + 1
				child_2 = self.array[child_2_index]
				if parent <= child_1 and parent <= child_2:
					break
				if child_1 <= parent <= child_2:
					self.value_changer(parent_index, child_1_index)
					parent_index = child_1_index
					continue
				if child_2 <= parent <= child_1:
					self.value_changer(parent_index, child_2_index)
					parent_index = child_2_index
					continue
				if parent >= child_1 and parent >= child_2:
					if child_1 <= child_2:
						self.value_changer(parent_index, child_1_index)
						parent_index = child_1_index
						continue
					else:
						self.value_changer(parent_index, child_2_index)
						parent_index = child_2_index
						continue
			else:
				if parent <= child_1:
						break
				else:
					self.value_changer(parent_index, child_1_index)
					break


def main():
	### Declare heap_min instanse
	heap = Heap_min()

	### Insertion of values in to the heap
	for i in range(int(2e5)):
		heap.insert(randint(-1e9, 1e9))
	heap.self_assessment()

	### Creation of sorted list
	sorted_list = []
	for i in range(int(1e5)):
		sorted_list.append(heap.extract_min())
	heap.self_assessment()

	### Vrification of the result
	# for i in range(1, int(1e3)):
	# 	assert res_list[i] >= res_list[i - 1]

if __name__ == '__main__':
	main()
