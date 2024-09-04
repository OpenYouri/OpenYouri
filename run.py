import pytest
import threading
from Test.Interface.Common.handle_path import report_dir

"""
一般是  某一个线程 执行某类测试用例

1.  业务流
2.  模块的
3.  冒烟
"""
def test(mark):
    pytest.main([
                '-s', '-v', '-m', '{}'.format(mark),
                "--alluredir={}".format(report_dir),
                "--reruns", "2", "--reruns-delay", "3"
                 ])

marks=["Business","not Business"]
for i in marks:
    t=threading.Thread(target=test(i))
    t.start()

pytest.main(['-s', '-v',
            "--alluredir={}".format(report_dir)])
