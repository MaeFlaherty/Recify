Welcome to the Recify team! usre this file to quickly get started developing for recify

 ___________________
|					|
|	Dependencies	|
|___________________|

Before launching the site, make sure you have installed: 
- The latest Version of python
- php(to create a test server)
- the beautifulSoup module for python
- the googleSearch module for python
- the web.py module for python
Once all of this is on your machine, you are ready to start a test build of the site

 _______________________
|						|
|	Launching the site	|
|_______________________|

1.	make sure your git repository is on the latest version of the site in order to aviod nasty branch conflicts. to do this, use the command "git pull" 
2.	Go to the Recify folder and use the command "php -S localhost:8000" to start the homepage
3.	Go to the webScraper folder in another terminal window, and use the command "python3 app.py" to start the recify web scraper so that the site can display recipe data

 _______________________________________
|										|
|	Editing the Fontend and Backend		|
|_______________________________________|

Recify is contained within 2 main folders:

recipe-generator-project/Recify:
contains the html, css, and javascript for the main page and satellite pages, as well as the relevant images for this page.
-index.html: html for main recify page
-main.css: css for recify homepage
-gfg.js: javascript for homepage, covers form submission and some css animations
-contact.html: html for contact page
-contacts.css: css for contact us page
-about.html: html for about us page
-aboutUs.css: css for about us page

recipe-generator-project/webScraper:
Contains the webscraper, as well as the app.py python script, which controlls both the search pages

webScraper.py:
	uses the BeautifulSoup library to scrape data from a given link and turn it into a Recipe object, which contains the recipe's name, ingredients, instructions, and a relevant image.

recipeSearch.py:
	Uses the googleSearch python library to find the top 5 search results for a given string, then returns the links to valid recipes that it finds within these links

app.py: 
	Uses the web.py library to generate a display page for the data of a recipe object, as well as the search results page from recipeSearch
	Modules: webScraper.py, recipeSearch.py