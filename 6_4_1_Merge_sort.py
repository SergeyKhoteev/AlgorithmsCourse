from random import randint


def merge(lst1: list, lst2: list) -> list:
	# print(f'merge(lst1: {lst1}, lst2: {lst2})')
	new_list = []
	global count
	while len(lst1) > 0 and len(lst2) > 0:
		if lst1[0] <= lst2[0]:
			minimum = lst1.pop(0)
			new_list.append(minimum)
		else:
			minimum = lst2.pop(0)
			new_list.append(minimum)
			count += len(lst1)
	if len(lst1) > 0:
		new_list += lst1
	else:
		new_list += lst2
	return new_list


def merge_sort(lst: list, start: int, finish: int) -> list:
	# print(f'merge_sort(lst: {lst[start:finish]}, start: {start}, finish: {finish})')
	if finish - start > 1:
		mid = (start + finish) // 
		return merge(merge_sort(lst, start, mid), merge_sort(lst, mid, finish))
	return lst[start:finish]


def test():
	a = [randint(1 ,int(1e9)) for i in range(int(1e5))]
	a = [randint(1 ,20) for i in range(8)]
	global count
	count = 0
	print(a)
	b = merge_sort(a, 0, len(a))
	print(count)


def main():
	n = input()
	lst = list(map(int, input().split()))
	global count
	count = 0
	print(lst)
	new_lst = merge_sort(lst, 0, len(lst))
	print(count)

if __name__ == '__main__':
	# test()
	main()


# from random import randint

# def merge_sort(array: list, start: int, finish: int):
# 	if finish - start > 1:
# 		m = (start + finish) // 2
# 		return merge(
# 			merge_sort(array = array, start = start, finish = m), 
# 			merge_sort(array = array, start = m, finish = finish))
# 	else:
# 		return array[start:finish]

# def merge(array_1: list, array_2: list):
# 	new_array = []
# 	empty_array = []
# 	while array_1 != empty_array and array_2 != empty_array:
# 		if array_1[0] <= array_2[0]:
# 			new_array.append(array_1.pop(0))
# 		else:
# 			new_array.append(array_2.pop(0))
# 	return new_array + array_1 + array_2


# def main():
# 	array = [randint(1, 100) for i in range(30)]
# 	print(array)
# 	sorted_array = merge_sort(array = array, start = 0, finish = 30)
# 	print(sorted_array)


# if __name__ == '__main__':
# 	main()
