from flask import Flask
from flask import request
import json
from flask import redirect
from flask import url_for
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/demo1')
def demo1():
    return 'demo1'
# 给路由添加参数,格式就是<参数名>
# 并且视图函数需要接受这个参数
@app.route('/demo2/<int:user_id>')
def demo2(user_id):
    return 'demo2 %s' % user_id

@app.route('/demo3',methods=['GET','POST'])
def demo3():
    return 'demo3 %s' % request.method

@app.route('/json')
def demo4():
    json_dict = {
        "name":"laowang",
        "age":18
    }
    # 使用json.dumps将字典转成JSON字符串
    result = json.dumps(json_dict)
    # 使用JSON.loads讲json字符串转成字典
    # test_dict = json.load('{"name":"laowang", "age":18 }')
    # return result
    # jsonify会指定相应内容的数据格式(告诉客户端我返回给你的数据格式是什么)
    return jsonify(json_dict)


@app.route('/redirect')
def demo5():
    # 重定向到自己写的视图函数
    # url_for:取到指定视图函数所对应的路由URL,并且可以携带参数
    # url_for,后面参数写函数名
    return redirect(url_for('index'))

# 重定向自定义状态码
@app.route('/demo6')
def demo6():
    # 三个参数  第一个参数自定义信息  第二个错误代码  第三个更改响应体信息里字典模式
    return 'demo6',404

app.config['DEBUG'] = True
if __name__ == '__main__':
    print(app.url_map)
    app.run()