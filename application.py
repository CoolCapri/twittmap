from flask import Flask
from flask import render_template
from flask_socketio import SocketIO

from read_data import ReadData

# EB looks for an 'application' callable by default.
application = Flask(__name__)
application.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(application)

keywords = ["music, food, sport, tv, java, python, aws"]
data = ReadData()
tweets = data.read("static/data/tweets.txt", keywords)
for keyword in tweets.keys():
    print(len(tweets[keyword]))

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/hello/')
def hello():
    return render_template('test1.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #application.debug = True
    application.run()
