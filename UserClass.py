import random
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class User: 

	def __init__(self, users_config, win_score=0, loss_score=0):

		self.users_config = users_config
		self.win_score = win_score
		self.lose_score = loss_score
		self.user_figures = []


	def registration(self):		

		# user's nickname attribute
		self.nickname = input("Please enter your nickname: ")
		# user's client password attribute
		self.password = input("Please enter your password: ")

		# user's email address password
		self.email_address = input("Enter your email address to send you a password for registration: ")

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
						self.loop_status = False
						print("Goodbye!")
						break
					elif self.user_choice_input == "y":
						self.random = ""
						break
					else:
						print("Please enter a valid choice")
						self.user_choice_input = input("Your choice: ")





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


	# user moving his figures from coordinates:
	def user_move_from(self):

		second_position = None

		from_list = []

		print("Which figure? (example=b2)")

		choice = str(input(": "))

	

		# second position
		if choice[0] == "a":
			second_position = 0
		elif choice[0] == "b":
			second_position = 1
		elif choice[0] == "c":
			second_position = 2
		elif choice[0] == "d":
			second_position = 3
		elif choice[0] == "e":
			second_position = 4
		elif choice[0] == "f":
			second_position = 5
		elif choice[0] == "g":
			second_position = 6
		elif choice[0] == "h":
			second_position = 7

		# first position
		from_list.append(8 - int(choice[1]))

		# second position
		from_list.append(second_position)		

		return from_list

	# user moving his figures to coordinates
	def user_move_to(self):
		second_position = None

		to_list = []

		print("Where? (example=b3)")

		choice = str(input(": "))

		# second position
		if choice[0] == "a":
			second_position = 0
		elif choice[0] == "b":
			second_position = 1
		elif choice[0] == "c":
			second_position = 2
		elif choice[0] == "d":
			second_position = 3
		elif choice[0] == "e":
			second_position = 4
		elif choice[0] == "f":
			second_position = 5
		elif choice[0] == "g":
			second_position = 6
		elif choice[0] == "h":
			second_position = 7

		# first position
		to_ist.append(8 - int(choice[1]))

		# second position
		to_list.append(second_position)		

		return to_list

	# checking the status for the figure
	# if it is false, we delete it from the list
	def user_figure_check(self):

		for figure in self.user_figures:
			if figure.status != False:
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