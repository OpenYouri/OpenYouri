"""
jsonpath

$ 根节点，所有表达式的开始
. 访问属性，获取子节点
.. 获取所有符合条件的组合
[] 访问数组  一般处理有下标的值  array
[,] 匹配多个结果
* 匹配所有，通配符
@ 代表当前节点
?()  表示过滤

$..id
$.data[0,1].id

$.data[?(@.age>=18)].id
"""
data={
    "code":200,
    "msg":"成功",
    "data":[
                {"name":"张三","age":18,"id":26},
                {"name":"李四","age":16,"id":28},
                {"name": "王五", "age": 16, "id": 88}
            ]
}


# from jsonpath import jsonpath
# print(jsonpath(data,'$.data[?(@.age>=18)].id'))

from jsonpath import jsonpath
print(jsonpath(data,'$..age'))