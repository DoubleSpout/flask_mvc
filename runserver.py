from trymenu import app
from trymenu.controllers import *
from trymenu.models import *

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000)
    
    
    
