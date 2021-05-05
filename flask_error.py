from flask import Flask
import requests
import logging

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404 Error</h1>", 404

@app.route("/google")
def get_google():
    res = requests.get('http://www.google.co.kr')
    return res.text

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")