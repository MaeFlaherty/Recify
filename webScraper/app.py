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
        else:
            try:
                data = webScraper.get_ld_json(link)

                name = data["name"]
                ingredients = data["recipeIngredient"]
                instructions = data["recipeInstructions"]
                instructionsList = []
                for count, inst in enumerate(instructions):
                    instructionsList.append(instructions[count]["text"])

                return self.render.index(name, ingredients, instructionsList)

            except:
                link = "Couldn't generate recipe, try again"
        return link

if __name__ == "__main__":
    app.run()