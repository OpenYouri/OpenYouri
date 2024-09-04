
# from Common.handle_mysql import HandleMysql
import pytest
import requests
from Test.Interface.Common.handle_logger import log_close
from Test.Interface.Common.handle_data import EnvData
from Test.Interface.Common.handle_phone import get_new_phone


@pytest.fixture(scope='session',autouse=True)
def db():
    #实例化数据库
    # db=HandleMysql()
    yield #db#返回数据库对象
    #关闭数据库对象
    # db.close()
    log_close()

@pytest.fixture(scope='class')
def phone():
    phone_data=get_new_phone()
    setattr(EnvData,'phone',phone_data)