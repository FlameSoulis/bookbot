import sys
from stats import get_word_count, get_letter_count, get_letters_sorted

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents

def print_letters(letters_dict):
	for letter in letters_dict:
		if letter.isalpha():
			print(f"{letter}: {letters_dict[letter]}")

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book = sys.argv[1]
	print("============ BOOKBOT ============")
	book_contents = get_book_text(book)
	num_words = get_word_count(book_contents)
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	sorted_book_letters = get_letters_sorted(get_letter_count(book_contents))
	print_letters(sorted_book_letters)

main()