from flask import Flask, render_template, jsonify

app = Flask(__name__)

TUTOR =[
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
def hello_world():
  return render_template('login.html', 
                         tutor=TUTOR,
                        company_name='Technopolis')
@app.route("/api/tutor")
def list_tutor():
  return jsonify(TUTOR)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


