from flask import Flask

app = Flask(__name__)


@app.route('/article/<id>')
def index(id):
    print(f'接收到的文章ID是：{id}')
    print(type(id))
    return f'返回了，{id}的文章'


@app.route('/int/<int:id>')
def index_int(id):
    print(f'接收到的文章ID是：{id}')
    print(type(id))
    return f'返回了，{id}的文章'


@app.route('/float/<float:id>')
def index_float(id):
    print(f'接收到的文章ID是：{id}')
    print(type(id))
    return f'返回了，{id}的文章'


@app.route('/str/<string:id>')
def index_str(id):
    print(f'接收到的文章ID是：{id}')
    print(type(id))
    return f'返回了，{id}的文章'


@app.route('/path/<path:id>')
def index_path(id):
    print(f'接收到的文章ID是：{id}')
    print(type(id))
    return f'返回了，{id}的文章'


@app.route('/uuid/<uuid:id>')
def index_uuid(id):
    print(f'接收到的文章ID是：{id}')
    print(type(id))
    return f'返回了，{id}的文章'


@app.route('/<any(user,item):tmp>/<int:id>')
def index_any(tmp, id):
    if tmp == 'user':
        return f'返回了一个编号为 {id} 的 用户 信息'
    elif tmp == 'item':
        return f'返回了一个编号为 {id} 的 元素 信息'


from werkzeug.routing import BaseConverter

# user/[1,2,3]
# item/[1,2,3]
# vip/[1,2,3]
if __name__ == '__main__':
    app.run(debug=True)
