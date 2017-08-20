from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There! Regards,Thomas , update 9:10 </h1>"

@application.route("/index")
def index():
    user = {'nickname': 'Thomas'}  # fake user
    return  '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''

if __name__ == "__main__":
    application.run(host='0.0.0.0')
