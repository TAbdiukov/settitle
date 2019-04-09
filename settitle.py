#!/usr/bin/env python3

import sys
import platform
from abc import ABC, abstractmethod
from os import system

class settitle(ABC):

	@staticmethod
	def full_arg():
		return " ".join(sys.argv[1:])
		
	@staticmethod
	def PROGRAM_NAME():
		return "settitle"

	@staticmethod
	def environment():		
		# https://docs.python.org/3/library/platform.html#platform.platform
		# Returns the system/OS name, e.g. 'Linux', 'Windows', or 'Java'. An empty string is returned if the value cannot be determined.
		# also https://stackoverflow.com/a/4553152 (seemily only person who speaks reason)
		return platform.system().lower()

	@staticmethod
	def show_help():
		print("USAGE:")
		print("python "+settitle.PROGRAM_NAME()+".py <title>")

	@staticmethod
	def title():
		argc = len(sys.argv) - 1
		
		if (argc == 0): # default
			settitle.show_help()
		else:
			s = settitle.full_arg()
			e = settitle.environment()
			
			ret = -1
				
			if(e=="windows"):
				ret = settitle_Windows.title(s)
			elif (e=="linux"):
				ret = settitle_Linux.title(s)
			elif (e=="java"):
				raise WeirdOSException("Java not currently cupported")
			else:
				raise WeirdOSException("Unknown OS ("+e+")")

class settitle_Windows(settitle):
	@staticmethod
	def my_os():
		return "windows"
	
	# no root rights required
	@staticmethod
	def title(myCoolTitle):
		# https://stackoverflow.com/a/10229529
		buf = "title "+myCoolTitle
		#print(buf)
		# Windows trips over when subprocess is used so
		from os import system
		system(buf)
		#system("pause")
		#print(system)
		#print(proc)

		return 0


class settitle_Linux(settitle):
	import subprocess # https://docs.python.org/3/library/subprocess.html

	@staticmethod
	def my_os():
		return "linux"
	
	# Allow the user to set the title.
	# https://superuser.com/a/84711 (modified)
	@staticmethod
	def title(myCoolTitle):
		buf = "echo -ne \\"+chr34+"\\033]0;"+myCoolTitle+"\\007\\"+chr(34)
		proc = subprocess.Popen(buf, stdout=subprocess.PIPE)
		
		streamdata = proc.communicate()[0]
		return proc.returncode
		
class WeirdOSException(Exception):
	pass
		
if __name__ == '__main__':
	h = settitle.title()
	print("Done")