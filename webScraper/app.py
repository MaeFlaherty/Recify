import web
import webScraper
from webScraper import Recipe

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

            recipe = Recipe(data)
            
            return self.render.index(recipe.name, recipe.ingredients, recipe.instructions, recipe.image)
            

            

if __name__ == "__main__":
    app.run()