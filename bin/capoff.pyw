from base64 import b64decode as b64d, b64encode as b64e
import datetime
import os
import random
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
global states


	# Dictionaries containing the testing material on the 50 United States - North American Capital Cities & State Nicknames.
capitals = {'Alaska': 'Jueno', 'Alabama': 'Montgomery', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne',}

nicknames = {'Alabama': 'Yellowhammer State', 'Alaska': 'The Last Frontier', 'Arizona': 'Grand Canyon State', 'Arkansas': 'Natural State', 'California': 'Golden State', 'Colorado': 'Centennial State', 'Connecticut': 'Constitution State', 'Delaware': 'First State', 'Florida': 'Sunshine State', 'Georgia': 'Peach State', 'Hawaii': 'Aloha State', 'Idaho': 'Gem State', 'Illinois': 'Prairie State', 'Indiana': 'Hoosier State', 'Iowa': 'Hawkeye State', 'Kansas': 'Sunflower State', 'Kentucky': 'Bluegrass State', 'Louisiana': 'Pelican State', 'Maine': 'Pine Tree State', 'Maryland': 'Old Line State', 'Massachusetts': 'Bay State', 'Michigan': 'Great Lakes State', 'Minnesota': 'North Star State', 'Mississippi': 'Magnolia State', 'Missouri': 'Show Me State', 'Montana': 'Treasure State', 'Nebraska': 'Cornhusker State', 'Nevada': 'Silver State', 'New Hampshire': 'Granite State', 'New Jersey': 'Garden State', 'New Mexico': 'The Land of Enchantment', 'New York': 'Empire State', 'North Carolina': 'Tar Heel State', 'North Dakota': 'Peace Garden State', 'Ohio': 'Buckeye State', 'Oklahoma': 'Sooner State', 'Oregon': 'Beaver State', 'Pennsylvania': 'Keystone State', 'Rhode Island': 'Ocean State', 'South Carolina': 'Palmetto State', 'South Dakota': 'Mount Rushmore State', 'Tennessee': 'Volunteer State', 'Texas': 'Lone Star State', 'Utah': 'Beehive State', 'Vermont': 'Green Mountain State', 'Virginia': 'Old Dominion', 'Washington': 'Evergreen State', 'West Virginia': 'Mountain State', 'Wisconsin': 'Badger State', 'Wyoming': 'Equality State',}

states = list(capitals.keys())


class Login(tk.Tk):
	def __init__(self, *args, **kwargs):
		'''Small Tkinter.Tk() instance that requires a username and a decision on which quiz to start - State Capitals or State Nicknames. 
		Once satisfied, this window is destroyed and the Main/Root Tkinter.Tk() is called to conduct the testing.'''
		super().__init__(*args, **kwargs)
		self.title('Capital Offense - Login')
		self.iconbitmap(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' + '\\assets\\login.ico')))
		self.geometry('350x250')
		self.resizable(False, False)
	# Username authentication can be implemented for certain userbases - the same goes for incorporation of password requirements.
		self.userfile = os.path.abspath(os.path.join(os.path.dirname(__file__), '..' + '\\docs\\userstats.dat'))
		self.username = tk.StringVar()
		self.choice = tk.IntVar()
		self.bind('<Return>', func=self.check)
	# Widget creation - buttons, text boxes, etc.
		log_fram = tk.Frame(self, padx=10, pady=10, width=10)
		user_lbl = tk.Label(self, anchor='w', justify='left', padx=25, pady=15, text='Enter Username: ')
		user_ent = tk.Entry(self, textvariable=self.username, width=18, takefocus=True)
		ent_bttn = tk.Button(self, anchor='center', command=self.check, padx=15, text='Login')
		ext_bttn = tk.Button(self, anchor='center', command=quit, padx=15, text='Quit')
		spac_lbl = tk.Label(self, justify='center', padx=10, pady=10, width=10)
		cap_radi = tk.Radiobutton(self,  justify='center', padx=15, text='State Capitals', value=0, variable=self.choice)
		nic_radi = tk.Radiobutton(self, justify='center', padx=15, text='State Nicknames', value=1, variable=self.choice)
	# Geographic placement of widgets within the GUI window - using grid, obviously :P
		log_fram.grid(column=0, row=0, ipadx=10, ipady=10, padx=10, pady=10, sticky=tk.N)
		user_lbl.grid(column=0, row=0, padx=10, pady=20, sticky=tk.E)
		user_ent.grid(column=1, row=0, padx=10, pady=20, sticky=tk.W)
		ent_bttn.grid(column=0, row=4, ipadx=6, padx=20, pady=15, sticky=tk.E)
		ext_bttn.grid(column=1, row=4, ipadx=8, padx=20, pady=15, sticky=tk.W)
		spac_lbl.grid(column=0, row=2, padx=10, sticky=tk.N)
		cap_radi.grid(column=0, row=3, padx=10, pady=10, sticky=tk.S)
		nic_radi.grid(column=1, row=3, padx=10, pady=10, sticky=tk.S)


	# While no user authorization takes place, a few constraints are still enforced - with efforts mainly focused on filtering inappropriate or vulgar words, terms, and symbols.
	def check(self, key=None):
		cenfile = os.path.abspath(os.path.join(os.path.dirname(__file__), '..' + '\\docs\\cens.dat'))
		with open(cenfile, 'rb') as cens:
			data = cens.read()
		data = b64d(data)
		vulgar = data.decode()

	# Decode the base64 encoded blacklist of profanity containing nearly 3,000 curse words. If user's name contains any term within said list, it is rejected.
		username = self.username.get().strip().title()
		choice = self.choice.get()
		
		if len(username) <= 2:
			messagebox.showerror(title='Name Too Short', message='Username must contain at least 3 characters. Please choose another name.')
			self.username.set('')
			return
		elif username.lower() in vulgar:
			messagebox.showerror(title='Inappropriate Username', message='Name contains a vulgar, inappropriate, or unacceptable word. Please choose another name.')
			self.username.set('')
			return
		else:
			confirm = messagebox.askyesno(title='Confirm Name', message='You entered ' + username + ' as your name. Is this correct?')

		if confirm is True:
			self.destroy()
			MainWin(username, str(choice)).mainloop()
		else:
			self.username.set('')
			return


class MainWin(tk.Tk):
	def __init__(self, name, choice):
		'''Main window that displays randomized quiz questions and awaits user input as the answer.
		 Username and score are recorded to encoded file for progress monitoring.'''
		super().__init__(name, choice)
		self.grid_rowconfigure(1, pad=1, weight=2)
		self.grid_rowconfigure(4, pad=1, weight=2)
		self.title('Capital Offense - Earn Your Citizenship!')
		self.iconbitmap(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' + '\\assets\\northamerica.ico')))
		self.geometry('450x275')
		self.resizable(False, False)
		self.lift()
		self.focus_set()
		
	# Declaration of all necessary variables.
		self.score = 0
		self.username = name
		self.choice = choice
		self.start = datetime.datetime.now()
		self.userfile = os.path.abspath(os.path.join(os.path.dirname(__file__), '..' + '\\docs\\userstats.dat'))

	# Text variables and event bindings.
		self.ask = tk.StringVar()
		self.res = tk.StringVar()
		self.answer = tk.StringVar()
		self.bind('<Return>', func=self.submit)
		self.bind('<Alt-F4>', func=self.exit)

	# Creation, Setup, and configuration of the window's widgets - text boxes, buttons, etc.
		quiz_frame = tk.LabelFrame(self, bd=3, labelanchor='n', padx=45, pady=20, text="Are You a Real 'Merican?", width=10)
		bttn_frame = tk.Frame(self, padx=20, pady=20, height=2, width=15)
		quiz_lbl = tk.Label(quiz_frame, anchor='w', justify='left', pady=15, textvariable=self.ask)
		quiz_ent = tk.Entry(quiz_frame, takefocus=True, textvariable=self.answer, width=18)
		rest_lbl = tk.Label(self, anchor='center', justify='center', padx=15, pady=15, textvariable=self.res)
		spac_lbl = tk.Label(self, anchor='center', justify='center', padx=15)
		ent_bttn = tk.Button(bttn_frame, anchor='center', padx=10, text='Enter', command=self.submit)
		ext_bttn = tk.Button(bttn_frame, anchor='center', padx=10, text='Quit', command=quit)

	# Geometrical placement of each widget within the main window.
		quiz_frame.grid(column=0, row=0, ipadx=10, ipady=10, padx=30, sticky=tk.N)
		bttn_frame.grid(column=0, row=4, ipadx=10, ipady=10, padx=10, pady=10, sticky=tk.S)
		rest_lbl.grid(column=0, row=1, padx=10, pady=10, sticky=(tk.W + tk.E))
		spac_lbl.grid(column=1, row=2, sticky=tk.S)
		quiz_lbl.grid(column=0, row=0, sticky=tk.W)
		quiz_ent.grid(column=2, row=0, sticky=tk.E)
		ent_bttn.grid(column=0, row=4, columnspan=2, rowspan=2, ipadx=8, padx=50, sticky=tk.NW)
		ext_bttn.grid(column=3, row=4, columnspan=2, rowspan=2, ipadx=8, padx=50, sticky=tk.NE)

		self.quiz()

	def quiz(self):
		global states
	# Question generator - picks a state at random and sets the question depending on testing - Capitals or Nicknames.
		while len(states) >= 1:
			self.state = random.choice(states)
			states.pop(states.index(self.state))

			self.ask.set('')
			self.answer.set('')

			if int(self.choice) == 0:
				self.correct = capitals.get(self.state)
				self.ask.set('The Capital of ' + self.state + ' is: ')
				return
			elif int(self.choice) == 1:
				self.correct = nicknames.get(self.state)
				self.ask.set(self.state + "'s State Nickname: ")
				return
			else:
				assert False, ('This condition should never happen, however '
							  'if you see this error, contact joetrex@gmail.com '
							  'This is an Assertion Exception with radio button choice.')

		self.finish()

	def submit(self, key=None):	
		# Where user input slams into a wall of code... the input judgement day! Accept or reject, pass or fail, zero or one, on or off... RIGHT OR WRONG?! All answered here. 
			affirm = ['correct!', 'absolutely right!', '100% right!', 'exactly it!', 'on the money!', 'totally right!', 'exactly right!', 'incorrect... PSYCH! CORRECT AGAIN!',]
			answer = self.answer.get().strip().title()

			if answer == '' or answer == None:
				self.res.set('Answer is Blank. Take Your Best Guess if Necessary.')
				return
			elif answer == self.correct:
				pep = random.choice(affirm)
				self.score += 10
				self.res.set(str(self.correct) + ' is ' + pep + ' Score 10 Points!')
				self.quiz()
			elif answer[0:5] == str(self.correct)[0:5]:
				self.score += 5
				self.res.set('Partial Credit. Score 5 Points...' + ' it\'s ' + str(self.correct) + ' not ' + answer + '. Watch Your Spelling!')
				self.quiz()
			elif len(answer) < 3:
				self.res.set('Assuming the ENTER button was pressed by mistake... still waiting for your answer.')
				return
			elif answer.isnumeric():
				self.res.set('Since the answer can never be numbers, testing will wait on your REAL answer.')
				return
			else:
				self.res.set('Sorry, Incorrect. The correct answer for ' + self.state + ' is ' + str(self.correct) + '. No Points Awarded.')
				self.quiz()
	

	def finish(self):
		'''Once the test is complete, final score is displayed with developer's original 'ranking' status message - customize these messages to suit your standards.
			For instance, certain userbases may require a more professional and/or more formal presentation - some config scripts are provided in the docs folder with basic/typical terminology.'''

	# Calculate time taken to complete the test.
		self.end = datetime.datetime.now()
		self.testime = self.start - self.end
		minutes = round(self.testime.seconds / 60)

		if minutes < 120:
			self.testime = str(minutes) + ' Minutes  |  '
		elif minutes >= 120 and self.testime.days == 0:
			self.testime = round(minutes / 60)
			self.testime = str(self.testime) + ' Hours  |  '
		elif self.testime.days > 0:
			self.testime = 'Over 24 Hours - Assumed as User Didn\'t Log Off System.'
		else:
			self.testime = 'Something went wrong calculating test time for this user...'

	# Display final score and status message.
		self.res.set('Testing Complete! Final Score: ' + str(self.score))
		if self.score == 500:
			messagebox.showinfo(title='A Perfect Score?', message='Potential Use of Unauthorized Resources - N.S.A. is currently investigating possible use of a mobile device or other internet capable interface. Citizenship is pending the conclusion of said investigation!')
			self.recdata()
		elif self.score >= 400 and self.score < 500:
			messagebox.showinfo(title='Made America Great Again', message='The POTUS commends you and will send a letter of recognition. You\'re a model American, true Red, White, and Blue!')
			self.recdata()
		elif self.score >= 300 and self.score < 400:
			messagebox.showinfo(title='Average American', message='You scored in the sweet spot - the national average - perfectly acceptable and high enough to ensure your lasting American citizenship. Congrats.')
			self.recdata()
		elif self.score >= 200 and self.score < 300:
			messagebox.showinfo(title='Questionable Citizen', message='Scoring below average may cause your name to be flagged, triggering N.S.A. surveillance of your daily activities and other personal information. Have a nice day!')
			self.recdata()
		elif self.score >= 100 and self.score < 200:
			messagebox.showinfo(title='I.C.E. Notified', message='You have been sanctioned for deportation. Immigration and Customs Enforcement have been dispatched to your location. By default, you will be sent to Guantanamo Bay. Have a nice day!')
			self.recdata()
		else:
			messagebox.showinfo(title='Espionage / Treason Charges', message='Deportation is not an option until an investigation is conducted to determine whether you stand to face Grand Treason and/or Espionage - a Capital Offense! LOL Good luck!')
			self.recdata()



	def recdata(self):
		'''Originally was part of the self.final() function but was separated due to user data not being written to the user file correctly. 
			This records all user data and stats and is encoded to prevent testers from manipulating and/or altering the accurate information.'''
		if int(self.choice) == 0:
			test = 'State Capitals'
		elif int(self.choice) == 1:
			test = 'State Nicknames'
		else:
			assert False, (
				'This condition should never happen, however '
				'if you see this error, contact joetrex@gmail.com '
				'This is an Assertion Exception with radio button choice.'
				)

	# Record user statistics including login time, total testing time, final score, and user history - if any - useful in tracking a user's progress and/or improvement.
		userdata = 'Timestamp: ' + str(self.start) + '\n' + '==============================================' + 'User: ' + self.username + ' logged in and began the ' + test + ' quiz.\n'
		userprof = 'Completion Time: ' + str(self.end) + '  |  Total Testing Time: ' +  str(self.testime) + '  |  Resulting Final Score: ' + str(self.score) + ' out of a possible 500.' 
		userlog = userdata + userprof

		userdata = userdata.encode()
		prof = userprof.encode()
		userlog = userlog.encode()
		
		user = b64e(userdata)
		prof = b64e(prof)
		log = b64e(userlog)
		
		with open(self.userfile, 'ab') as rec:
			rec.write(user)
			rec.write(prof)
			rec.write(log)
		
		self.gameover()



	def gameover(self):
	# Yes/No choice to test again or quit - the potential for a higher score does not replace the previous test's score. Logs are still written for insight into user progress.'
		again = messagebox.askyesno(title='Try Again?', message='Do you want to re-test for a chance at a better score?')
		if again is True:
			self.quit()
			self.destroy()
			Login().mainloop()
		elif again is False:
			self.quit()
			self.destroy()
		else:
			assert False, (
				'True or False / Yes or No are the only options'
				'This error should never occur, though if it does'
				'please email joetrex@gmail.com to inform.'
				)
			

	# It never fails ... for years, 'pranksters' try to trick their less tech-savvy peers by telling them ALT+F4 does something amazing. Imagine answering #49 then ALT+F4...
	def exit(self, key=None):
		'''Event driven bound to the ALT+F4 key combination - confirming the intention to exit the program
			rather than automatically closing it with no prompt or confirmation.'''

		leave = messagebox.askyesno(title='Confirm Exiting App', message='Do you want to exit and quit?')
		if leave is True:
			self.quit()
			self.destroy()
		else:
			return


if __name__ == '__main__':
	login = Login()
	login.mainloop()
