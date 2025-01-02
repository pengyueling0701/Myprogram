import os
import configparser

cur_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件所在路径
configPath = os.path.join(cur_path, "setting.ini")  # 拼接出文件路径
conf = configparser.ConfigParser()


class ReadConfig:
    def __init__(self):
        conf.read(configPath)  # 读取配置文件setting.ini

    def get_env(self):
        return conf.get('env', 'env')

    def get_url(self, env):
        return conf.get(env, "task_url")

    def get_token(self, env):
        return conf.get(env, "token")


if __name__ == '__main__':
    rg = ReadConfig()
    temp = rg.get_env()
    print("env ", rg.get_env())
    print(rg.get_url(temp))
    print(rg.get_token(temp))
