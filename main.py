from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method=="POST":
        print(request.form["type"])
        return render_template("drivers.html", standing_type=request.form["type"])
    return render_template("drivers.html")
if __name__ == "__main__":
    app.run()