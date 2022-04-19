from flask import Flask
import json
import os

app = Flask(__name__)

@app.route('/pub/')
def pubbing():
    strPub = ''
    with open(os.path.expanduser("~/Documents/develop/web_flask/app/pubdata_flask.json")) as file:
        data = json.load(file)
    for i in data["x"]:
        test = i["name"]
        strPub = strPub + ', ' + test
        # print(test)
    return strPub

# from app import routes
@app.route('/')
def hello():
    # filename = 'pubs_test.json'
    # filepath = '~/Documents/develop/web_flask/app/'
    # fullfile = os.path.join(filepath, filename)
    # json_file_path = "/path/to/example.json"
    #
    # with open(os.path.expanduser("~/Documents/develop/web_flask/app/pubs.json")) as file:
    # # with open(fullfile) as file:
    #     contents = json.loads(file.read())
    #     # data = json.load(file)
    #     # pub_dict = json.loads(data)
    # test = contents['name']
    # tester = f"hi {test}"
    # return tester
    return 'hello world'


