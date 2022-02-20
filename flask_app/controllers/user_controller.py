from flask import render_template,request, redirect, session
from flask_app import app
from flask_app.models.survey import Survey

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/form", methods=["POST"])
def form():
    if Survey.is_valid(request.form):
        Survey.save(request.form)
        
        return redirect("second")
    return redirect("/")


@app.route("/second")
def second():
    return render_template("second.html") 
    






