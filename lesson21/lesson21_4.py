from flask import Flask

app = Flask(__name__) # 初始化Flask應用

@app.route("/") # 根路由
def index(): # 當訪問根路由時，返回這個頁面
    # 返回一個HTML標題
    return "<h1>您好, 全世界!</h1>"

@app.route("/name") # 新增一個路由
def name(): # 當訪問/name時，返回這個頁面
    # 返回一個HTML標題
    return "<h1>您好, 這是name的頁面!</h1>"