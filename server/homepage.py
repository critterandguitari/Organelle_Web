import cherrypy

config = { '/': 
        {
        }
}
base = '/'


class Root(object):
    apps = None
    links = ''
    def __init__(self, apps):
        self.apps = apps
        for app in apps : 
            self.links += '<a href="'+app.base+'">'+app.name+'</a></br>'

    @cherrypy.expose
    def index(self):
        return "<html>Welcome to the Organelle Home </br>" + self.links + '</html>'
