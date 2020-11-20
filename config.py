# coding:utf-8

import redis

class Config(object):
    """配置信息"""
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 6666

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


class DevelopmentConfig(Config):
    """開發模式的配置信息"""
    DEBUG = True


class ProductConfig(Config):
    """生產環境配置信息"""
    pass


# 名字與類的映射關係()
config_map = {
    "develop": DevelopmentConfig,
    "product": ProductConfig
}