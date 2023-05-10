import webScraper
from webScraper import Recipe
try:
	from googlesearch import search
except ImportError:
	print("Please install google module")


def pySearch(searchString):
	validSites = 0
	searchResults = []
	for i in search(searchString, tld = "co.in", num = 10, stop = 10, pause = 0.5):
		print(i)
		if webScraper.verifyJSON(i):
			searchResults.append(i)
			validSites += 1
	print(f"Valid Recipes Found: {validSites}")
	return searchResults




if __name__ == "__main__":
	searchString = str(input("Enter Search String: "))
	results = pySearch(searchString)

	for i in results:
		data = webScraper.get_ld_json(i)
		recipe = Recipe(data)
		print(recipe.name)

