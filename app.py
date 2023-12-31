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

@app.route("/api/list/teachers", methods=['POST'])
def list_the_teachers():
 if request.method == 'POST':
  if request.form.get('school_year'):
   return list_teachers(request.form.get('user'),request.form.get('pass'), request.form.get('school_year'))
  else:
   return list_teachers(request.form.get('user'),request.form.get('pass'))

@app.route("/api/gpa", methods=['POST'])
def get_the_gpa():
 if request.method == 'POST':
  if request.form.get('school_year'):
   return calculate_gpa(request.form.get('user'),request.form.get('pass'), request.form.get('school_year'))
  elif request.form.get('mp'):
   return calculate_gpa(request.form.get('user'),request.form.get('pass'), "current", request.form.get('mp'))
  elif request.form.get('mp') and request.form.get('school_year'):
   return calculate_gpa(request.form.get('user'),request.form.get('pass'), request.form.get('school_year'), request.form.get('mp'))
  else:
   return calculate_gpa(request.form.get('user'),request.form.get('pass'))
app.run()
