import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class User:

	def __init__(self, win_score=0, loss_score=0, users_config)

		self.users_config = users_config
		self.win_score = score
		self.lose_score
		self.user_figures = []


	def registration(self):		

		# user's nickname attribute
		self.nickname = input("Please enter your nickname: ")
		# user's client password attribute
		self.password = input("Please enter your password: ")

		# user's email address password
		self.email_address = input("Enter your email address to send you a password for registration: ")


		while True:

			# the password
			self.random = ""
			for i in range(0,6):
				n = random.randint(0,10)

			self.random += str(n)

			self.registration_code_sender()

			self.user_code_input = str(input("Please enter the password here: "))

			if self.user_code_input == self.random:

				print("Registration success! \n" \
					"Hi {self.nickname}!")

				break

			else:
				print("The password was wrong, We can send another password")
				print("If you want new password, type `y` \n" \
				 "if you wan't to cancel registration, enter `!exit!`")
				while True:
					self.user_choice_input = input("Your choice: ")

					if self.user_choice_input == "!exit":
						print("Goodbye!")
						break
					elif self.user_choice_input == "y":
						self.random = ""
						continue
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
				"Please don't answer to this email." \
				"Best regards!" \
				"Chessgameregistration team"

		self.msg.attach(MIMEText(self.text, "plain"))

		self.main_msg = self.msg.as_string()

		self.server.sendmail("chessgameregistration@mail.ru", self.email_address, self.main_msg)
		print(f"Mail sended to {self.email_address}")

		self.server.close()