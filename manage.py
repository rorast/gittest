# coding:utf-8


from flask_session import Session
from flask_wtf import CSRFProtect

import redis

from ihome import create_app


# 創建flask的應用對象
app = create_app("develop")



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