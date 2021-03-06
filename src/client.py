import requests
import json
from src.plugins import PluginManager
from lib.conf.config import settings

class Base(object):
    def post_asset(self,server_info):
        requests.post(settings.API,json=server_info)
        # body: json.dumps(server_info)
        # headers= {'content-type':'application/json'}
        # request.body
        # json.loads(request.body)

class Agent(Base):

    def execute(self):
        server_info = PluginManager().exec_plugin()
        self.post_asset(server_info)

class SSHSALT(Base):
    def get_host(self):
        # 获取未采集的主机列表：
        response = requests.get(settings.API)
        # result = json.loads(response.text) # "{status:'True',data: ['c1.com','c2.com']}"
        result = {"status": True, 'data': ['web07',]}
        if not result['status']:
            return
        return result['data']

    def execute(self):
        host_list = self.get_host()
        for host in host_list:
            server_info = PluginManager(host).exec_plugin()
            self.post_asset(server_info)