# 1. 打开文件
# 2. 选择表单
# 3. 获取所有的单元格
# 4. 组合
# 5. 关闭
from openpyxl import load_workbook

class HandleExcel():

    def __init__(self,filename,sheet_name):
        """
        :param filename: excel文件名
        :param sheet_name: 表单名
        """
        #打开工作薄
        self.wb=load_workbook(filename)
        #选择表单
        self.sh=self.wb[sheet_name]

    def __get_titles(self):

        keys=[]#所有的键名存放列表

        #获取表单第一行的所有单元格
        for i in list(self.sh.rows)[0]:
            #依次取值，然后放入 列表中
            keys.append(i.value)

        return keys

    def read_datas(self):
        #存放 打包好的数据  [{},{}]
        data=[]

        #获取除第一行外的所有行
        for i in list(self.sh.rows)[1:]:

            #所有值存放的列表
            values=[]
            for val in i:
                call_val=val.value
                if isinstance(call_val,str) and call_val is not None:
                    values.append(call_val.replace("\n",'').replace(' ','').replace('\xa0',''))
                else:
                    values.append(call_val)

            data.append(dict(zip(self.__get_titles(),values)))

        return data

if __name__ == '__main__':
    from Test.Interface.Common.handle_path import data_dir
    import os
    filename=os.path.join(data_dir,'萤火商城接口自动化测试用例.xlsx')
    excel=HandleExcel(filename,'购物车模块业务流')
    print(excel.read_datas())
