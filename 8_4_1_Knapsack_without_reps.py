# from _Generate_test_data import generate_knapsack_data
from sys import stdin


def main():
	reader = (tuple(map(int, line.split())) for line in stdin)
	capacity, n = next(reader)
	ingots = list(next(reader))
	result = get_best_result(capacity = capacity, n = n, ingots = ingots)

def get_best_result(capacity: int, n: int, ingots: list) -> int:
	values = [0 for i in range(capacity + 1)]
	items = [[] for i in range(capacity + 1)]
	maximum = 0
	for i in range(capacity + 1):
		for j in range(n):
			if ingots[j] > i:
				continue
			if ingots[j] == i:
				values[i] = ingots[j]
				items[i] = [j]
				break
			if ingots[j] < i:
				if values[i] == 0:
					values[i] = ingots[j]
					items[i] = [j]
				if values[i] <= ingots[j] + values[i - ingots[j]] <= i:
					if j not in items[i - ingots[j]]:
						values[i] = ingots[j] + values[i - ingots[j]]
						items[i] = items[i - ingots[j]] + [j]
			if values[i] > maximum:
				maximum = values[i]
	print(maximum)

if __name__ == "__main__":
	# generate_knapsack_data()
	main()
