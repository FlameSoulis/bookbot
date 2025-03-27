def get_word_count(the_string):
	temp_list = the_string.split()
	return len(temp_list)

def get_letter_count(the_string):
	#aw hell
	test_string = the_string.lower()
	letter_dict = {}
	for letter in test_string:
		if letter not in letter_dict:
			letter_dict[letter] = 0
		letter_dict[letter] += 1
	return letter_dict

def sort_on_num(dict):
	return dict["num"]

def get_letters_sorted(unsorted_dict):
	# convert to a list
	temp_list = []
	for letter in unsorted_dict:
		temp_list.append({"name":letter, "num":unsorted_dict[letter]})
	temp_list.sort(reverse=True, key=sort_on_num)
	sorted_dict = {}
	for letter in temp_list:
		sorted_dict[letter["name"]] = letter["num"]
	return sorted_dict