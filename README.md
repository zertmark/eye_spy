# eye_spy
Simple script which takes screenshots and sends them on your email on Python 3                         
# INSTALL:                                         
git clone https://github.com/zertmark/eye_spy.git && cd eye_spy && chmod +x install.sh && ./install.sh                       
# RUN:                         
python3 eye.py -h                    

usage: eye.py [-h] [-t DELAY] [-n NUMBER] email password              

EYE SPY                      
 
positional arguments:                             
  email                 Email adress(gmail)                        
  password              Password from your email                              
 
optional arguments:                                  
  -h, --help                      show this help message and exit                                         
  -t DELAY, --delay DELAY         Delay in seconds after previous screenshot                                                       
  -n NUMBER, --number NUMBER      How many screenshots to take until sending email                         

