"""
用户自定义配置文件
"""
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER = 'root'
PWD = "sdfsdf"

<<<<<<< HEAD
#MODE = "AGENT" # SALT,SSH
MODE = "SALT"  # SALT,SSH
=======
# MODE = "AGENT" # SALT,SSH
MODE = "SALT" # SALT,SSH
>>>>>>> c892015b3a1e0cb2c895450c8f6a1893c0a2d4d6

DEBUG = True


SSH_USER = "root"
SSH_PWD = "root"
SSH_KEY = "/xxx/xxx/xx"
SSH_PORT = 22



PLUGINS_DICT = {
    'basic': "src.plugins.basic.Basic",
    'board': "src.plugins.board.Board",
    'cpu': "src.plugins.cpu.Cpu",
    'disk': "src.plugins.disk.Disk",
    'memory': "src.plugins.memory.Memory",
    'nic': "src.plugins.nic.Nic",
}

API = "http://www.oldboyedu.com"
