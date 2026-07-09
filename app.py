from flask import Flask, jsonify, render_template
from monitor import get_metrics
from database import get_all_metrics, save_metrics

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

    return jsonify(data)

@app.route("/history")
def history():
    return jsonify(get_all_metrics())

if __name__ == "__main__":
    app.run(debug=True)