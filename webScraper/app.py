import web
import webScraper

urls = (
    '/(.*)', 'index'
)
app = web.application(urls, globals())

class index:
    def __init__(self):
        self.render = web.template.render("templates/")

    def GET(self, link):
        if not link:
            link = 'Error, Link Invalid'
            return link

        else:
            try:
                data = webScraper.get_ld_json(link)
            except:
                print("ld+json not found")
                link = "Couldn't generate recipe, try again"
                return link

            try:
                name = data["name"]
                print(name)
            except KeyError:
                name = "NULL"

            try:
                ingredients = webScraper.stripList(data["recipeIngredient"])
            except KeyError:
                ingredients = ["Not Found"]

            try: 
                image = data["image"]
            except:
                image = "Not Found"

            try: 
                instructions = data["recipeInstructions"]
            except KeyError:
                instructions = [{"text": "Not Found"}]

            instructionsList = []
            for count, inst in enumerate(instructions):
                instructionsList.append(instructions[count]["text"])
            instructionsList = webScraper.stripList(instructionsList)
            return self.render.index(name, ingredients, instructionsList, image[0])
            

            

if __name__ == "__main__":
    app.run()