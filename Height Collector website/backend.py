from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"]="postgresql://postgres:Chiquita.2014@localhost/Height_collector"
db=SQLAlchemy(app)


class Data(db.Model):
    __tablename__="data"
    id=db.Colimn(db.Integer, primary_key=True)
    email_=db.Coloum(db.String(120), unique=True)
    height_=db.Coloumn(db.integer)
    
    def __init__(self, email, height):
        self.email=email_
        self.height=height_


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    if request.method=="POST":
        email=request.form["email_name"]
        height=request.form["height_name"]
        
        return render_template("success.html")

if __name__ =="__main__":
    app.debug=True
    app.run()