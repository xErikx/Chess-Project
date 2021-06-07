import random
import json
import smtplib
import hashlib
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def configuration_create():
	"""
    Creatingconfiguration function:

    Creating database file configuration function for user's creds availability

    Attributes:
    	connection: connection variable responsible for connection to db file
    	cursor: cursor variable for db use in general

	"""

	# creating connection
	connection = sqlite3.connect("chess_users.db")

	# creating cursor
	cursor = connection.cursor()

	# creating table with user's creds
	cursor.execute("CREATE TABLE IF NOT EXISTS user (nickname TEXT, password TEXT, email_address TEXT, win_score INTEGER, lose_score INTEGER)")

	# closing cursor
	cursor.close()

	# closing db connection
	connection.close()


class User: 
	"""
    A class used to represent User in email client

    ...

    Attributes
    ----------
    nickname : str
        user's nickname for client
    password : str
        user's client password
    email_address : str
        user's email address to login to server

    Methods
    -------
    registration:
        User's registration to client
    login:
		User's login to client
    connect:
		User's options for logins/registration to client
	win_score_update:
		Users win score update if he wins
	lose_score_update:
		Users lose score update if he loses
	registration_code_sender:
		code sender which sends registration code to user's email address
	user_move_from:
		coordinates sending option which figures must move
	user_move_to:
		coordinates sending option where figures should move
    """

	def __init__(self, users_config, socket):
		"""
        Parameters
        ----------
        users_config: user's creds in db configuration file

        Attributes
		
		users_config: user config file
		
		users_figures: user's figures list, which will be filled when game starts

		communication: user's communication attrbute with socket connection
        """

		# saving socket attribute
  		self.socket = socket

  		self.users_config = users_config

  		self.user_figures = []

  		self.communication = UserCommunication(self.socket)




	def win_score_update(self):
		"""
	    win_score_update:
		
	    Users win score update function if he wins

	    Attributes:
	    ----------
	    connection: connection variable responsible for connection to db file
    	cursor: cursor variable for db use in general
    	new_score: updated score
    	"""
		
		# creating connection
		connection = sqlite3.connect(self.users_config)

		# creating cursor
		cursor = connection.cursor()

		rows = cursor.execute(
		    "SELECT nickname, password, win_score, lose_score FROM user WHERE nickname = ?",
		    (self.nickname,),
		).fetchall()

		new_score = rows[0][2] + 1

		cursor.execute(f'UPDATE user SET win_score = {new_score} WHERE nickname = "{self.nickname}"')

		connection.commit()

		cursor.close()

		connection.close()


	def lose_score_update(self):
		"""
	    lose_score_update:
		

	    Users lose score update function if he loses

	    Attributes:
	    ----------
	    connection: connection variable responsible for connection to db file
    	cursor: cursor variable for db use in general
    	new_score: updated score
    	"""

		# creating connection
		connection = sqlite3.connect(self.users_config)

		# creating cursor
		cursor = connection.cursor()

		rows = cursor.execute(
		    "SELECT nickname, password, win_score, lose_score FROM user WHERE nickname = ?",
		    (self.nickname,),
		).fetchall()

		new_score = rows[0][3] + 1

		cursor.execute(f'UPDATE user SET lose_score = {new_score} WHERE nickname = "{self.nickname}"')

		connection.commit()

		cursor.close()

		connection.close()


	def registration(self):
		"""
	    Registration function:

	    Registration function, which stores user's creds
	    to db configuration file

	    Attributes:
	    ----------
	    self.nickname: user's nickname variable
	    self.password: user's mail client variable
	    self.email_address: user's email address to receive registration code
	    connection: connection to db configuration file
	    cursor: db configuration file cursor
	    self.hex_dig: hashed password
    	"""

		# creating connection
		connection = sqlite3.connect(self.users_config)

		# creating cursor
		cursor = connection.cursor()

		self.communication.send_msg("Please enter your nickname")

		# user's nickname attribute
		self.nickname = self.communication.receiving_msg()["msg"]

		self.communication.send_msg("Please enter your password")

		# user's client password attribute
		self.password = self.communication.receiving_msg()["msg"]

		self.communication.send_msg("Enter your email address to send you a password for registration")

		# user's email address to send a password for registration
		self.email_address = self.communication.receiving_msg()["msg"]

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

			self.communication.send_msg(f"Mail sended to {self.email_address}. Please enter the password here")

			self.user_code_input = str(self.communication.receiving_msg()["msg"])

			if self.user_code_input == self.random:

				params = (self.nickname, self.hex_dig, self.email_address, 0, 0)

				# inserting values to db
				cursor.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?)", params)

				connection.commit()

				# closing the cursor
				cursor.close()

				# closing db connection
				connection.close()

				print("Registration success! \n" \
					f"Hi {self.nickname}!")

				break

			else:
				

				while True:

					self.communication.send_msg("The password was wrong, We can send another password \n" \
					"1) If you want new password, type `y` \n" \
					"2) if you wan't to cancel registration, enter `!exit!`")

					self.user_choice_input = self.communication.receiving_msg()["msg"]

					if self.user_choice_input == "!exit":

						# closing the cursor
						cursor.close()

						# closing db connection
						connection.close()

						self.loop_status = False
						self.communication.send_msg("Goodbye!")
						break

					elif self.user_choice_input == "y":
						self.random = ""
						break
					else:
						self.communication.send_msg("Please enter a valid choice")
						self.user_choice_input = self.communication.receiving_msg()["msg"]


	def login(self):
		"""
	    Login function:

	    Login function, which provides logging in into client with user's creds
	    from json configuration file

	    Attributes:
        
	    ----------
	    self.nickname: user's nickname variable
	    self.password: user's mail client variable
	    self.email_address: user's email address to receive registration code
	    connection: connection to db configuration file
	    cursor: db configuration file cursor
	    self.hex_dig: hashed password
    	"""

		connection = sqlite3.connect(self.users_config)
		cursor = connection.cursor()

		self.communication.send_msg("Please enter your nickname")

		# user's nickname attribute
		self.nickname = self.communication.receiving_msg()["msg"]

		self.communication.send_msg("Please enter your password")

		# user's client password attribute
		self.password = self.communication.receiving_msg()["msg"]

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
					self.communication.send_msg("Either your password or login are incorrect, please enter correct values. \n" \
					"Please enter your nickname")

					# user's nickname attribute
					self.nickname = self.communication.receiving_msg()["msg"]

					self.communication.send_msg("Please enter your password")

					# user's client password attribute
					self.password = self.communication.receiving_msg()["msg"]


					# hashing our client password
					self.bytes_password = str.encode(self.password)
					self.hashed_password = hashlib.sha1(self.bytes_password)

					# our client password hashed
					self.hex_dig = self.hashed_password.hexdigest()
			else:
				self.communication.send_msg("Either your password or login are incorrect, please enter correct values. \n" \
				"Please enter your nickname")
					
				# user's nickname attribute
				self.nickname = self.communication.receiving_msg()["msg"]

				self.communication.send_msg("Please enter your password")

				# user's client password attribute
				self.password = self.communication.receiving_msg()["msg"]

				# hashing our client password
				self.bytes_password = str.encode(self.password)
				self.hashed_password = hashlib.sha1(self.bytes_password)

				# our client password hashed
				self.hex_dig = self.hashed_password.hexdigest()



	def registration_code_sender(self, sample_code):
		"""
	    registration_code_sender function:

	    Registration code sender, which provides registration code to the user

	    Attributes:
	    ----------
	    self.server: smtp protocol mail server
	    self.msg: multipart message 
	    self.main_msg: main message with registration code
    	"""

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
		

		self.server.close()


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

		self.communication.send_msg("Would You like to register or login? \n" \
		"if you want to register press `r` \n" \
		"if you want to login press `l` \n" \
		"If you want to close the programm type `!exit`")

		# user's choice
		choice = str(self.communication.receiving_msg()["msg"])

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
				self.communication.send_msg("Please enter valid choice: ")
				choice = self.communication.receiving_msg()["msg"]


	def user_move_from(self):
		"""
	    user_move_from function:

	    Sending initial coordinates of figure to move

	    Attributes:
	    	from_list: initially empty coordinates list
	    	choice: user's input
	    	first_position: first coordinate for board
	    	second_position: second coordinate for board

	    Returns:
	    ----------
	    	Returns from_list with coordinates 
		"""

		second_position = None

		from_list = []

		self.communication.send_msg("Which figure? (example=b2)")

		loop_status = True

		secondary_status = True

		choice = str(self.communication.receiving_msg()["msg"])

		while loop_status:

		    if choice[1].isnumeric() and choice[0].isalpha() and choice[1] != 0:
		        loop_status = False
		    else:
		        self.communication.send_msg("Please insert correct values, example: b2")
		        choice = str(self.communication.receiving_msg()["msg"])

		while secondary_status:

			if choice[0] in "abcdefgh" and 0 < int(choice[1]) < 9:
				secondary_status = False
			else:
				self.communication.send_msg("Please insert correct values, example: b2")
				choice = str(self.communication.receiving_msg()["msg"])

		# first position
		from_list.append(8 - int(choice[1]))

		# second position
		second_position = ord(choice[0]) - 97

		# second position
		from_list.append(second_position)		

		return from_list


	def user_move_to(self):
		"""
	    user_move_to function:

	    Sending coordinates for figure where to move

	    Attributes:
	    	to_list: initially empty coordinates list
	    	choice: user's input
	    	first_position: first coordinate for board
	    	second_position: second coordinate for board

	    Returns:
	    ----------
	    	Returns to_list with coordinates 
		"""

		second_position = None

		to_list = []

		self.communication.send_msg("Where to? (example=b2)")

		loop_status = True

		secondary_status = True

		choice = str(self.communication.receiving_msg()["msg"])

		while loop_status:

		    if len(choice) == 2 and choice[1].isnumeric() and choice[0].isalpha() and choice[1] != 0:
		        loop_status = False
		    else:
		        self.communication.send_msg("Please insert correct values, example: b2")
		        choice = str(self.communication.receiving_msg()["msg"])

		while secondary_status:

			if choice[0] in "abcdefgh" and 0 < int(choice[1]) < 9:
				secondary_status = False
			else:
				self.communication.send_msg("Please insert correct values, example: b2")
				choice = str(self.communication.receiving_msg()["msg"])

		# first position
		to_list.append(8 - int(choice[1]))

		# second position
		second_position = ord(choice[0]) - 97

		# second position
		to_list.append(second_position)		

		return to_list
		

	def user_figure_check(self):
		"""
	    user_figure_check function:

	    Function checks if there are eaten figures
	    in user's list and deletes them

	    Attributes:
	    	user_figures: user figures list
	     
		"""

		for figure in self.user_figures:
			if figure.figure_status != False:
				continue
			else:
				del figure
				break




class UserCommunication:
	"""
    A class used to communicate user with server using client
    ...

    Attributes
    ----------
    socket: str
        socket attribute for connection

    Methods
    -------
    send_msg:
        sending messages function
    receiving_msg:
		receiving messages function
    """

    def __init__(self, socket):
    	"""
        Parameters
        ----------
        socket: socket connection parameter
        """

        # saving the socket inside the class
        self.socket = socket

    def send_msg(self, msg):
    	"""
	    send_msg function:

	    Function encodes and sends message

	    Attributes:
	    	message: message from json file
	    	send_length: refilled with neccesary bytes length
	    Args:
	    	msg: message argument  
		"""

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

    def receiving_msg(self):
    	"""
	    receiving_msg function:

	    Function decodes and receives message

	    Attributes:
	    	msg_length: message from json file in length
	    	main_msg: decoded msg
	    Args:
	    	msg: message argument    

	    Returns:
	    	Returns message as as dictionary 
		"""

        msg_length = self.socket.recv(128).decode("utf-8")

        if msg_length:
            # reformatting it into an integer
            msg_length = int(msg_length)
            # telling how many bites are we going to receive with the message
            main_msg = self.socket.recv(msg_length).decode("utf-8")
            dict_msg = json.loads(main_msg)

            return dict_msg

