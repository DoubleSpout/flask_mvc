# -*- coding: utf-8 -*-
from trymenu import app
from trymenu import config
from trymenu.controllers import *
from trymenu.models import *
import os
import sys
import getopt

__opts, _ = getopt.getopt(sys.argv[1:], "e:") #获取命令行参数
__scritpEnv = ""

for name, value in __opts:
    if name == "-e": #获取命令行参数e
        __scritpEnv = value
        

if __scritpEnv == "Production" :
    app.config.from_object(config.Production())
else:
    app.config.from_object(config.Debug())

if __name__ == '__main__':
    app.run(host=app.config.get("HOST"),port=app.config.get("PORT"))
    
    
    
