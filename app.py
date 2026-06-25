from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods = ("GET", "POST"))
def index():
    time, name = None 
    if request.method == "POST":
        name = request.form["Name"]
        dob = request.form["DOB"]
        gender = request.form["Gender"]
        time = "7 Hours"
    return render_template("index.html", time = time, name = name)

if __name__ == "__main__":
    app.run(debug = True)
    