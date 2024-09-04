import re
"""
.  除了  \n外的 任意单个字符
*  匹配前一个字符一次或者多次
?  匹配前一个字符0次或者1次

"""
# (.*?)
id=18
str1='{"data":{"id":#id#,"name":#name#,"age":#age#,"home":#home#}}'

date=re.findall("#(.*?)#",str1)
print(date)

new_str=str1.replace("#{}#".format(date[0]),(id))
print(new_str)

"""
如果你的用例里面有特殊的规则  #需要替换的变量名#   那么会先把  你需要替换的变量名获取出来

然后去查看   全局变量（EnvData）   或者 配置文件（ini）  里面   是否存在这个值

如果存在那么替换
否则不替换


1. 全局变量的值在哪
2. ini的值

"""