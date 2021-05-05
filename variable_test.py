from flask import Flask, template_rendered
app = Flask(__name__)

app.route('hello/<user>')
def hello(user):
    return template_rendered('variable.html', name1 = user, name2=2)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")