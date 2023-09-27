#!/usr/bin/python3
from flask import Flask,request,Response
from jupiter_api import *
app = Flask(__name__)
@app.route("/api/list/classes",methods=['POST'])
def list_the_classes():
 if request.method == 'POST':
  if request.form.get('school_year'):
   return list_classes(request.form.get('user'),request.form.get('pass'), request.form.get('school_year'))
  else:
   return list_classes(request.form.get('user'),request.form.get('pass'))

@app.route("/api/profile_picture",methods=['POST'])
def get_the_image():
 if request.method == 'POST':
  return Response(get_picture(request.form.get('user'),request.form.get('pass')), mimetype="image/jpg")

@app.route("/api/list/grades",methods=['POST'])
def list_the_grades():
 if request.method == 'POST':
  if request.form.get('school_year'):
   return list_grades(request.form.get('user'),request.form.get('pass'), request.form.get('school_year'))
  else:
   return list_grades(request.form.get('user'),request.form.get('pass'))
app.run()
