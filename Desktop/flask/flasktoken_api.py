#./anaconda3/lib/python3.6/site-packages (1.2.15)
from flask import Flask,request,jsonify#import objects from the flask model
app=Flask(__name__)#define app in flask
languages=[{"name":"python"},{"name":"javascript"},{"name":"java"}]

@app.route("/", methods=["GET"])
def hello():
	return jsonify({"message":"it works"})

@app.route("/lang",methods=["GET"])
def returnall():
	return jsonify({"languages":languages})

@app.route("/lang/<string:name>",methods=["GET"])
def returnone(name):
	langs=[language for language in languages if language["name"]==name]
	return jsonify({"language":langs[0]})

@app.route('/lang', methods=['POST'])
def addone():
	language = {"name" :request.json["name"]}
	languages.append(language)
	return jsonify({"languages":languages})

@app.route("/lang/<string:name>",methods=["PUT"])
def editone(name):
	langs=[language for language in languages if language["name"]==name]
	langs[0]["name"]=request.json["name"]
	return jsonify({"languages":langs[0]})

@app.route("/lang/<string:name>",methods=["DELETE"])
def removeone(name):
	langs=[language for language in languages if language["name"]==name]
	languages.remove(langs[0])
	return jsonify({"languages":languages})


if __name__ == '__main__':
	app.run(debug=True,port=8080)#run app on port 8080 in debug mode
