from flask import Flask
from .views import blue

# 定义创建主APP的函数

def create_app():
    app = Flask(__name__) # 创建flask实例
    app.register_blueprint(blue) # 绑定蓝图        
    return app