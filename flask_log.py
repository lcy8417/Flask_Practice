from flask import Flask
import requests

app = Flask(__name__)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler # logging 핸들러 이름을 적어줌
    file_handler = RotatingFileHandler(
        'dave_server.log', maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

@app.errorhandler(404)
def page_not_fount(error):
    app.logger.error('dd')
    return "<h1>404 Error</h1>", 404

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=False)