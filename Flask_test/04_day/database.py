from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:mysql@127.0.0.1:3306/python_test"
# 是否追踪数据库的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 查询时会显示原生SQL语句
app.config['SQLALCHEMY_ECHO'] = True
# 初始化SQL对象
db = SQLAlchemy(app)

class Role(db.Model):
    # 指定该模型对应数据库中的表明,如果不指定为类名小写
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),unique=True)


    def __repr__(self):
        return 'Role %d %s' %(self.id,self.name)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 添加外键
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))


    def __repr__(self):
        return 'Role %d %s' % (self.id, self.name)



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
    ro2 = Role(name='user')
    db.session.add_all([ro1,ro2])
    db.session.commit()

    user1 = User(name='laowang',role_id = ro1.id)
    user2 = User(name='laozhao',role_id = ro1.id)
    user3 = User(name='xiaoli',role_id = ro2.id)

    db.session.add_all([user1,user2,user3])
    db.session.commit()

    app.run()