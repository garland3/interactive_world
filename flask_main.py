from flask import Flask
from flask import render_template
from flask import request
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy


import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from lib.world import *
from lib.db import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maindb.sqlite3'
app.config['uploads_static']='uploaded_data\\images'



app.add_url_rule('/world/', view_func=World.as_view('world'))
app.add_url_rule('/worldimg/<int:post_id>/', view_func=GetImageForWorld.as_view('worldimg'))

dbwrapper.setdb(app)
dbwrapper.setroot(app.root_path)


@app.route('/upload/', methods = ['GET','POST'])
def upload(name=None):
    result = "Ready for Upload "
    if request.method == "POST":
        result = ProcessUpload(request)
    return render_template('upload.html', result=result)
  
def ProcessUpload(request):
    # try:
    p = Path("./uploaded_data/images")
    imgfiles = list(p.glob("*.png"))
    new_num = max([int(file.stem) for file in imgfiles])+1 if len(imgfiles) > 0 else 0
    p  = p / f"{new_num}.png"
    f = request.files['fileToUpload']
    print(p)
    f.save(str(p))  
    dbwrapper.db.session.add(imagefile(str(p)))
    dbwrapper.db.session.commit()
    return "Success!"
    # except:
        # return "Failed :("
   






if __name__ == "__main__":
    # SetupDb()
    app.run()