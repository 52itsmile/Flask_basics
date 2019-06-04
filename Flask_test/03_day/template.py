from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/demo1')
def demo1():
    my_name = 'wwww'
    my_str = '<script>for (var i;i<=3;i++){alert("哈哈")}</script>'
    my_list = [1, 2, 3, 4]
    my_dict = {'name':'laowang',
               'age':18}
    my_dict_list = [
        {
            'good_name':"大白菜",
            'price':10
        },
        {
            'price':20
        }
    ]

    return render_template('template.html',
                           my_name = my_name,
                           my_dict = my_dict,
                           my_list = my_list,
                           my_str = my_str,
                           my_dict_list = my_dict_list)
# 方式1:使用装饰器添加
@app.template_filter('lireverse')
def do_lireverse(li):
    temp = list(li)
    temp.reverse()
    return  temp
# 方式2:直接添加过滤器
app.add_template_filter(do_lireverse,'lireverse')

@app.route('/demo2')
def demo2():
    my_list1 = [
        {
            "id": 1,
            "value": "我爱工作"
        },
        {
            "id": 2,
            "value": "工作使人快乐"
        },
        {
            "id": 3,
            "value": "沉迷于工作无法自拔"
        },
        {
            "id": 4,
            "value": "日渐消瘦"
        },
        {
            "id": 5,
            "value": "以梦为马，越骑越傻"
        }
    ]
# @app.route('/demo3')
# def demo3():
#     return render_template('template.html')

if __name__ == "__main__":
    app.run(debug=True)