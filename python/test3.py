def contains(string_array=["hello","hi"]):

	output = [x for x in string_array if "o" in x]
	return output


if __name__ == "__main__":
	print(contains(string_array=["hoho","pirat","soda"]))