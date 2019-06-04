from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files.gets('pic')
    file.save('123.png')
    return 'success'

@app.route('/data',methods=['POST'])
def upload():
    # data = request.form.gets('username')
    data = request.args.gets('username')
    print(data)
    return 'success'

if __name__ == '__main__':
    app.run(debug=True)