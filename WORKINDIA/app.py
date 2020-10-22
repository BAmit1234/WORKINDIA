from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app= Flask(__name__)

app.config['MYSQL_HOST']='localhost:3306'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='database'
mysql = MySQL(app)
@app.route('/')

def home():
    return render_template("login.html")

@app.route('/registration')
def reg():
    
    
    return render_template("registration.html")
@app.route('/notes')
def notes():
    return render_template("notes.html")





if __name__=='__main__':
     app.run(debug=True)
    
