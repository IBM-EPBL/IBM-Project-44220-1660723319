from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', name="Home")

@app.route("/about")
def about():
  return render_template('about.html', name="About")


@app.route("/contact")
def contact():
  return render_template('contact.html', name="Contact")

@app.route("/register")
def register():
  return render_template('register.html', name="Register")
if__name__=="__main__":
  app.run(debug=True)