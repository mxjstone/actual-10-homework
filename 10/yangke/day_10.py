from flask import Flask
from flask import redirect,render_template,session,request
from db import *
import json

app = Flask(__name__)
app.secret_key = "dfahiu2jf"

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        login_info = dict((k, v[0]) for k, v in dict(request.form).items())
        if not checkuser({"name": login_info["name"]}, "name"):
            return json.dumps({"code": 0, "result":"user is not exist"})
        if login_info["password"] != checkuser({'name': login_info["name"]})[0]:
            return json.dumps({"code": 0, "result":"password error"})

        u_role = checkuser({"name": login_info["name"]}, "role")
        session["username"] = login_info["name"]
        session["role"] = u_role
        return json.dumps({"code": 1,"result":"login success"})


@app.route('/')
def index():
    if not session.get("username",None):
        return redirect("/login")
    return render_template("index.html")

@app.route('/userlist')
def user_list():
    if not session.get("username",None):
        return redirect("/login")
    fields = ["id", "name", "name_cn", "mobile", "email", "role", "status"]
    data = userlist(fields)
    return render_template("userlist.html", users=data, info=session)

@app.route('/add',methods=["GET","POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        addinfo = dict((k, v[0]) for k, v in dict(request.form).items())
        if checkuser({"name": addinfo["name"]}, "name"):
            return json.dumps({"code":1,"errmsg":"user is exist"})
        adduser(addinfo)
        return json.dumps({"code":0,"result":"add user success"})

@app.route('/delete')
def dele():
    if not session.get("username",None):
        return redirect("/login")
    uid = request.args.get("id")
    delete(uid)
    return json.dumps({"code":0,"result":"delete user success"})

@app.route('/update',methods=["GET","POST"])
def up():
    if request.method == "GET":
        uid = request.args.get("id")
        userinfo = getone(uid)
        return json.dumps(userinfo)
    else:
        userinfo = dict((k,v[0]) for k,v in dict(request.form).items())
        modfiy(userinfo)
        return json.dumps({"code":0})

@app.route('/idc')
def idc():
    return render_template("idc.html")

@app.route('/server')
def server():
    return render_template("server.html")

@app.route('/cabinet')
def cabinet():
    return render_template("cabinet.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000,debug=True)
