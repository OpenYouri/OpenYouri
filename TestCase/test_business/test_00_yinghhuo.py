"""
===========================
@Author: 日月腾飞
@Project: 萤火接口框架
@File: test_00_yinghhuo.py
@Time: 2024/2/2 17:50
===========================
"""

import pytest
import os

from Common.handle_data import replace_case_by_regular
from Common.handle_data_from_response import data_from_response
from Common.handle_excel import HandleExcel
from Common.handle_path import data_dir
from Common.handle_request import send_request

filename=os.path.join(data_dir,'萤火商城接口自动化测试用例.xlsx')
excel=HandleExcel(filename,'萤火商城业务流')
data=excel.read_datas()

@pytest.mark.Business
@pytest.mark.usefixtures("phone")
class Test():

    @pytest.mark.parametrize('case',data)
    def test(self,case):
        # 1. 替换数据---#变量#
        case=replace_case_by_regular(case)
        #2. 发送接口请求
        res = send_request(case['url'],case['method'],case['data'],case['json_type'],case['login_status'])

        #3. 是否需要提取值，放入  全局变量中
        if case['jsonpath']:
            data_from_response(res.json(),case['jsonpath'])
