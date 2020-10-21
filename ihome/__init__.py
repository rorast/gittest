# coding: utf-8

from flask import flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy


# 資料庫
db = SQLAlchemy()

# 官方在配置設定檔上，建議使用 "工廠模式"
def create_app(config_name):
    """
    創建flask的應用對象
    :param config_name: str 配置模式的名字 ("develop", "product")
    :return:
    """
    app = Flask(__name__)

    # 根據配置模式的名字獲取配置參數的類
    config_class = config_map.get(config_name) 
    app.config.from_object(config_class)

    # 使用app初始化db
    db.init_app(app)

    return app