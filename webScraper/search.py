
try:
	from googlesearch import search
except ImportError:
	print("Please install google module")


def pySearch(searchString):
	for i in search(searchString, tld = "co.in", num = 10, stop = 10, pause = 0.5):
		print(i)




if __name__ == "__main__":
	searchString = str(input("Enter Search String: "))

	pySearch(searchString)
