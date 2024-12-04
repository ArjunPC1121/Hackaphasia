from flask import Flask, render_template, Response, url_for
import pandas as pd
from utilities.quiz import recommend_by_difficulty

app = Flask(__name__)

data = pd.read_csv("coursea_data.csv")
data.drop_duplicates(inplace=True)
data['course_difficulty'] = data['course_difficulty'].fillna('Beginner')  # Default to Beginner
data['course_difficulty'] = data['course_difficulty'].str.capitalize()

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/quizzes")
def quiz():
    recommended_courses = recommend_by_difficulty(data, 'Beginner')
    print(recommended_courses.to_dict(orient='records'))  # Debugging step
    return render_template("quiz.html", recommended_courses=recommended_courses.to_dict(orient='records'))

@app.route("/options")
def options():
    return render_template("options.html")

if __name__ == "__main__":
    app.run(debug=True)
