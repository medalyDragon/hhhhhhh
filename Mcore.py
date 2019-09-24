## Mcore.py - useful module of M-Tools
# -*- coding: utf-8 -*-
import os
import sys
import time

M-Tools_banner = """
 __  __    ______           _ 
|  \/  |   |_   _|__   ___ | |___
| |\/| |_____| |/ _ \ / _ \| / __|
| |  | |_____| | (_) | (_) | \__ \
|_|  |_|     |_|\___/ \___/|_|___/

  by Mohamed Aly Sidi Mohamed
  
"""
 
 backtomenu_banner = """   
   [10] Exit the M-Tools
"""

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print backtomenu_banner
	backtomenu = raw_input("lzmx > ")
	
	
	if backtomenu == "10":
		sys.exit()
	else:
		print "\nERROR: Wrong Input"
		time.sleep(2)
		restart_program()

def banner():
	print M-Tools_banner

   
def termux-ohmyzsh():
	print '\n###### Installing termux-ohmyzsh'
	os.system('apt update && apt upgrade')
	os.system('pkg install git')
	os.system('git clone https://github.com/cabbagec/termux-ohmyzsh')
	print '###### Done'
	backtomenu_option()


def wordpreSScan():
	print '\n###### Installing Wordpresscan'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 python2-dev clang libxml2-dev libxml2-utils libxslt-dev')
	os.system('git clone https://github.com/swisskyrepo/Wordpresscan')
	os.system('mv Wordpresscan ~')
	os.system('cd ~/Wordpresscan && python2 -m pip install -r requirements.txt')
	print '###### Done'
	backtomenu_option()


def wordpresscan():
	print '\n###### Installing wordpresscan(2)'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap figlet git')
	os.system('git clone https://github.com/silverhat007/termux-wordpresscan')
	os.system('cd termux-wordpresscan && chmod +x * && sh install.sh')
	os.system('mv termux-wordpresscan ~')
	print '###### Done'
	print "###### Type 'wordpresscan' to start."
	backtomenu_option()

def x-project():
	print '\n###### Installing x-project(2)'
	os.system('pkg update')
	os.system('pkg upgrade')
	os.system('pkg install python2')
	os.system('pkg install git')
	os.system('git clone https://github.com/haitemaouati/X-project')
	print '###### Done'
	backtomenu_option()


def metasploit():
	print '\n###### Installing Metasploit'
	os.system("apt update && apt upgrade")
	os.system("apt install git wget curl")
	os.system("wget https://gist.githubusercontent.com/Gameye98/d31055c2d71f2fa5b1fe8c7e691b998c/raw/09e43daceac3027a1458ba43521d9c6c9795d2cb/msfinstall.sh")
	os.system("mv msfinstall.sh ~;cd ~;sh msfinstall.sh")
	print '###### Done'
	print "###### Type 'msfconsole' to start."
	backtomenu_option()


def wpsploit():
	print '\n###### Installing WPSploit'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone git clone https://github.com/m4ll0k/wpsploit')
	os.system('mv wpsploit ~')
	print '###### Done'
	backtomenu_option()

def sqlmap():
	print '\n###### Installing sqlmap'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/sqlmapproject/sqlmap')
	os.system('mv sqlmap{} ~')
	print '###### Done'
	backtomenu_option()
	

def ngrok():
	print '\n###### Installing Ngrok'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/themastersunil/ngrok')
	os.system('mv ngrok ~')
	print '###### Done'
	backtomenu_option()

def osif():
	print '\n###### Installing OSIF'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/ciku370/OSIF')
	os.system('mv OSIF ~')
	print '###### Done'
	backtomenu_option()
def nmap():
	print '\n###### Installing Nmap'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap')
	print '###### Done'
	print "###### Type 'nmap' to start."
	backtomenu_option()