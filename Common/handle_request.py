from Test.Interface.Common.handle_data import EnvData
"""
通过传入的  url  请求方式（post，get）   请求数据   数据类型（json  非 json）
判断：post，get
    
json：
    json  包
    json 文件 
    
    
    json.load()  将json文件数据读取出来，变成字典类型
    json.dump()  将json数据写入文件
    
    字典   ------  json  
    json.loads()     json  类型  转化为  字典类型
    json.dumps()     字典类型   转化为   json
"""
import requests
import json
from Test.Interface.Common.handle_config import conf
from Test.Interface.Common.handle_logger import log
def send_request(url,method='post',data=None,json_type=True,login_status=None):
    """
    接口请求
    :param url: 完整的url +  协议 +域名 +路径
    :param method: get  或者  post  默认发生 post请求
    :param data: 请求数据---接口的入参
    :param json_type: 判断是否为json类型，，True 代表json类型（默认值） False代表 非json类型（采用传入的数据类型）
    :param headers  是否
    :return: 接口的返回值
    """
    #根据用例中的  路径   拼接成完成的  url
    url=__pre_url(url)
    #处理data（入参数据），把其中的  null转为 None,把字符串类型转为了  字典类型
    data=__pre_data(data)
    # 首字符转为大写后，变为 bool类型
    json_type=__pre_json_type(json_type)

    #headers  处理方式
    headers=__pre__headers(login_status)
    log.info('请求的url：{}'.format(url))
    log.info('请求的请求方法：{}'.format(method))
    log.info('请求的数据：{}'.format(data))
    log.info('请求的header：{}'.format(headers))
    if json_type:#如果  当前值为 True
        #数据转为json类型
        data=json.dumps(data)

    # 判断传入的 请求方式 是否是 get 请求   .lower的作用（传入的参数转为小写）不区分大小写
    if method.lower() =='get':
        #发送 get 请求
        res=requests.get(url,data,headers=headers)
    else:
        #发生post请求
        res=requests.post(url,data,headers=headers)

    try:
        log.info('接口返回值：{}'.format(res.text))
    except:
        log.error('接口返回值：{}'.format(res.text))
    return res

def __pre_url(url):
    """
    协议  + 域名 + 路径
    :return:
    """

    #获取  ini文件中  域名+协议
    base_url=conf.get('server','base_url')

    #判断传入的路径是否为  /开头
    if url.startswith('/'):
       return base_url + url
    else:
       return base_url + '/'+url


def __pre_data(data):
    """
    1. 字符串 变   字典
    2. null  变为  None
    :return:
    """
    #判断当前传入的数据是否是字符串并且  还不能是 空
    if isinstance(data,str) and data is not None:
        if data.find('null') != -1:
            data=data.replace('null',"None")

        if data.find('true') != -1:
            data = data.replace('true', "True")

        if data.find('false') != -1:
            data = data.replace('false', "False")

    #判断当前的值是否为 字典：字典不需要再次转为字典
    if isinstance(data,dict):
        return data
    if data is None:
        return data
    #字符串转为字典类型
    return eval(data)


def  __pre_json_type(json_type):
    #首先保证他是字符串
    if isinstance(json_type,str):
        #把传入的内容 ，替换为了首字符大写
        new_str=json_type.replace(json_type,json_type.title())

        #字符串转为  bool类型
        return eval(new_str)

    return json_type


def __pre__headers(login_status):

    #1. 先补全headers---从ini文件中的  headers中取所有值
    res = conf.items("headers")
    #把其中所有的值放入headers中
    headers = {}
    for i in res:
        headers.update({i[0]: i[1]})

    if login_status is None:
        # 3.从全局变量中找到token 然后补全       EnvData中找
        for key,val in headers.items():
            if key.find('token') != -1:
                if hasattr(EnvData,'token'):
                     headers.update({key:getattr(EnvData,'token')})
    return headers


if __name__ == '__main__':
    # data=__pre_data('{"name":"迪迦","age":None,"home":"M78星云","sex":"男"}')
    # __pre__json_type('TRue')
    # __pre__headers()
    pass