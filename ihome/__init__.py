# coding: utf-8

import logging
from flask import flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_session import Session
from flask_wtf import CSRFProtect
from ihome import api_1_0  # 也可 from . import api_1_0
from logging.handlers import RotatingFileHandler

# 資料庫
db = SQLAlchemy()

# 創建redis連接對象
redis_store = None

logging.error("")  # 錯誤級別
logging.warn("")  # 警告級別
logging.info("")  # 消息提示級別
logging.debug("")  # 調試級別

# 設置日誌的記錄等級
logging.basicConfig(level=logging.DEBUG)  # 調試debug級
# 創建日誌記錄器，指明日誌保存的路徑、每個日誌文件的最大大小、保存的日誌文件個數上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 創建日誌記錄的格式                 日誌等級    輸入日誌信息文件名   行數     日誌信息 
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 為剛創建的日誌記錄器設置日誌記錄格式
file_log_handler.setFormatter(formatter)
# 為全局的日誌工具對象 (flask app使用的) 添加日記錄器
logging.getLogger().addHandler(file_log_handler)


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

    # 初始化 redis
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST ,port=config_class.REDIS_PORT)


    # 利用flask-session，將session數據保存到redis中
    Session(app)

    # 為flask補充csrf防護
    CSRFProtect(app)

    # 注冊藍圖
    from ihome import api_1_0 # 需要才導入，避免循環導入流程卡死
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")

    return app