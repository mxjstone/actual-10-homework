from flask import request,render_template, redirect,session
from app import app

@app.route('/idc')
def idc():
   if not session.get('username',None):
        return redirect("/login")
   return  render_template('idc.html',info=session)

@app.route('/cabinet')
def cabinet():
   if not session.get('username',None):
        return redirect("/login")
   return  render_template('cabinet.html',info=session)

@app.route('/server')
def server():
   if not session.get('username',None):
        return redirect("/login")
   return  render_template('server.html',info = session)
