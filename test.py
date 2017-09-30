from flask import Flask
from flask import render_template
from forms import LoginForm
application = Flask(__name__)
application.config.from_object('config')

@application.route("/")
def hello():
    return render_template ("index.html")

@application.route("/about")
def about():
    return render_template ("about.html")

@application.route("/resume")
def resume():
    return render_template ("resume.html")

@application.route("/projects")
def projects():
    return render_template ("projects.html")

if __name__ == "__main__":
    application.run(host='0.0.0.0')
