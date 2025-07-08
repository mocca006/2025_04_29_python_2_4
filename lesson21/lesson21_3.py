from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>您好, 全世界!</h1>"

# https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application

# To run the Flask application, use the command:
# flask run
# Make sure to set the FLASK_APP environment variable to the name of this file, e
# g., `export FLASK_APP=lesson21_3.py` on Unix or `set FLASK_APP=lesson21_3.py` on Windows.
# If you want to run it on a specific port, you can use:
# flask run --port 5000
if __name__ == "__main__":
    app.run(debug=True, port=5000)
# Note: The `debug=True` option enables debug mode, which is useful during development.
# In production, you would typically set this to `False` and use a production-ready server
