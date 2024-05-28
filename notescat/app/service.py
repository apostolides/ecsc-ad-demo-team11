#!/usr/bin/env python3
# Notes Cat

import os
import sys

# Getting input from the user
def get_user_input(txt):
	print(txt, end="")
	sys.stdout.flush() # flushing is needed so that socat don't produce errors
	return sys.stdin.readline()


# Challenge Start
# -----------------------------------------------------------
print(r'''
                                              /\_/\                  
                                             ( o.o )                 
Welcome to...                                 > ^ <                  
███╗   ██╗ ██████╗ ████████╗███████╗███████╗ ██████╗ █████╗ ████████╗
████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝██╔════╝██╔════╝██╔══██╗╚══██╔══╝
██╔██╗ ██║██║   ██║   ██║   █████╗  ███████╗██║     ███████║   ██║   
██║╚██╗██║██║   ██║   ██║   ██╔══╝  ╚════██║██║     ██╔══██║   ██║   
██║ ╚████║╚██████╔╝   ██║   ███████╗███████║╚██████╗██║  ██║   ██║   
╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   
                                     ...the purrfect notes keeper.   
''')

print("")


userfolder = None
while True:

	if userfolder is None:
		print("# [Unauthenticated]")
		print("# Select an action:")
		print("1. Login")
		print("2. Register")
		print("3. Password Reset")
		print("4. Exit")
		answer = get_user_input("> ").strip()
		print("")

		if answer == '1':
			print("# Please Login")
			username = get_user_input("username: ").strip()
			password = get_user_input("password: ").strip()

			password_file = os.path.join('.', 'files', username, 'password.txt')
			if not os.path.exists(password_file):
				print('[!] This username does not exist.')
			else:
				with open(password_file, 'r') as f:
					saved_password = f.read().strip()
				
				if (password == saved_password):
					userfolder = os.path.join('.', 'files', username)
					print('[!] You are now logged in.')
				else:
					print('[!] Invalid password.')

		elif answer == '2':
			print("# Please enter your information")
			username = get_user_input("username: ").strip()
			password = get_user_input("password: ").strip()
			os.makedirs(os.path.join('.', 'files'), exist_ok=True)
			os.makedirs(os.path.join('.', 'files', username), exist_ok=True)
			with open(os.path.join('.', 'files', username, 'password.txt'), 'w') as f:
				f.write(password)

			token = get_user_input("token: ").strip()
			with open(os.path.join('.', 'files', username, 'token.txt'), 'a') as f:
				f.write(token)
			print('[!] User was created. You can use this token to reset your password')

		elif answer == '3':
			print("# Please provide the following information")
			username = get_user_input("username: ").strip()
			token = get_user_input("token: ").strip()
			new_pw = get_user_input("new password: ").strip()

			token_file = os.path.join('.', 'files', username, 'token.txt')
			password_file = os.path.join('.', 'files', username, 'password.txt')

			if not os.path.join('.', 'files', username):
				print('[!] This username does not exist.')
			else:
				with open(token_file, 'r') as f:
					saved_token = f.read().strip()
				
				if (token in saved_token):
					with open(os.path.join('.', 'files', username, 'password.txt'), 'w') as f:
						f.write(new_pw)
						print('[!] Password reset was successful!')
				else:
					print('[!] Invalid token.')

		elif answer == '4':
			break

	else:
		print("# [Authenticated]")
		print("# Select an action:")
		print("1. New note")
		print("2. Open note")
		print("3. Logout")
		answer = get_user_input("> ").strip()
		print("")

		if answer == '1':
			print("# Please enter your note's information")
			name = get_user_input("Name: ").strip()
			content = get_user_input("Content: ").strip()

			notepath = os.path.join(userfolder, 'note-' + name + '.note')
			if os.path.exists(notepath):
				print("[!] A note with the same name already exists.")
				notepath = None

			if not notepath is None:
				with open(notepath, 'w') as f:
					f.write(content)
				print("[!] Your note was saved.")

		elif answer == '2':
			print("# Please enter your note's information")
			name = get_user_input("Name: ").strip()

			notepath = os.path.join(userfolder, 'note-' + name + '.note')
			if os.path.exists(notepath):
				with open(notepath, 'r') as f:
					print("Content: " + f.read())
			else:
				print("[!] Note was not found.")

		elif answer == '3':
			userfolder = None
			print("[!] You were logged out.")

	print("")

print("")
print(r'''
  /\_/\  
 ( o.o )
  > ^ < 
 MAU BYE
''')