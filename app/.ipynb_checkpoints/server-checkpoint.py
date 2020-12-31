from flask import Flask
from flask import jsonify
from flask import request
import language_tool_python as ltp

# make a new flask app
app = Flask(__name__)

# make a new language tool locally
tool = ltp.LanguageTool('en-US')

# Base route
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : "Hello, World!"})

# Grammar Check route
@app.route('/check/<string:text>')
def check_grammar(text):
    corrected = tool.correct(text)
    return jsonify({'corrected' : corrected})
    
if __name__ == "__main__":
    app.run(debug=True)