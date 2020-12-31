import language_tool_python as ltp
from flask import Flask, render_template, request, url_for

tool = ltp.LanguageTool('en-US')
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def main_get(num=None):
    return render_template('submit_test.html', num=num)

@app.route('/result', methods=['POST', 'GET'])
def calculate(num=None):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        inputText = request.args.get('char1')
        corrected = tool.correct(inputText)

        return render_template('submit_test.html', text=inputText, result=corrected)

if __name__ == '__main__':
  app.run(debug=True, threaded=True)
