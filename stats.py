def get_word_count(text):
	words = text.split()
	num_words = len(words)

	return num_words


def get_character_count(text):
	text = text.lower()
	char_count = {}

	for char in text:
		if char not in char_count:
			char_count[char] = 0
		if char in char_count:
			char_count[char] += 1

	#print(char_count)
	return char_count


def sort_on(dict):
	return dict["num"]


def sort_dictionary(character_count):
	report = []

	for entry in character_count:
		count = character_count[entry]
		if entry.isalpha():
			report.append({"character": entry, "num": count})

	

	report.sort(reverse=True, key=sort_on)

	return report

	
