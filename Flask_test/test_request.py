from flask import Flask

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    print('before_first_request')

@app.before_request
def before_request(id):
    if id > 1:
        print('before_request_successful')
        return 'before_request_successful'
    else:
        print('before_request_failed')
        return 'before_request_failed'

@app.route('/')
def index():
    return 'selfindex open successful'


@app.after_request
def after_request(response):
    print("after_request")
    response.headers["Content-Type"] = "application/json"
    return response

@app.teardown_request
def teardown_request():
    return 'teardown_request'

if __name__ == '__main__':

    app.run(debug=True)






