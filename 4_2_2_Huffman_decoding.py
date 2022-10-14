def decode_huffman(inputs: list) -> str:
	letters_dict = inputs[0]
	string = inputs[1]

	anal_string = ''
	for digit in string:
		anal_string += digit
		if anal_string in letters_dict.keys():
			letters_dict[anal_string]
			print(letters_dict[anal_string], end='')
			anal_string = ''
	print()

def get_input_data():
	letters_dict = {}
	ran, length = tuple(map(int, input().split()))
	for i in range(ran):
		key, value = input().split()
		letters_dict[value] = key[:-1]
	return [letters_dict, input()]


def main():
	decode_huffman(get_input_data())


if __name__ == '__main__':
	main()

