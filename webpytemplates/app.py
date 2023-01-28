import web
from web import form

urls = (
    '/', 'Index',
)
app = web.application(urls, globals()) #aplicacion web
render = web.template.render('templates/', base='index')


class Index:
    def GET(self):
        datos= [
            ["1","Dejah"],
            ["2","Jhon"],
            ["3","alfre"],
            ["4","oscar"]
        ]
        return render.tabla(datos)
        
if __name__ == "__main__":
    web.config.debug = False
    app.run()