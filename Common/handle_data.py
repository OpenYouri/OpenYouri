import re
#全局属性存放位置-----全局变量
from Test.Interface.Common.handle_config import conf
from Test.Interface.Common.handle_logger import log

class EnvData():
    pass


def replace_case_by_regular(case):
    """
    根据你传入的  case 替换里面对应的规则   #需要替换的变量名#
    :return:
    """
    log.info("需要替换的case:{}".format(case))
    for key,val in case.items():
        if val is not None and isinstance(val,str):
            case[key]=replace_by_regular(val)

    return case


def replace_by_regular(val):
    """

    :param val: 需要替换的值
    :return:
    """
    """
    1. 通过正则表达式取找 这个值是否需要替换   ---  #变量名#
    2. 全局变量  EnvData
    3. 全局配置文件  ini
    
    如果可以找到 替换，否则，不替换
    """

    #通过正则表达式取找 这个值是否需要替换   ---  #变量名#
    res =re.findall('#(.*?)#',val)

    #先判断是否需要替换
    if res:

        for item in res:

            try:
                #全局变量  EnvData 查看是否存在  item
                value = getattr(EnvData,item) #如果没有找到该值，会发生报错
            except:
                try:

                    #如果全局变量 EnvData没有找到那么取找  ini文件的  data块
                    value = conf.get('data',item)
                    print(value)
                except:
                    #如果  ini和 EnvData 都找不到那么这个值不找了，开始去找下一个值
                    continue

            val=val.replace("#{}#".format(item),value)
            log.info('替换的key为 ：{}  替换后的字符串：{}'.format(item,val))


    return val

