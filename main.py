from flask import Flask
from admin import admin
from public import public
from user import user

import demjson
from api import api

app=Flask(__name__)
app.secret_key="secretkey"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(user,url_prefix='/user')

app.register_blueprint(api,url_prefix='/api')


app.run(debug=True, port=5081, host="0.0.0.0")