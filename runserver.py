from trymenu import app
from trymenu import config
from trymenu.controllers import *
from trymenu.models import *
import os

__env = os.environ.get("FLASKENV")

if __env == "Production" :
    app.config.from_object(config.Production())
else:
    app.config.from_object(config.Debug())
    
if __name__ == '__main__':
    app.run(host=app.config.get("HOST"),port=app.config.get("PORT"))
    
    
    
