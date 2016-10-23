from flask import Flask
from flask import render_template

# EB looks for an 'application' callable by default.
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/hello/')
@application.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #application.debug = True
    application.run()
