from flask import Flask, url_for, send_from_directory
from flask import render_template
from flask import request
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask import url_for


import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from flask.views import View

from  .db import dbwrapper
from  .db import imagefile as imagefile

# @app.route('/world/')
# def hello(name=None):
#     data = {"js":url_for('static', filename='move.js')}
#     data.update({'css':url_for('static', filename='world.css') })    
#     return render_template('world.html',data= data)
def get_img_url(filepath):
    id = Path(filepath).stem 
    return str(request.host_url+f"worldimg/{id}/")

class World(View):
    def dispatch_request(self):        
        data = {"js":url_for('static', filename='move.js')}
        data.update({'css':url_for('static', filename='world.css') })
        db = dbwrapper.getdb()
       
        # imgDict = {str(img.id):str(url_for(f"worldimg", post_id=img.id)) for img in imagefile.query.all()}
        # imgDict = {str(img.id): get_img_url(img.id) for img in imagefile.query.all()}
        imglist = [ get_img_url(img.path) for img in imagefile.query.all()]
        data['imgs'] = imglist
        print(imglist)
        # print(send_from_directory('uploaded_data/images', filename='1.png'))

        # print (data)
        return render_template('world.html',data= data)

class GetImageForWorld(View):
    def dispatch_request(self,post_id):
        print(post_id)
        return send_from_directory('uploaded_data/images', filename=f"{post_id}.png")
        # return str(post_id)