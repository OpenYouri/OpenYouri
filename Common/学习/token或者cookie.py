"""
通过登录接口获取到  token

把token放入header头里面，那么这样就能够登录成功了



cookie是登录后在 浏览器缓存中存在的，
所有如果你的项目是 cookie登录的
1. 登录
2. 请求


session
1. 登录---session
2. 请求---session
"""
"""渠道接口，查询手机列表"""
# import requests
#
# session=requests.Session()
# #登录
# res=session.post("http://192.168.25.40:7001/admin/login/login.html",{"username":"admin",'password':"admin888"})
# print(res.text)
#
# res=session.get('http://192.168.25.40:7001/admin/phone/getphoneList')
# print(res.text)

"""
怎么把 ini文件中的  块下面的所有项取出来

.items()
"""
from Test.Interface.Common.handle_config import conf

res=conf.items("headers")

headers={}
# print(res)
for i in res:
    headers.update({i[0]:i[1]})

print(headers)