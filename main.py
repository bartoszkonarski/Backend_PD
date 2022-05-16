from flask import (
    Flask, 
    render_template,
    request
)
from statistics import get_drivers_standings, get_teams_standings
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method=="POST":
        if request.form['type'] == "drivers":
            standing=get_drivers_standings(request.form['season'])
            return render_template("base.html", standing_type = "drivers", standing=standing)
        else:
            standing=get_teams_standings(request.form['season'])
            return render_template("base.html", standing_type = "teams", standing=standing)

    return render_template("base.html")
if __name__ == "__main__":
    app.run()