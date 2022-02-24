from flask import Flask, render_template, request
from fishel import date_fix

app = Flask(__name__)

WORKOUTS = []
EXERCISES = [
  'Lunges', 'Pushups','Burpees', 'Crunches', 'Side Planks', 'Squats', 'Planks', 'Mountain Climbers', 'Reverse Crunches', 'Knee to Elbow Crunches'
]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/exercise", methods=["GET","POST"])
def exercise():
  # grab the first name from the form
  
  f_name = request.form.get('first')
  if not f_name:
    return render_template("error.html", message="You must resister befor you can log workouts!")
  return render_template("exercise.html", first_name=f_name, exercise_list=EXERCISES)

@app.route("/add", methods=["GET","POST"])
def add():
  if request.method == "POST": #accessed from the form
    # grab the info from the form
    ex_date = date_fix(request.form.get('date'))
    exercise = request.form.get('exercise')
    if exercise not in EXERCISES:
      return render_template("error.html", message="Please select a valid exercise from the list!")
    reps = request.form.get('reps')
    WORKOUTS.append({
      'ex_date': ex_date,
      'exercise': exercise,
      'reps':reps
    })
  return render_template("add.html", workout_list = WORKOUTS)

if __name__ == "__main__":
  app.run("0.0.0.0")
