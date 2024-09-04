from Test.Interface.Common.handle_data import EnvData
from Test.Interface.Common.handle_logger import log
"""
从接口的返回值中  通过json表达式   获取到值  放入  全局变量  EnvData
"""
from jsonpath  import jsonpath
def data_from_response(response,expression):
    """
    :param response: 接口的返回值
    :param expression: json表达式
    :return:
    """
    expression=eval(expression)
    for key,val in expression.items():

        value=jsonpath(response,val)[0]

        try:
            log.info("设置全局变量 key :{}   ====value：  {}".format(key,value))
            setattr(EnvData,key,str(value))
            log.info('目前全局变量中的值：{}'.format(EnvData.__dict__.items()))
        except:
            log.error("当前全局变量Key为：{}".format(key))
            raise

if __name__ == '__main__':
    dict={
        "result_code": "200",
        "result_msg": "新增成功",
        "data": [
                {
                        "id": 2408
                }
        ]
}
    data_from_response(dict,'{"id":"$..id"}')

    print(getattr(EnvData,'id'))