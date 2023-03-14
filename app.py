from flask import Flask, render_template#, jsonify
from database import load_jobs_from_db

app = Flask(__name__)



@app.route("/")
def home():
  tutor = load_jobs_from_db()
  return render_template('home.html', 
                       tutor=tutor,
                       company_name='Technopolis')

def Avail():
  tutor = load_jobs_from_db()
  return render_template('availpositions.html', 
                       tutor=tutor, company_name='Technopolis')
# @app.route("/api/tutor")
# def list_tutor():
#   return jsonify(TUTOR)
@app.route("/home/")
def home_page():
  return render_template('home.html')

@app.route("/login/")
def login_page():
  return render_template('login.html')

@app.route("/signup/")
def signup_page():
  return render_template('signup.html')

@app.route("/availpositions/")
def availpositions_page():
  return render_template('availpositions.html')

@app.route("/myprofile/")
def myprofile_page():
  return render_template('myprofile.html')

@app.route("/application/")
def application_page():
  return render_template('application.html')
# home link = https://technopolis.sansprogram.repl.co
# sigup link = https://technopolis.sansprogram.repl.co/signup/
# login link = https://technopolis.sansprogram.repl.co/login/
# profile link = https://technopolis.sansprogram.repl.co/myprofile
# available positions link = https://technopolis.sansprogram.repl.co/availpositions/ 

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


