"""
我把这包引入过来，我直接能获取到  conf

用的时候直接   conf.get()
"""
from configparser import ConfigParser
from Test.Interface.Common.handle_path import conf_dir
import os
class HandleConfig(ConfigParser):

    def __init__(self,filename):
        super().__init__()
        self.read(filename,encoding='utf-8')

filename=os.path.join(conf_dir,'keen.ini')

#这个是需要引用的
conf=HandleConfig(filename)

