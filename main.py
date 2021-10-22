# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
import re
from ping3 import ping
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route('/list')
def list():
    ret = ""
    file1 = open('/etc/hosts', 'r')
    count = 0
    while True:
        count += 1 
        line = file1.readline()
        if not line:
            break
        line = line.strip()
        if not line.startswith("#"):
            parts = re.split(r' ', line)
            if parts[0].startswith('10.'):
                 if parts[1].strip() != "":
                     r = ping(parts[0], ttl=2, timeout=3)
                     ok = "-"
                     if isinstance(r, float): 
                          ok = "ONLINE"
                     ret = ret + parts[1] + " " + ok + "<br />"
    file1.close()
    return ret


# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0', port=808)