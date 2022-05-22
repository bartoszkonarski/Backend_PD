from flask import (
    Flask, 
    render_template,
    request,
    Response
)
import json
from statistics import get_drivers_standings, get_teams_standings
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
        return render_template("base.html")

@app.route("/standing", methods=["POST"])
def standing():
    request_data = request.get_json()
    standing_type = request_data['standing_type']
    season = request_data['season']
    if standing_type == "drivers":
        return Response(json.dumps(get_drivers_standings(season)),  mimetype='application/json')
    else:
        return Response(json.dumps(get_teams_standings(season)),  mimetype='application/json')

if __name__ == "__main__":
    app.run()