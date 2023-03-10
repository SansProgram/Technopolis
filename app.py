from flask import Flask, render_template, jsonify

app = Flask(__name__)

Positions =[
  {
    'id': 1,
    'title': 'Tutor Position',
    'department': 'Information Technology',
    'location': 'DUT Steve Biko, ML Sutan, Ritson Campuses',
    'salary': 'R200.00 p/h',
    
  },
  {
    'id': 2,
    'title': 'Teacher Assistant',
    'department': 'Information Systems',
    'location': 'DUT Steve Biko, ML Sutan, Ritson Campuses',
    'salary': 'R1000.00 p/m'
  },
  {
    'id': 1,
    'title': 'Tutor Position',
    'department': 'Statistics',
    'location': 'DUT Steve Biko, ML Sutan, Ritson Campuses',
    'salary': 'R200 p/h',
    
  }
]

@app.route("/")
def home():
  return render_template('home.html', 
                         tutor=Positions,
                        company_name='Technopolis')
@app.route("/api/tutor")
def list_tutor():
  return jsonify(Positions)

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
# home link = https://technopolis.sansprogram.repl.co
# sigup link = https://technopolis.sansprogram.repl.co/signup/
# login link = https://technopolis.sansprogram.repl.co/login/
# profile link = https://technopolis.sansprogram.repl.co/myprofile
# available positions link = https://technopolis.sansprogram.repl.co/availpositions/ 

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


