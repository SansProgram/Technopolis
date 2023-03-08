from flask import Flask, render_template, jsonify

app = Flask(__name__)

TUTOR =[
  {
    'id': 1,
    'title': 'Tutor Position',
    'location': 'DUT Steve Biko, ML Sutan, Ritson Campuses',
    'salary': 'R1500.00',
    'department': ''
  },
  {
    'id': 2,
    'title': 'Teacher Assistant',
    'location': 'DUT Steve Biko, ML Sutan, Ritson Campuses',
    'salary': 'R1000.00',
    'department': ''
  },
  {
    'id': 1,
    'title': 'Tutor Position',
    'location': 'DUT Steve Biko, ML Sutan, Ritson Campuses',
    'salary': 'R1500.00',
    'department': ''
  },
  {
    'id': 1,
    'title': 'Tutor Position',
    'location': 'DUT Steve Biko, ML Sutan, Ritson Campuses',
    'salary': 'R00.00',
    'department': ''
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         tutor=TUTOR,
                        company_name='Technopolis')
@app.route("/api/tutor")
def list_tutor():
  return jsonify(TUTOR)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


