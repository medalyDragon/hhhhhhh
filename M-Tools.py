## M-Tools.py - M-Tools v 19.9                          
# -*- coding: utf-8 -*-
##
import os
import sys
from time import sleep as timeout
from core.lzmcore import *

def main():
	banner()
	print "   [01] termux-ohmyzsh"
	print "   [02] Wordpresscan"
        print "   [03] Metasploit"
        print "   [04] x-project"
	print "   [05] WPSploit"
	print "   [06] sqlmap"
	print "   [07] Ngrok"
	print "   [08] OSIF"
	print "   [09] Nmap\n"
	print "   [10]Exit the M-Tools\n"
	M-Tools = raw_input("lzmx > ")  

  if M-Tools == "1" or M-tools == "01":
         termux-ohmyzsh()
  elif M-Tools == "2" or M-tools == "02":
         Wordpresscan() 
  elif M-Tools == "3" or M-tools == "03":
         Metasploit()
  elif M-Tools == "3" or M-tools == "03":
  	    x-project()       
  elif M-Tools == "5" or M-tools == "05":
         WPSploit()
  elif M-Tools == "6" or M-tools == "06":
         sqlmap()
  elif M-Tools == "7" or M-tools == "07":
         Ngrok()
  elif M-Tools == "8" or M-tools == "08": 

  elif  M-Tools == "9" or M-tools == "09":

  elif   M-Tools == "10"
		sys.exit()

	else:
		print "\nERROR: Wrong Input"
		timeout(2)
		restart_program()

if __name__ == "__main__":
	main()
