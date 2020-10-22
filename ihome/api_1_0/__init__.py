# coding:utf-8

frmo flask import Blueprint

# 創建藍圖對象
api = Blueprint("api_1_0", __name__)


# 導入藍圖的視圖
from . import demo