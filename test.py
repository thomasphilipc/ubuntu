from flask import Flask
from flask import render_template
from forms import LoginForm
application = Flask(__name__)
application.config.from_object('config')

@application.route("/")
def hello():
    return "<h1> Thomas has forgotten about this website. remind him</h1>"

@application.route("/index")
def index():
    user = {'nickname': 'Thomas'}  # fake user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)

@application.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username)
        print(form.password)
    return render_template('login.html', title='Sign In', form=form)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
