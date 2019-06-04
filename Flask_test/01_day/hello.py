# 导入Flask
from flask import Flask
# 创建flask应用程序
# 第一个参数:模块名称,1.指定模块的绝对路径2.在相应的路径下去找对应的静态文件和模板文件
app = Flask(__name__,
            # 访问静态文件的路径(1.0.0版本的时候弃用了)
            static_path='/static',
            # 静态文件访问的路径,如果制定为none,系统默认文件的访问路径为/static
            static_url_path='/static',
            # 指定静态文件夹的名字
            static_folder='static',
            # 指定模板文件夹的名字
            template_folder='template')
# 使用装饰器路由与师徒函数进行关联
@app.route('/')
def index():
    return 'hhhhh'

if __name__ == '__main__':
    # 运行当前Flask应用程序
    app.run()