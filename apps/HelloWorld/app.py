import cherrypy

config = { '/': 
        {
        }
}
base = '/helloworld'


class Root(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"
