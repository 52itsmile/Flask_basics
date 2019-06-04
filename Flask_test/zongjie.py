from flask import  Flask
from flask import redirect,url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired
# 创建app实例
app = Flask(__name__)
app.secret_key = 'sdfsdfsdfsd'

# @app.before_first_request
# def link_db():
#
#     pass

# 链接数据库
# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 创建数据库实例
db = SQLAlchemy(app)

# 创建User表结构
class User(db.Model):
    username = db.Column(db.String(32),primary_key=True)
    password = db.Column(db.Integer,unique=True)

# 使用wtfFORM设置插入表单
class Insertform(FlaskForm):
    user_na = StringField('用户:',validators=[InputRequired('请输入用户')])
    pass_wd = IntegerField('密码:',validators=[InputRequired('请输入密码')])
    submit = SubmitField('添加')
# 主页
@app.route('/')
def index():
    # return 'index'
    # 重定向到login
    return redirect(url_for('login'))
# 设置登录页面路由
@app.route('/login',methods=['POST','GET'])
def login():
    # 获取表单信息
    add_user = Insertform()
    # user_name = request.form.get('username')
    # pass_word = request.form.get('password')
    # 判断用户是否提交成功
    if add_user.validate_on_submit():
        # 获取input框内的内容
        user_name = add_user.user_na.data
        pass_word = add_user.pass_wd.data
        print(user_name,pass_word)
        try:
            usernow = User.query.filter(User.username == user_name).first()
        except Exception as error:
            flash('查询错误,参数不正确')
            flash(error)
            return 'select error'
        else:
            if usernow:
                flash('已存在请勿重复添加')

            else:
                try:
                    user = User(username=user_name,password=pass_word)
                    db.session.add(user)
                    db.session.commit()
                except Exception as error:
                    db.session.rollback()
                    flash('添加失败')


    else:
        if request.method == 'POST':
            flash('参数错误')
    userinfo = User.query.all()

    return render_template('login.html',userinfo=userinfo,form=add_user)


@app.route('/delete/<get_username>')
def delete_user(get_username):
    try:
        deleteuser = User.query.filter(User.username == get_username).first()
        print(deleteuser)
        db.session.delete(deleteuser)
        db.session.commit()

    except Exception as error:
        db.session.rollback()
        print(error)
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    user1 = User(username='abc', password='123456')
    user2 = User(username='qwe', password='764246')
    user3 = User(username='tyu', password='343413')

    db.session.add_all([user1,user2,user3])
    db.session.commit()

    app.run(debug=True)