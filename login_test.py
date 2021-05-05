from flask import Flask, request, render_template, jsonify
app = Flask(__name__, static_url_path='/static')

@app.route('/login')
def login():
    email_info = request.args.get('email_info')
    passwd = request.args.get('pw')
    print(email_info, passwd)
    if email_info == "bbcc8417@naver.com" and passwd == "111":
        return_data = {'auth':'success'}
    else:
        return_data = {'auth':'failed'}
    return jsonify(return_data)


@app.route('/html_test')
def html_test():
    return render_template('login_site.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")