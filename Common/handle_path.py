import os

base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#配置文件层
conf_dir=os.path.join(base_dir,'Conf')
#用例层
case_dir=os.path.join(base_dir,'TestCase')

#测试用例文件路径
data_dir=os.path.join(base_dir,'TestDates')

logs_dir=os.path.join(base_dir,'OutPuts','log')
report_dir=os.path.join(base_dir,'OutPuts','report')
