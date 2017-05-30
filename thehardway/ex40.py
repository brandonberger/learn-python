class Song(object): # def class
	def __init__(self, lyrics): # def magic function called on init, passes class (self) and lyrics list
		self.lyrics = lyrics # asigns class variable to lyrics list passed

	def sing_me_a_song(self): # defines function passing class self
		for line in self.lyrics: # for each line in class lyrics var
			print line # print line

# inits Song class passing happybirthday lyrics
happy_bday = Song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"])

# inits SOng class passing ram lyrics
bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])
# calls function on instance of happybirthdya
happy_bday.sing_me_a_song()

# calls function on instance of RAM
bulls_on_parade.sing_me_a_song()