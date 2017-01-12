from xmlrpc.server import SimpleXMLRPCServer

import logging
import os

# Set up logging
logging.basicConfig(level=logging.DEBUG)

server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)

# Expose a function
def list_contents(dir_name):
    logging.debug('list_contents(%s)', dir_name)
    return os.listdir(dir_name)
server.register_function(list_contents)

try:
    print ('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print ('Exiting')

'''
def file_reader(file_name):
    with open(file_name, 'r') as f:
        return f.read()

server = SimpleXMLRPCServer(('localhost', 8000))
server.register_introspection_functions()

server.register_function(file_reader)
server.serve_forever()
'''