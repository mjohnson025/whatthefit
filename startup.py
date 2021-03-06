from flask import Flask, url_for, request, make_response
from flask import render_template
from module.dbhelper import DBhelper
import json


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/tracker')
def tracker():
	helper = DBhelper()
	try:
		exerciseLkupTable = helper.getExerciseLookup()
		return render_template('tracker.html', exerciseLkupTable=exerciseLkupTable)
	except Exception as e:
		exerciseLkupTable=[1,1,2,3,4]
		return render_template('tracker.html', exerciseLkupTable=json.dumps(exerciseLkupTable))

@app.route('/update')
def update():
	return render_template('update.html')

@app.route('/tables')
def tables():
	helper = DBhelper()
	try:
		workouts = helper.getWorkout()
		return render_template('tables.html', workouts=workouts)
	except Exception as e:
		raise e


#API
@app.route('/api/insertIntoWorkoutTable')
def insertIntoWorkoutTable():
	exerciseId = request.args.get('exerciseid')
	exerciseCount = request.args.get('exercisecount')

	helper = DBhelper()
	try:
		helper.insertWorkout('default',exerciseId, exerciseCount)
		return make_response("Call Success",200)
	except Exception as e:
		return make_response("Bad Request", 400)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
