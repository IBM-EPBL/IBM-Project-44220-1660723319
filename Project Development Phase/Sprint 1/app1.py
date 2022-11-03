from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', name="Home")

@app.route("/Homepage")
def homepage():
  return render_template('Homepage.html', name="Homepage")

@app.route("/Register")
def register():
  return render_template('Register.html', name="Register")
if __name__=="__main__":
 app.run(debug=True)