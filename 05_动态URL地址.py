from flask import Flask

app = Flask(__name__)


@app.route('/article/details/86714886')
def index1():
    return '/article/details/86714886'


@app.route('/article/details/103582822')
def index2():
    return '/article/details/103582822'


@app.route('/article/details/<id>')
def index(id):
    print(f'接收到的文章ID是：{id}')
    # 获取到ID后，去数据库查询数据

    return f'返回了，{id}的文章'


if __name__ == '__main__':
    app.run()
