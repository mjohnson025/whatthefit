from flask import Flask, url_for
from flask import render_template
from module.dbhelper import DBhelper

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/tracker')
def tracker():
	helper = DBhelper()
	exerciseLkupTable = helper.getExerciseLookup()
	return render_template('tracker.html', exerciseLkupTable=exerciseLkupTable)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
