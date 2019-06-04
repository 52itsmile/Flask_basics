from flask import Flask
from flask import session

app = Flask(__name__)
# 使用session的话,需要配置secret_key
app.config['SECRET_KEY'] = 'sdfsdfsdf'

@app.route('/')
def index():
    user_id = session['user_id']
    user_name = session['user_name']
    return '%s%s' % (user_id,user_name)

@app.route('/login')
def login():
    # 假装校验成功
    session['user_id'] = '1'
    session['user_name'] = 'laowang'
    return 'success'

@app.route('/logut')
def logut():
    # 假装校验成功
    session.pop('user_id')
    session.pop('user_name')
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)