from flask import Flask, render_template

"""
It creates an instance of the Flask class, 
Which will be the WSGI application
"""

### WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to this Flask course. This should be an amazing course </H1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
