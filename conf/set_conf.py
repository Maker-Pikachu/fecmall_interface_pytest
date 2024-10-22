# Author: Sanmu
# CreatTime: 2024/10/22
# Descriptior: 描述
import configparser
import pathlib

file = pathlib.Path(__file__).parents[0].resolve() / 'conf.ini'

# 读取配置文件
def read_conf(section, option):
    conf = configparser.ConfigParser()
    conf.read(file)
    values = conf.get(section, option)
    return values

# 写入配置文件
def write_conf(section, option, value):
    conf = configparser.ConfigParser()
    conf.read(file)
    conf.set(section, option, value)
    with open(file, 'w') as f:
        conf.write(f)