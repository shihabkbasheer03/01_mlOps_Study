from flask import Flask
"""
It creates an instance of the flask class, 
Which will be WSGI application
"""
### WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask course. This should be an amazing cource "

if __name__=="__main__":
    app.run(debug=True)
