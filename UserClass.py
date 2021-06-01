import random
import json
import smtplib
import hashlib
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def configuration_create():

	# creating connection
	connection = sqlite3.connect("chess_users.db")

	# creating cursor
	cursor = connection.cursor()

	# creating table with user's creds
	cursor.execute("CREATE TABLE IF NOT EXISTS user (nickname TEXT, password TEXT, win_score INTEGER, lose_score INTEGER)")

	cursor.close()

	connection.close()


class User: 

	def __init__(self, users_config):

		self.users_config = users_config
		self.user_figures = []


	def registration(self):

		# creating connection
		connection = sqlite3.connect(self.users_config)

		# creating cursor
		cursor = connection.cursor()

		# user's nickname attribute
		self.nickname = input("Please enter your nickname: ")
		# user's client password attribute
		self.password = input("Please enter your password: ")

		# user's email address to send a password for registration
		self.email_address = input("Enter your email address to send you a password for registration: ")

		# hashing our client password
		self.bytes_password = str.encode(self.password)
		self.hashed_password = hashlib.sha1(self.bytes_password)

		# our client password hashed
		self.hex_dig = self.hashed_password.hexdigest()

		# trigger to stop the loop if we need so
		self.loop_status = True

		while self.loop_status:

			# the password
			self.random = ""
			for i in range(0,6):
				n = random.randint(0,10)
				self.random += str(n)


			self.registration_code_sender(self.random)

			self.user_code_input = str(input("Please enter the password here: "))

			if self.user_code_input == self.random:

				params = (self.nickname, self.hex_dig, 0, 0)

				# inserting values to db
				cursor.execute("INSERT INTO user VALUES (?, ?, ?, ?)", params)

				connection.commit()

				# closing the cursor
				cursor.close()

				# closing db connection
				connection.close()

				print("Registration success! \n" \
					f"Hi {self.nickname}!")

				break

			else:
				print("The password was wrong, We can send another password")
				print("If you want new password, type `y` \n" \
				 "if you wan't to cancel registration, enter `!exit!`")

				while True:
					self.user_choice_input = input("Your choice: ")

					if self.user_choice_input == "!exit":

						# closing the cursor
						cursor.close()

						# closing db connection
						connection.close()

						self.loop_status = False
						print("Goodbye!")
						break

					elif self.user_choice_input == "y":
						self.random = ""
						break
					else:
						print("Please enter a valid choice")
						self.user_choice_input = input("Your choice: ")


	def login(self):

		connection = sqlite3.connect(self.users_config)
		cursor = connection.cursor()

		# user's nickname attribute
		self.nickname = input("Please enter your nickname: ")
		# user's client password attribute
		self.password = input("Please enter your password: ")

		# hashing our client password
		self.bytes_password = str.encode(self.password)
		self.hashed_password = hashlib.sha1(self.bytes_password)

		# our client password hashed
		self.hex_dig = self.hashed_password.hexdigest()

		rows = cursor.execute(
		    "SELECT nickname, password, win_score, lose_score FROM user WHERE nickname = ?",
		    (self.nickname,),
		).fetchall()

		while True:
			if rows:
				if self.hex_dig == rows[0][1]:
					print(f"login success! Hello {self.nickname}")

					# closing cursor connection
					cursor.close()

					# closing db connection

					connection.close()

					break
				else:
					print("Either your password or login are incorrect, please enter correct values")
					# user's nickname attribute
					self.nickname = input("Please enter your nickname: ")
					# user's client password attribute
					self.password = input("Please enter your password: ")

					# hashing our client password
					self.bytes_password = str.encode(self.password)
					self.hashed_password = hashlib.sha1(self.bytes_password)

					# our client password hashed
					self.hex_dig = self.hashed_password.hexdigest()
			else:
				print("Either your password or login are incorrect, please enter correct values")
				# user's nickname attribute
				self.nickname = input("Please enter your nickname: ")
				# user's client password attribute
				self.password = input("Please enter your password: ")

				# hashing our client password
				self.bytes_password = str.encode(self.password)
				self.hashed_password = hashlib.sha1(self.bytes_password)

				# our client password hashed
				self.hex_dig = self.hashed_password.hexdigest()



	# registration code sending function
	def registration_code_sender(self, sample_code):

		# server connection and sending password to user for registration
		self.server = smtplib.SMTP_SSL("smtp.mail.ru", 465)

		# server listening
		self.server.ehlo()

		# logging in
		self.server.login("chessgameregistration@mail.ru", "checkmatesarenice456")

		# multiparting mail to send
		self.msg = MIMEMultipart()
		self.msg["From"] = "chessgameregistration@mail.ru"
		self.msg["To"] = self.email_address
		self.msg["Subject"] = "Chess game registration code"

		self.text = f"Your password for Chess game is {sample_code} \n " \
				"Please don't answer to this email. \n" \
				"Best regards! \n" \
				"Chessgameregistration team"

		self.msg.attach(MIMEText(self.text, "plain"))

		self.main_msg = self.msg.as_string()

		self.server.sendmail("chessgameregistration@mail.ru", self.email_address, self.main_msg)
		print(f"Mail sended to {self.email_address}")

		self.server.close()


	# main Register, Login function
	def connect(self):
		"""
	    Connect function:

	    Connect function, which activates as the programm starts
	    providing Login?/Register option for user

	    Attributes:
        
	    ----------
	    choice: user's choice variable
    	"""

		# ask user if register or login 

		print("Would You like to register or login? \n",
			"if you want to register press `r` \n",
			"if you want to login press `l` \n",
			"If you want to close the programm type `!exit`")

		# user's choice
		choice = str(input(": "))

		# loop for executing the login/register process,
		# and in case if user write's wrong initial,
		# programm will work untill it executes properly

		while True:

			# register option
			if choice == "r":
				self.registration()
				break

			# login option
			elif choice == "l":
				self.login()
				break

			# programm exit option
			elif choice == "!exit":
				print("Closing the programm...")
				print("Goodbye!")
				break

			else:
				print("Please enter valid choice: ")
				choice = str(input())


	# user moving his figures from coordinates:
	def user_move_from(self):

		second_position = None

		from_list = []

		print("Which figure? (example=b2)")

		loop_status = True

		secondary_status = True

		choice = str(input(": "))

		while loop_status:

		    if choice[1].isnumeric() and choice[0].isalpha() and choice[1] != 0:
		        loop_status = False
		    else:
		        print("Please insert correct values, example: b2")
		        choice = str(input(": "))

		while secondary_status:

			if choice[0] in "abcdefgh" and 0 < int(choice[1]) < 9:
				secondary_status = False
			else:
				print("Please insert correct coordinates")
				choice = str(input(": "))

		# first position
		from_list.append(8 - int(choice[1]))

		# second position
		second_position = ord(choice[0]) - 97

		# second position
		from_list.append(second_position)		

		return from_list


	# user moving his figures to coordinates
	def user_move_to(self):

		second_position = None

		to_list = []

		print("Where to? (example=b2)")

		loop_status = True

		secondary_status = True

		choice = str(input(": "))

		while loop_status:

		    if choice[1].isnumeric() and choice[0].isalpha() and choice[1] != 0:
		        loop_status = False
		    else:
		        print("Please insert correct values, example: b2")
		        choice = str(input(": "))

		while secondary_status:

			if choice[0] in "abcdefgh" and 0 < int(choice[1]) < 9:
				secondary_status = False
			else:
				print("Please insert correct coordinates")
				choice = str(input(": "))

		# first position
		to_list.append(8 - int(choice[1]))

		# second position
		second_position = ord(choice[0]) - 97

		# second position
		to_list.append(second_position)		

		return to_list
		

	# checking the status for the figure
	# if it is false, we delete it from the list
	def user_figure_check(self):

		for figure in self.user_figures:
			if figure.figure_status != False:
				continue
			else:
				del figure
				break



class UserCommunication:

    def __init__(self, socket):
        # saving the socket inside the class
        self.socket = socket

    # making a sending msg function
    def send_msg(self, msg):
        # initial message which must be sent
        message = json.dumps(msg).encode("utf-8")
        # variable for message char length as integer
        msg_length = len(message)
        # converting length into str and formatting into `utf-8`
        send_length = str(msg_length).encode("utf-8")
        # refilling the empty bytes with a space so that we can send the full length
        send_length += b' ' * (128 - len(send_length))
        # sending to the socket the full length including the message
        self.socket.send(send_length)
        # sending the main message to the client
        self.socket.send(message)

    # creating a msg receiving function
    def receiving_msg(self):
        msg_length = self.socket.recv(128).decode("utf-8")

        if msg_length:
            # reformatting it into an integer
            msg_length = int(msg_length)
            # telling how many bites are we going to receive with the message
            main_msg = self.socket.recv(msg_length).decode("utf-8")
            dict_msg = json.loads(main_msg)

            return dict_msg