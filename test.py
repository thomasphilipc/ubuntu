from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There! Regards,Thomas , update 9:10 </h1>"

@application.route("/index")
def index():
    return "<h1 style='color:blue'>Hello There! You are on the index page </h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
