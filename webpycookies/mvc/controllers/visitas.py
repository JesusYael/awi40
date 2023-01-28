import web
from datetime import datetime
A= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
class Visitas:
    def GET(self,nombre):
        try:
            print(A)
            cookie = web.cookies()
            visitas = "0"
            web.setcookie("fecha",A,expires="",domain=None)
            if nombre:
                web.setcookie("nombre",nombre,expires="",domain=None)
            else:
                nombre= "Anonimo"
                web.setcookie("nombre",nombre,expires="",domain=None)
            if cookie.get("visitas"):
                visitas = int(cookie.get("visitas"))
                visitas += 1
                web.setcookie("visitas",str(visitas),expires="",domain=None)
            else:
                web.setcookie("visitas",str(1),expires="",domain=None)
                visitas = "1"
            
            return "Visitas "+ str(visitas) + " nombre "+ nombre + " Fecha "+ A    

        except Exception as e:
                return "Error "+ str(e.args)