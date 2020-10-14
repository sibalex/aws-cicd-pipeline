from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")
def root():
    return render_template("index.html")

@application.route("/help")
def helppage():
    return render_template("help.html")

@application.route("/hello")
def index():
    return "Hello World from Flask Hello Page.<b> v1.0"


if __name__ == "__main__":
    application.run(debug=True)
    
