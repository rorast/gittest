# coding:utf-8


from flask import flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect


app = Flask(__name__)

class Config(object):
    """配置信息"""
    DEBUG = True

    SECRET_KEY = "Xdfsk3902ldD#$**())_"

    # 資料庫
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/test_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask-session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 對cookie中session_id進行隱藏處理
    PERMANENT_SESSION_LIFETIME = 86400  # session數據的有效期，單位秒

app.conifg.from_object(Config)

# 資料庫
db = SQLAlchemy(app)

# 創建redis連接對象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST ,port=Config.REDIS_PORT)

# 利用flask-session，將session數據保存到redis中
Session(app)

# 為flask補充csrf防護
CSRFProtect(app)


@app.route("/index")
def index():
    return "index page"    

if __name__ == '__main__':    
    app.run()            