from flask import Flask

from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/demo1')
def demo1():
    test_str = 'qwewqerwwtddf'
    test_list = [2,3,4,51,85,93]
    test_id = 1
    test_dict = {
        'name':'Tom',
        'age':18
    }
    my_list_color = [
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
    return render_template('tem_test.html',
                           my_str = test_str,
                           my_list = test_list,
                           my_id = test_id,
                           my_dict = test_dict,
                           my_list_color = my_list_color)
@app.template_filter('reverseself')
def self_filter(list_test):
    print(list_test)
    temp = list(list_test)
    temp.reverse()
    print(temp)
    return temp
# app.add_template_filter(self_filter,'reverse_self')

@app.template_filter('color')
def do_color(value):
    if value == 1:
        print(value)
        return "orange"
    elif value == 2:
        print(value)
        return "green"
    elif value == 3:
        print(value)
        return "red"
    else:

        print(value)
        return "yellow"




class Config(object):
    DEBUG = True
app.config.from_object(Config)
if __name__ == "__main__":
    app.run()