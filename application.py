from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello, this is Nomad Cycling Club Web Site running on Azure web services!"