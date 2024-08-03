from flask import Blueprint,render_template,redirect,request
from .models import *



# 创建一个蓝图
blue = Blueprint("user",__name__)

# 定义路由及视图函数
# 首页
@blue.route("/")
@blue.route("/home/")
def home():    
    return render_template("index.html");

@blue.route("/get/",methods=['GET'])
def get():
    print(request.args)
    return dict(request.args)


@blue.route("/post/",methods=['POST'])
def post():
    print(request.form)
    return dict(request.form)

@blue.route("/postjson/",methods=['POST'])
def postjson():
    print(request.json)
    return {"status":200}



