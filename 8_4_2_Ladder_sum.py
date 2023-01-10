from _Generate_test_data import generate_ladder_data
from sys import stdin


def main():
	reader = (line.strip() for line in stdin)
	n = int(next(reader))
	steps = list(map(int, next(reader).split()))

	step_sum = get_sum_BU(n = n, array = steps)
	print(step_sum)

	# results = [steps[i] if i == 0 else 'x' for i in range(n)]
	# step_sum = get_sum_TD(n = n - 1, array = steps, results = results)
	# print(results)
	# print(step_sum)

def get_sum_BU(n: int, array: list) -> int:
	if n == 1:
		return array[0]
	results = [0 for i in range(n)]
	print(results)
	for i in range(n):
		results[i] = array[i] + max(results[i - 1], results[i - 2])
	# print(results)
	return results[n - 1]


# def get_sum_TD(n: int, array: list, results: list) -> int:
# 	if results[n] != 'x':
# 		return results[n]
# 	else:
# 		predecessor_1 = get_sum_TD(n = n - 1, array = array, results = results)
# 		predecessor_2 = get_sum_TD(n = n - 2, array = array, results = results)
# 		results[n] = array[n] + max(predecessor_1, predecessor_2)
# 		print(f'results for n = {n}: {results}')
# 		return results[n]



if __name__ == '__main__':
	# generate_ladder_data()
	main()
