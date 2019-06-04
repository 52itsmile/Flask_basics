from flask import Flask
# 请求上下文中的变量
from flask import request
from flask import session
# 应用上下文的变量
from flask import current_app
from flask import g

app = Flask(__name__)

# print(session.get('user_id',''))

@app.route('/')
def index():
    print(request.method)
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)