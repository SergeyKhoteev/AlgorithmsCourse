from operator import itemgetter

def huffman_encoding(string: str):
	assert len(string) <= 1e4, "String is too long"

	letter_list= []
	b = []
	i = 0
	string_sorted = sorted(string)
	while i != len(string_sorted):
		count = string_sorted.count(string_sorted[i])
		letter_list.append([string_sorted[i], count])
		b.append([string_sorted[i], count])
		i += count
	letter_list = sorted(letter_list, key=itemgetter(1))
	b = sorted(b, key=itemgetter(1), reverse=True)

	encoding_list = []
	while len(letter_list):
		if len(letter_list) > 1:
			first = letter_list.pop(0)
			first.append('0')
			encoding_list.append(first)
			second = letter_list.pop(0)
			second.append('1')
			encoding_list.append(second)
			letter_list.append([first[0]+second[0], first[1] + second[1]])
			letter_list = sorted(letter_list, key=itemgetter(1))
		else:
			if len(encoding_list) == 0:
				first = letter_list.pop(0)
				first.append('0')
				encoding_list.append(first)
				break
			break

	encoding_list = sorted(encoding_list, key=itemgetter(1), reverse=True)
	for i in b:
		str1 = ''
		for j in encoding_list:
			if i[0] in j[0]:
				str1 += j[2]
		i.append(str1)
		string = string.replace(i[0], str1)

	print(len(b), len(string))
	for i in b:
		print(i[0], ': ', i[2], sep='')
	print(string)	


def main():
	string = input()
	huffman_encoding(string)


if __name__ == '__main__':
	main()
	
	