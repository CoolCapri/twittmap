from flask import Flask
from flask import jsonify
from flask import render_template
from flask_socketio import SocketIO

from read_data import DataReader

# EB looks for an 'application' callable by default.
application = Flask(__name__)
#application.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(application)

# pre-load fixed tweets
def pre_load_fixed_data():
    keywords = ["music", "food", "sport", "show", "movie", "car", "commercial", "party", "war", "hello"]
    data = DataReader()
    return data.read("static/data/tweets.txt", keywords)

tweets_json = pre_load_fixed_data()

@application.route('/')
def index():
    return render_template('test1.html')

@application.route('/searchf/')
@application.route('/searchf/<keyword>')
def searchf(keyword=None):
    if keyword is None:
        to_return = jsonify(**tweets_json)
    else:
        tweets_of_keyword = {keyword: []}
        if keyword in tweets_json:
            tweets_of_keyword = {keyword: tweets_json[keyword]}
        to_return = jsonify(**tweets_of_keyword)
    return to_return

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
