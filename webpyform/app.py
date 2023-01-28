import web
from web import form

urls = (
    '/', 'Index',
)
app = web.application(urls, globals()) #aplicacion web
render = web.template.render('templates')


class Index:
    def GET(self):
        return render.index()

    def POST(self):
        data = web.input()
        return data["nombre"]

if __name__ == "__main__":
    web.config.debug = False
    app.run()