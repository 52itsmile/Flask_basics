from flask_sqlalchemy import SQLAlchemy
from flask import Flask



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    us = db.relationship('User', backref='role')
    # print(us)

    # repr()方法显示一个可读字符串
    def __repr__(self):

        return 'Role:%s' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:%s' % self.name

@app.route('/')
def index():
    return 'index'



class Config(object):
    DEBUG = True
app.config.from_object(Config)

if __name__ == "__main__":
    db.drop_all()
    db.create_all()

    ro1 = Role(name='admin')
    db.session.add(ro1)
    db.session.commit()
    # 再次插入一条数据
    ro2 = Role(name='user')
    db.session.add(ro2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
    us5 = User(name='tang', email='tang@itheima.com', password='158104', role_id=ro2.id)
    us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
    us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
    us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
    us9 = User(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
    us10 = User(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
    db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    db.session.commit()
    """
    查询所有用户数据
    User.query.all()
    查询有多少个用户
    User.query.count()
    查询第1个用户
    User.query.first()
    查询id为4的用户[3种方式]
    User.query.get(4)
    User.query.filter_by(id=4).first()  
    User.query.filter(User.id==4).first()  
    查询名字结尾字符为g的所有数据[开始/包含]
    User.query.filter(User.name.endswith('g')).all() 
    查询名字不等于wang的所有数据[2种方式]
    User.query.filter(not_(User.name=='wang')).all() 
    User.query.filter(User.name != 'wang').all()   
    查询名字和邮箱都以 li 开头的所有数据[2种方式]
    User.query.filter(User.name.startswith('li'),User.email.startswith('li')).all()  
    User.query.filter(and_(User.name.startswith('li'),User.email.startswith('li'))).all() 
    查询password是 `123456` 或者 `email` 以 `itheima.com` 结尾的所有数据
    User.query.filter(or_(User.password =='123456',User.email.endswith('itheima.com'))).all() 
    查询id为 [1, 3, 5, 7, 9] 的用户列表
    
    查询name为liu的角色数据
    User.query.filter(User.name == 'liu').first().role
    查询所有用户数据，并以邮箱排序
    User.query.order_by(User.email.desc()).all()
    每页3个，查询第2页的数据
    
    """



    app.run()