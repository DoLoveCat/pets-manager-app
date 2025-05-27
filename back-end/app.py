# be the entry point of the application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
# 创建 Flask 应用实例，__name__ 表示当前模块名
CORS(app)
# 启用跨域支持，解决前后端不在同一个端口时浏览器阻止访问的问题

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///pets.db"
# 配置数据库连接，这里使用 SQLite，数据库文件为 pets.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 关闭对对象修改的追踪功能，节省资源，通常设为 False

db = SQLAlchemy(app)
# 创建 SQLAlchemy 数据库操作对象，后续可以用它定义表、操作数据

import routes
#since we dont return anything from routes.py
from routes import *

with app.app_context():
    db.create_all()
#准备操作数据库，把当前这个 app 的配置环境打开使用
#也就是上下文操作


if __name__ == '__main__':
    app.run(debug=True)
# 启动 Flask 开发服务器，debug=True 表示开启调试模式（开发阶段使用）