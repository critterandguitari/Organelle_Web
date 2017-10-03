import cherrypy
import imp 
import helpers
import homepage
import traceback

APPS_PATH = '../apps/'

# global config
cherrypy.config.update({    'environment': 'production',
                            'log.error_file': '/tmp/site.log',
                            'log.screen': True,
                            'server.socket_host': '0.0.0.0',
                            'server.socket_port': 8080,
                        })
# load apps
print "loading apps..."
app_folders = sorted(helpers.get_immediate_subdirectories(APPS_PATH), key=lambda s: s.lower() )
apps = []
for app_folder in app_folders :
    app_name = str(app_folder)
    app_path = APPS_PATH+app_name+'/app.py'
    print 'loading: ' + app_path
    try :
        app = imp.load_source(app_name, app_path)
        cherrypy.tree.mount(app.Root(), app.base, app.config)
        apps.append(app)
    except Exception, e:
        print traceback.format_exc()

# load home 
cherrypy.tree.mount(homepage.Root(apps), homepage.base, homepage.config)

# start webserver
cherrypy.engine.start()
cherrypy.engine.block()
