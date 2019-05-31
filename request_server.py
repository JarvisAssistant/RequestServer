#!flask/bin/python
from flask import Flask, request, abort, jsonify
import imp
import os

import commands

app = Flask(__name__)

@app.route('/intent', methods=['PUT'])
def intent():
	print(request.get_json())
	if not request.json or not 'intent' in request.json:
		abort(400)
	
	answer = handle_intent(request.json)
	
	return jsonify(answer)

def handle_intent(data):
	intent = data['intent']

	if not hasattr(commands, intent):
		return { "error" : "no such intent named \"%s\"" % (data['intent']) }

	parameters = data.get("parameters", [])

	return run_command(intent, parameters)

def run_command(intent, parameters):
	return getattr(commands, intent)(*parameters)

if __name__ == "__main__":
	app.run(debug=True)

