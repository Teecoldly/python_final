
from flask import Flask,render_template,request
import sqlite3
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def home():
    if (request.method  == 'POST'):
        username = request.form['username']
        password = request.form['password']
        if login(username,password):
            data = loaddetail(username,password)
            return render_template('userinfo.html',data=data)
             

        
    return render_template('index.html')


def loaddetail(username,password):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    result = cur.execute("select * from userinfo where username='"+username +"'and password = '" + password+"'")
    data = []
    for i in result:
        for d in i:
            data.append(d)
    conn.close()
    return data     
def login(username,password):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    result = cur.execute("select count(*) from userinfo where username='"+username +"'and password = '" + password+"'")
    for i in result:
        for d in i:
            data = d
    conn.close()
    return data          
if __name__ == "__main__":
    app.debug = True
    app.run(host ='localhost',port=8000)
 