from stats import get_word_count, get_character_count, sort_dictionary
import sys

def get_book_text(filepath):
	file_contents = ""

	with open(filepath) as f:
		file_contents = f.read()

	return file_contents


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	# text = get_book_text("books/frankenstein.txt")
	text = get_book_text(sys.argv[1])
	word_count = get_word_count(text)
	char_count = get_character_count(text)
	analysis = sort_dictionary(char_count)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for entry in analysis:
		print(f"{entry["character"]}: {entry["num"]}")
	print("============= END ===============")


main()