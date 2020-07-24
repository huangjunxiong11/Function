"""
# 下面四句代码将该文件所处文件夹目录加到了导包目录中, 在启动py文件里面加上这句话
import os
import pathlib
import sys
sys.path.insert(0, os.path.abspath(pathlib.Path.cwd()))
"""
import glob
import os
import pathlib
import sys


class OsExample(object):
    def __init__(self):
        pass

    def get_py(self, path, format):
        """
        :param path: 文件夹,如“dirs/jpgs”
        :param format: 文件格式，如“*.py”
        :return: 该文件夹下面所有满足文件格式的文件组成的列表
        """
        BaseName = os.path.abspath(path)
        BaseName = glob.glob(os.path.join(BaseName, format))  # 读取文件夹下面所有的文件
        return BaseName


pass
