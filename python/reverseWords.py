def reverseWords(input)：
	inputWords = input.split(" ")

	inputWords = inputWords[-1 : : -1]

	output = ' '.joint(inputWords)

	return output

if __name__ == '__main__':
	input = 'I like python'
	rw = reverseWords(input)
	print(rw)
