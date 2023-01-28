import web

urls = (
    '/(.*)', 'mvc.controllers.visitas.Visitas',
)
app = web.application(urls, globals()) #aplicacion web

if __name__ == "__main__":
    web.config.debug = False
    app.run()