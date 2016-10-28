from flask import Flask
from flask import jsonify
from flask import render_template
from flask import send_file

from read_data import DataReader

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# pre-load fixed tweets
def pre_load_fixed_data():
    keywords = ["music", "food", "sport", "show", "movie", "car", "commercial", "party", "war", "hello"]
    data = DataReader()
    return data.read("static/data/tweets.txt", keywords)

tweets_json = pre_load_fixed_data()

@application.route('/')
def index():
    return render_template('index.html')
@application.route('/search/<keyword>')
def search(keyword=None)
    r=requests.get("url"+keyword+"&size=10000")
    output_coord=[]
    dic=jsonify(r)
    length=len(dic["hits"]["hits"])
    for i in xrange(0,length):
        coord=[float(dic['hits']['hits'][i]['_source']['geo'][0]),float(dic['hits']['hits'][i]['_source']['geo'][1])]
        output_coord.append(coord)
    json_output_coord=json.dumps(output_coord)
    return json_output_coord
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

@application.route('/images/<filename>')
def get_image(filename=None):
    return send_file('static/img/'+filename, mimetype='image/png')

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #application.debug = True
    application.run()
