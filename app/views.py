from flask import Blueprint,render_template,redirect,request
from .models import *



# 创建一个蓝图
blue = Blueprint("user",__name__)

# 定义路由及视图函数
# 首页
@blue.route("/home/")
def home():
    
    return ("hello flask")


