import os.path
import time
import glob
import json
import cherrypy
import urllib
import time
import socket
from cherrypy.lib import static
import imp

current_dir = os.path.dirname(os.path.abspath(__file__))

def get_immediate_subdirectories(dir) :
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]

config = { '/': 
        {
 		'tools.staticdir.on': True,
		'tools.staticdir.dir': current_dir + '/static/',
		'tools.staticdir.index': 'index.html',
        }
}
base = '/sliders'
name = 'Extra Sliders'

class Root():

    def tester(self, name):
        return "TESTdf"
        print "cool"
    tester.exposed = True
  
    def control(self, **data):
        
        print data
        return 'cool'

    control.exposed = True


