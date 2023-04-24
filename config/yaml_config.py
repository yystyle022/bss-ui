import os
import yaml


class GetConfig:
    def __init__(self):
        self.current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


    def get_redis(self):
        '''
        返回redis信息
        @return:
        '''
        with open(self.current_path + '\config\environment.yaml') as f:
            environment = yaml.load(f.read(), Loader=yaml.FullLoader)
            return environment['redis']

if __name__ == '__main__':
    print(GetConfig().get_redis()['host'])
