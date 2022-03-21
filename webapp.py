from flask import Flask, render_template, request
from sort import sort_routes
from moonboard import Display
import json
import ast

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/problem/", methods=["POST", "GET"])
def problem():
    if request.method == "GET":
        return "bruh"
    if request.method == "POST":
        grade = request.form["Grade"]
        sort = request.form["sort"]
        problem_list = sort_routes(grade, sort)
        return render_template("problem.html", problem_list=problem_list)

@app.route("/setproblem/", methods=["POST"])
def setproblem():
    # hold function here
    problem_json = json.loads(json.dumps(ast.literal_eval(request.form['problem'])))
    display.displayProblem(problem_json)
    return render_template("problem.html")

display = Display()
app.run()