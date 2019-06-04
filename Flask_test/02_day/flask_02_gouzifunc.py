from flask import Flask

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    """在第一次请求之前会访问该函数"""
    print('before_first_request')

@app.before_request
def before_request():
    """在每次请求之前都会调用"""
    print('before_first_request')
    #可以对一些非法的请求进行阻止
    # 如果ip在黑名单
    # 返回  '你在~~~'

@app.after_request
def after_request(response):
    # 在请求之后会调用,并且函数里面接受一个参数,:响应,还需要讲响应进行返回
    print('after_request')
    return response

@app.teardown_request
def teardown_request(error):
    # 在请求之后会执行,如果在响应中出现异常,会把具体的异常传入到此函数
    print('teardown_request')
    print(error)

@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run()