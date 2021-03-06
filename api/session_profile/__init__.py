# @Time    : 2020/11/21 11:18 下午
# @Author  : h0rs3fa11
# @FileName: __init__.py.py
# @Software: PyCharm

from flask import Blueprint
from flask_restful import Api
from api.session_profile.views import InfoView, AvatarView, PasswordView

sprofile_blu = Blueprint('profile', __name__, url_prefix='/session_profile')

api = Api(sprofile_blu)

api.add_resource(InfoView, '/info')
api.add_resource(PasswordView, '/password')
api.add_resource(AvatarView, '/avatar')
