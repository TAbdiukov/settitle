#!/usr/bin/env python3

import sys
import platform
from os import system

def full_arg():
	return " ".join(sys.argv[1:])
	
def PROGRAM_NAME():
	return "settitle"

def environment():		
	# https://docs.python.org/3/library/platform.html#platform.platform
	# Returns the system/OS name, e.g. 'Linux', 'Windows', or 'Java'. An empty string is returned if the value cannot be determined.
	# also https://stackoverflow.com/a/4553152 (seemily only person who speaks reason)
	return platform.system().lower()

def show_help():
	print("USAGE:")
	print("python "+PROGRAM_NAME()+".py <title>")

def title(s):
		e = environment()
		
		ret = -1
			
		if(e=="windows"):
			ret = title_win(s)
		elif (e=="linux"):
			ret = title_linux(s)
		elif (e=="java"):
			raise WeirdOSException("Java not currently cupported")
		else:
			raise WeirdOSException("Unknown OS ("+e+")")
			
		return ret

# no root rights required
def title_win(myCoolTitle):
	# https://stackoverflow.com/a/10229529
	buf = "title "+myCoolTitle
	print(buf)
	# Windows trips over when subprocess is used so
	system(buf)
	system("pause")
	#print(system)
	#print(proc)

	return 0

def title_linux(myCoolTitle):
	buf = "echo -ne \\"+chr34+"\\033]0;"+myCoolTitle+"\\007\\"+chr(34)
	proc = subprocess.Popen(buf, stdout=subprocess.PIPE)
	
	streamdata = proc.communicate()[0]
	return proc.returncode
		
class WeirdOSException(Exception):
	pass
		
if __name__ == '__main__':
	argc = len(sys.argv) - 1
	
	if (argc == 0): # default
		show_help()
	else:
		title(full_arg())
