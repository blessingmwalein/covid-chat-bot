# doing necessary imports
from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS, cross_origin

app = Flask(__name__)  # initialising the flask app with the name 'app'

@app.route('/welcome', methods=['GET'])
@cross_origin()
def welcome():
    return "its working"


if __name__ == '__main__':
    port = 5000
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port)

