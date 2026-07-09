from flask import Flask, jsonify, render_template
from monitor import get_metrics
from database import (
    get_all_metrics,
    save_metrics,
    create_incident,
    get_incidents
)

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/metrics")
def metrics():

    data = get_metrics()

    save_metrics(
        data["cpu"],
        data["memory"],
        data["disk"]
    )

    # Incident Detection

    if data["cpu"] > 80:
        create_incident("High CPU Usage")

    if data["memory"] > 90:
        create_incident("High Memory Usage")

    if data["disk"] > 90:
        create_incident("Disk Almost Full")

    return jsonify(data)


@app.route("/history")
def history():
    return jsonify(get_all_metrics())


@app.route("/incidents")
def incidents():
    return jsonify(get_incidents())


if __name__ == "__main__":
    app.run(debug=True)