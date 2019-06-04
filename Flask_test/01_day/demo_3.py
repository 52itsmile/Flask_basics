from flask import Flask
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__,
            static_url_path='/a',
            static_folder='static',
            template_folder='template')


@app.route('/')
def demo1():
    return 'successful'


@app.route('/a')
def demo2():
    return 'demo2====>succeseful'

@app.route('/abc/<user_id>')
def demo3(user_id):
    return user_id
@app.route('/demo6')
def demo6():
    return redirect(url_for('demo2'))
@app.route('/demo7')
def demo7():
    return 'demo7',200,{'Content-Type':'test'}
@app.route('/demo8',methods=["GET","POST"])
def demo8():
    return request.method

@app.route('/demo9/<user1>/<user2>/<user3>',methods=["GET"])
def demo9(user1,user2,user3):
    print(user1,user2,user3)
    # return user1+'/'+user2+'/'+user3
    return '%s%s%s'% (user1,user2,user3)



# class Config(object):
#     DEBUG = True
#
# app.config.from_object(Config)
if __name__ == '__main__':
    print(app.url_map)
    app.run(host='localhost',port=8888,debug=True)