import cherrypy
import imp 

cherrypy.config.update({    'environment': 'production',
                            'log.error_file': '/tmp/site.log',
                            'log.screen': True,
                            'server.socket_host': '0.0.0.0',
                            'server.socket_port': 80,
                        })

HelloWorld = imp.load_source('HelloWorld', '/usbdrive/WebServer/apps/HelloWorld/app.py')
FileManager = imp.load_source('FileManager', '/usbdrive/WebServer/apps/FileManager/app.py')

cherrypy.tree.mount(FileManager.Root(), FileManager.base, FileManager.config)
cherrypy.tree.mount(HelloWorld.Root(), HelloWorld.base, HelloWorld.config)

cherrypy.engine.start()
cherrypy.engine.block()
