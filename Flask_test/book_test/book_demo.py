from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
app = Flask(__name__)
app.secret_key = 'qwerwertre'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/python_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class AddBookForm(FlaskForm):
    author = StringField('作者:',validators=[InputRequired('请输入作者')])
    book = StringField('书名:',validators=[InputRequired('请输入书名')])
    submit = SubmitField('添加')

class Author(db.Model):
    # 一
    __tablename__ = 'author'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64), unique=True)
    books = db.relationship('Book', backref='author')

class Book(db.Model):
    # 多
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer,db.ForeignKey(Author.id))

@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    try:
        book = Book.query.get(book_id)
    except Exception as error:
        print(error)
        flash('查询错误')
    if not book:
        print('书籍不存在')
        flash('书籍不存在')
    else:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as error:
            print('错误')
            db.session.rollback()
            flash('删除失败')
    return redirect(url_for('index'))

@app.route('/delete_author/<author_id>')
def delete_author(author_id):
    try:
        author = Author.query.get(author_id)
    except Exception as error:
        flash('查询出错')
    if not author:
        return '查无此人'
    else:
        try:
            Book.query.filter(Book.author_id==author_id).delete()
            db.session.delete(author)
            db.session.commit()
        except Exception as error:
            flash('删除出现异常')
            return '删除错误'

    return redirect(url_for('index'))



# @app.route('/delete_author/<author_id>')
# def delete_author(author_id):
#     """删除作者以及作者所有的书籍"""
#
#     try:
#         author = Author.query.get(author_id)
#     except Exception as e:
#         print(e)
#         return "查询错误"
#
#     if not author:
#         return "作者不存在"
#
#     # 删除作者及其所有书籍
#
#     try:
#         # 先删除书籍
#         Book.query.filter(Book.author_id == author_id).delete()
#         # 再删除指定作者
#         db.session.delete(author)
#         db.session.commit()
#     except Exception as e:
#         print(e)
#         db.session.rollback()
#         return "删除失败"
#
#     return redirect(url_for('index'))




# @app.route('/delete_book/<book_id>')
# def delete_book(book_id):
#
#     try:
#         book = Book.query.get(book_id)
#     except Exception as error:
#         print(error)
#         return '查询错误'
#     if not book:
#         return "书籍不存在"
#
#     try:
#         db.session.delete(book)
#         db.session.commit()
#     except Exception as error:
#         print(error)
#         db.session.rollback()
#         return '删除失败'
#     return redirect(url_for('index'))



@app.route('/',methods=['POST','GET'])
def index():
    book_form = AddBookForm()

    if book_form.validate_on_submit():
        author_name = book_form.author.data
        book_name = book_form.book.data

        author = Author.query.filter(Author.name == author_name).first()
        book = Book.query.filter(Book.name == book_name).first()

        if author and not book:
            try:
                book = Book(name=book_name,author_id=author.id)
                db.session.add(book)
                db.session.commit()
            except Exception as error:
                db.session.rollback()
                print(error)
                flash('添加失败')
                return
        # 作者不存在,书不存在
        elif not author and not book:
            try:
                author = Author(name=author_name)
                db.session.add(author)
                db.session.commit()
                book = Book(name=book_name, author_id=author.id)
                db.session.add(book)
                db.session.commit()
            except Exception as error:
                db.session.rollback()
                print(error)
                flash('添加错误')
        else:
            print('重复添加')
            flash('重复添加')



        # 作者存在,书存在

        # 作者不存在,书存在

    else:
        if request.method == 'POST':
            flash('参数错误')


    # 判断book_form是否可以提交
    # 如果可以被提交执行逻辑处理
    # if book_form.validate_on_submit():
    #     author_name = book_form.author.data
    #     book_name = book_form.book.data
    # #     1.提交表单首先查询作者的名字
    #     author = Author.query.filter(Author.name == author_name).first()
    # #     判断作者名字是否存在
    #     if not author:
    # #     如果作者名字不存在
    # #       添加作者信息到数据库
    #         try:
    #             author = Author(name=author_name)
    #             db.session.add(author)
    #             db.session.commit()
    #             book = Book(name=book_name, author_id=author.id)
    #             db.session.add(book)
    #             db.session.commit()
    #         except Exception as error:
    #             db.session.rollback()
    #             print(error)
    #             flash('添加失败')
    #     else:
    #         book = Book.query.filter(Book.name == book_name).first()
    #         if not book:
    #             try:
    #         #     否则添加书籍到数据库(指定作者)
    #                 book = Book(name=book_name,author_id=author.id)
    #                 db.session.add(book)
    #                 db.session.commit()
    #             except Exception as error:
    #                 print(error)
    #                 flash("添加失败")
    #         else:
    #             flash('已经存在')
    # # 如果不能被提交则提示错误
    # else:
    #     if request.method == "POST":
    #         flash('错误')

    authors = Author.query.all()
    # 使用form表单
    # return render_template('base.html',authors=authors)
    # print(book_form)
    # 使用wtf表单
    return render_template('base_form.html',authors=authors, form=book_form)

class Config(object):
    DEBUG = True
app.config.from_object(Config)

if __name__ == "__main__":
    # db.drop_all()
    db.create_all()

    # au1 = Author(name='张三')
    # au2 = Author(name='王五')
    # au3 = Author(name='李四')
    # db.session.add_all([au1,au2,au3])
    # db.session.commit()
    #
    # bk1 = Book(name='asdfsd',author_id=au1.id)
    # bk2 = Book(name='sdfsdfbxvxc',author_id=au2.id)
    # bk3 = Book(name='cxfdgdh',author_id=au3.id)
    # db.session.add_all([bk1,bk2,bk3])
    # db.session.commit()


    app.run()