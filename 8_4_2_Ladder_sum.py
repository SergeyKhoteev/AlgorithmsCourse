from _Generate_test_data import generate_ladder_data
from sys import stdin


def main():
	reader = (line.strip() for line in stdin)
	n = int(next(reader))
	steps = list(map(int, next(reader).split()))

	step_sum = get_sum_BU(n = n, array = steps)
	print(step_sum)

	results = [0 if i == 0 else steps[0] if i == 1 else None for i in range(n + 1)]
	step_sum = get_sum_TD(i = n, array = steps, results = results)
	print(step_sum)

def get_sum_BU(n: int, array: list) -> int:
	results = [0 for i in range(n + 1)]
	for i in range(1, n + 1):
		results[i] = array[i - 1] + max(results[i - 1], results[i - 2])
	return results[n]


def get_sum_TD(i: int, array: list, results: list) -> int:
	if results[i] is not None:
		return results[i]
	else:
		predecessor_1 = get_sum_TD(i = i - 1, array = array, results = results)
		predecessor_2 = get_sum_TD(i = i - 2, array = array, results = results)
		results[i] = array[i - 1] + max(predecessor_1, predecessor_2)
		return results[i]



if __name__ == '__main__':
	generate_ladder_data()
	main()
