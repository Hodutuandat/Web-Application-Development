from flask import Flask, render_template, request, redirect, url_for 
from pymongo import MongoClient

app = Flask (__name__)

client = MongoClient ("mongodb://localhost:27017/")
db = client ["student_db"]
collection = db["students"]


#Display the student list
@app.route("/")
def index():
    students = list(collection.find())
    return render_template("index.html", students=students)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        major = request.form["major"]
        collection.insert_one({"name": name, "age": age, "major": major})
        return redirect(url_for("index"))
    return render_template("form.html", student=None)

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    student = collection.find_one({"_id": id})
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        major = request.form["major"]
        collection.update_one({"_id": id(id)}, {"$set": {"name": name, "age": age, "major": major}})
        return redirect(url_for("index"))
    return render_template("form.html", student=student)

@app.route("/delete/<id>")
def delete(id):
    collection.delete_one({"_id": id})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
