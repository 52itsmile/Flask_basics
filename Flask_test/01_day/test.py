from flask import Flask
from flask import request
from flask import make_response
from flask import session
from flask import abort
from werkzeug.routing import BaseConverter




app = Flask(__name__)
app.secret_key = 'sdfsdfsdfsdf'

# 自定义正则转换器
class RegexConverter(BaseConverter):
    def __init__(self,url_map,*args):
        super(RegexConverter, self).__init__(url_map)
        self.regex = args[0]
    def to_python(self, value):
        print('=====to_python=====')
        int(value)
        return type(value)
    def to_url(self, value):
        print('=====to_url=====')
        print(type(value))
        return value
app.url_map.converters['re'] = RegexConverter



# 添加获取删除cookie
@app.route('/<re("[0-9]{2}"):logid>')
def index(logid):
    # userid = request.cookies.get('user_id')
    # username = request.cookies.get('user_name')
    # return 'userid=%s,username=%s'%(userid,username)
    return str(logid)

@app.route('/login')
def login_cookie():
    response = make_response('login successful')
    response.set_cookie('user_id','1')
    response.set_cookie('user_name','wwwwww')

    return response

@app.route('/logout')
def logout_cookie():
    response = make_response('logut successful')
    response.delete_cookie('user_id')
    response.delete_cookie('user_name')
    return response


# 添加获取删除
@app.route('/ls')
def index1():
    userid = session.get('userid')
    username = session.get('username')
    return 'userid:%s,username:%s' %(userid,username)
    # return 'success'

@app.route('/login_session')
def login_session():
    session['username']= 'wangdana'
    session['userid']= '12345'
    return 'login_session add successful'


@app.route('/logout_session')
def logout_session():
    session.pop('userid')
    session.pop('username')
    return 'logout_session delete successful'


@app.before_first_request
def test_before_first_request():
    print('before_first_request')
    # return 'before_first_request  successful'

@app.before_request
def test_before_request():
    print('before_request')
    name = session.get('username')
    print(name)
    # return 'before_request  %s successful'%name


@app.route('/error')
def error_html():
    # 直接抛出异常
    abort(500)
    return 'error'
# 出现异常跳转异常页面
@app.errorhandler(500)
def error_index_html(error):
    return '页面不见了'


class Config(object):
    DEBUG = True

app.config.from_object(Config)
if __name__ == '__main__':
    app.run()