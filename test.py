from flask import Flask
from flask import render_template
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There! Regards,Thomas , update 9:10 </h1>"

@application.route("/index")
def index():
    user = {'nickname': 'Thomas'}  # fake user
    return  render_template('index.html',title='Home',user=user)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
