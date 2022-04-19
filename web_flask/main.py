# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os

def print_hi(name):
    strPub = ''
    with open(os.path.expanduser("~/Documents/develop/web_flask/app/pubdata_flask.json")) as file:
        data = json.load(file)
    for i in data["x"]:
        test = i["name"]
        strPub = strPub + ', ' + test
    print(strPub)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
