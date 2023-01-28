import web

urls = (
    '/', 'Index',
    '/bienvenida','Bienvenida'
)
app = web.application(urls, globals()) #aplicacion web
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()

class Bienvenida:
    def GET(self):
        return render.bienvenida("Hola como estas")

if __name__ == "__main__":
    app.run()