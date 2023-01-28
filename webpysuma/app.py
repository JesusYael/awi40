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
        data= dict(web.input())
        print(data)
        n1= int(data['n1'])
        n2= int(data['n2'])
        if data['operacion']=="sumar":
            resultado = n1+n2
            return "La suma de",n1,"mas",n2,"es",resultado
        if data['operacion']=="restar":
            resultado = n1-n2
            return "La resta de",n1,"menos",n2,"es",resultado
        if data['operacion']=="multiplicar":
            resultado = n1*n2
            return "La multiplicacion de",n1,"*",n2,"es",resultado
        if data['operacion']=="dividir":
            resultado = n1/n2
            return "La division de",n1,"entre",n2,"es",resultado




if __name__ == "__main__":
    web.config.debug = False
    app.run()