from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 需求：路径参数传递多信息并以一个参数接收。
# 比如：获取姓名：zs 年龄 18的信息
# /user/zs+18


class LiConverter(BaseConverter):
    # override this method
    # to_python 方法是用于处理从 URL 中提取的值，并将其转换为 Python 对象。
    # 这个方法将在 Flask 处理 URL 时被调用。
    # return value.split('+') 这行代码是 to_python 方法的实现。
    # 它接受一个名为 value 的参数，并将其以 '+' 字符为分隔符进行分割，然后返回一个字符串列表。
    def to_python(self, value):
        return value.split('+')


app.url_map.converters['li'] = LiConverter


@app.route('/')
def index():
    return "Hello"


@app.route('/user/<info>')
def user(info):
    args = info.split('+')
    # sql  : select * from t_user where uname = args[0] and age = args[1];
    return f'获取了某某信息！！{args}'


@app.route('/user_info/<li:info>')
def user_info(info):
    # sql  : select * from t_user where uname = args[0] and age = args[1];
    return f'获取了某某信息！！{info}'


if __name__ == '__main__':
    app.run(debug=True)
