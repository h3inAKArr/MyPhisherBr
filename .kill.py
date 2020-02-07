

import os
import re
from time import sleep



user = os.popen("whoami").read()[:-1]

def kill(service):
  saida = os.popen("ps -u {}".format(user)).read()
  out = re.findall(r"([\w]+)[\/?\:?\w?\ ?]+{}".format(service),saida)
  for pid in out:
    os.system("kill {}".format(pid))
  os.system("pkill -f {}".format(service))

while 1:
  sleep(3)
  s = os.popen("ps").read()
  o = re.findall(r"([\w]+)[\/?\:?\w?\ ?]+python",s)
  if len(o) == 1:
    kill("php")
    kill("ngrok")
    break
