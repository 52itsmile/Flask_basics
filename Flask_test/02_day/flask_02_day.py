from flask import Flask
from werkzeug.routing import BaseConverter
from flask import abort


class RegexConverter(BaseConverter):
    # 自定义正则转换器
    # regex = "[0-9]{6}"
    def __init__(self,url_map,*args):
        super(RegexConverter,self).__init__(url_map)
        # 取到第一个参数,给regex属性取值
        self.regex = args[0]
app = Flask(__name__)

# 将自己的转换器添加到默认的转换器列表中
app.url_map.converters["re"] = RegexConverter
@app.route('/')
def index():
    return 'index'
@app.route('/user/<re("[0-9]{6}"):user_id>')
def demo1(user_id):
    return "用户id是%s"%user_id
# @app.route('/user/<re:userid>'):
# def demo1(userid):
#     return userid

@app.route('/demo2')
def demo2():
    # 主动抛出http指定错误状态码
    # abort(404)
    a = 0
    b = 1/a
    return 'demo1'

# 使用装饰器的形式去捕获指定错误码和异常
# 可以自定义异常跳转页面
@app.errorhandler(404)
def page_not_found(error):
    return '页面不见了'

@app.errorhandler(ZeroDivisionError)
def zero_division_error(error):
    return '除数不能为0'

if __name__ == '__main__':
    app.run(debug=True)