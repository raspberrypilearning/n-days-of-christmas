The N Days Of Christmas
=======================

We all love Christmas, and what we love the most is Christmas songs. Unfortunately, most Christmas songs just don't go on for long enough. Songs like **The Twelve Days of Christmas** would be so much better if you they could be stretched out a little longer. How about **The Fifty Days of Christmas**, **The Hundred Days of Christmas**, or even **The Thousand Days of Christmas**!.

In this resource, you'll be creating a Python script to produce the lyrics to **The N Days of Christmas** where N is any number you want it to be. That way, when you go out carol singing, you only need to remember the lyrics to one, very long, song.

Getting the text files.
-----------------------

In the 12 Days of Christmas, the lyrics follow a general trend of:

- 12 nouns a doing
- 11 nouns a doing
- 10 nouns a doing

To create your program you're going to need a long list of nouns and a long list of verbs.

1.  Create a new directory called `n-days`, to save both the files in
2.  The **nouns.txt** file can be downloaded [here](...)
3.  The **words.txt** file can be downloaded [here](...)

Importing the words
-------------------

1.  Open Python 3 (IDLE) and create a new file called `christmas.py`. Save it in your `n-day` directory.
2.  To make the song as interesting as possible, you're going to need to randomly pick words. So at the top of your file, you can import the `choice` function from the `random` module.

	```python
	from random import choice
	```

1.  Next you can create function that will allow you to open text files.

  ```python
	def load_words(text_file):
		with open(text_file, 'r', encoding='utf8') as f:
			words = f.read()
		return words
  ```

1.  You can see what the first thirty characters in `words` contains by switching to the Python interpreter.

	```python
	words = load_words('nouns.txt') 
	words[0:30]
	```

1.  This isn't much use to you, but you can convert the long string, into a list by using `splitlines()`. Edit your file so it looks like this:

  ```python
	def load_words(text_file):
		with open(text_file, 'r', encoding='utf8') as f:
			words = f.read().splitlines()
		return words
  ```

1.  Save and run your file, then switch back to the interpreter and have a look at `words` now.

	```python
	words = load_words('nouns.txt') 
	words[0:30]
	```

1.  Now `words` consists of a list of words, the string having been broken up at every *newline*.

Getting all the verbs and nouns
-------------------------------

Getting all the nouns is easy, as you can just pass the `nouns.txt` into your `load_words` function. The verbs is a little trickier, they're in `words.txt` somewhere, but you're going to have to find them.

1.  To start with you can load the words up into two separate list, and create an empty list, ready to store your verbs.

  ```python
	def get_matching(items):
		nouns = load_words('nouns.txt')
		words = load_words('words.txt')
		verbs = []
  ```

1.  You can get all the verbs by finding words that end in `ing`. A little bit of string slicing can help you get this. Switch over to the Interpreter and try out the following.

1.  This gets you the first character of the string `Hello`.

	```python
	'Hello'[0]
	```

1.  To get the first three characters you could type:

	```python
	'Hello'[0:3]
	```

1.  Or even just:

	```python
	'Hello'[:3]
	```

1.  To get the last character you could type:

	```python
	'Hello'[-1]
	```

1.  And to get the last three characters you can type:

	```python
	'Hello'[-3::]
	```

1.  This technique can be used to check if a word ends in `ing` and if it does, you can add it to your list of verbs.

	```python
	def get_matching(items):
		nouns = load_words('nouns.txt')
		words = load_words('words.txt')

		verbs = []
		for word in words:
			if word[-3::] == 'ing':
				verbs.append(word)
	```

Getting some random nouns
-------------------------

1.  You can get some random nouns by shuffling the list of nouns, and then popping off the end of the list inside a loop.

	```python
	rand_nouns = []
	shuffle(nouns)
	for item in range(items):
		rand_nouns.append(nouns.pop())
	```

Pairing verbs and nouns.
------------------------

In *The 12 Days of Christmas* song the verbs and nouns often share the same first letter:

-   Swans a Swimming
-   Maids a Milking
-   Lords a Leaping
-   Pipers Piping
-   Drummers Drumming

In your version of the song, they'll always share the same first letter, so you're going to need to build up a dictionary of nouns, with corresponding verbs that share the same letter.

1.  You can start by creating an empty dictionary inside the `get_matching()` function:

	```python
	matching = {}
	```

1.  Next you want to iterate through the random nouns you have selected, and add each one to the dictionary as a *key*, with an empty list as it's *value*.

  ```python
	for noun in rand_nouns:
		matching[noun] = []
  ```

1.  Still within that loop, you can iterate through all the verbs, and if the first character of the verb is the same as the first character of the noun, you can add them to the list for that noun.

	```python
	  for verb in verbs:
		  if verb[0].upper() == noun[0].upper():
			  matching[noun].append(verb)
	```

1.  Finally you want to `return` the `matching` dictionary.
2.  Your whole function should now look like this:

  ```python
	def get_matching(items):
		nouns = load_words('nouns.txt')
		words = load_words('words.txt')

		verbs = []
		for word in words:
			if word[-3::] == 'ing':
				verbs.append(word)

	  rand_nouns = []
	  shuffle(nouns)
	  for item in range(items):
		  rand_nouns.append(nouns.pop())

		matching = {}
		for noun in rand_nouns:
			matching[noun] = []
			for verb in verbs:
				if verb[0].upper() == noun[0].upper():
					matching[noun].append(verb)

		return matching
  ```

1.  Save and run the code, then switch over to the interpreter and test it out.

	```python
	>>> matching = get_matching(12)
	>>> matching.keys()
	```

Turning loops to list comprehensions
------------------------------------

You can skip this step if you like as you are only going to re-factor your code. Jump down to the next section, if you don't want to play with *comprehensions*.

At the moment you have a three loops all producing data structures such as lists and dictionaries.

There's another way of producing these however, using list and dictionary comprehensions.

1.  These four lines of code:

	```python
	verbs = []                
	for word in words:        
		if word[-3::] == 'ing':
			verbs.append(word) 
	```

	can be condensed down to:

	```python
	verbs = [word for word in words if word[-3::] == 'ing']
	```

1.  These lines of code:

	```python
	rand_nouns = []                     
	for item in range(items):           
		rand_nouns.append(choice(nouns))
	```

	can be condensed down to

	```python
	rand_nouns = []
	shuffle(nouns)
	for item in range(items):
		rand_nouns.append(nouns.pop())
	```

1.  Lastly, the following code:

	```python
	  matching = {}                                 
	  for noun in rand_nouns:                       
		  matching[noun] = []                       
		  for verb in verbs:                        
			  if verb[0].upper() == noun[0].upper():
				  matching[noun].append(verb)
	```

	can be condensed down to:

	```python
	matching = {rand_nouns[item]:[verb for verb in verbs if verb[0].upper() == rand_nouns[item][0].upper()] for item in range(items)}
	```

1.  Your function should now look like:

	```python
	def get_matching(items):
		nouns = load_words('nouns.txt')
		words = load_words('words.txt')
		verbs = [word for word in words if word[-3::] == 'ing']
		shuffle(nouns)
		rand_nouns = [nouns.pop() for item in range(items)]
		matching = {rand_nouns[item]:[verb for verb in verbs if verb[0].upper() == rand_nouns[item][0].upper()] for item in range(items)}
		return matching
	```

1.  You can use either of your `get_matching` functions, just remember to comment out the one you don't use.

Getting suffixes for numerals
-----------------------------

The first line of the song changes, depending on the number of days. You might have:

*On the 3rd day of Christmas...*

**or**

*On the 8th day of Christmas...*

with the *suffix* on the number changing between **st**, **nd**, **rd** and **th**

You can create a new function to handle this.

1.  Define a new function called `get_suffix`.

	```python
	def get_suffix(num):
	```

1.  A dictionary would be a useful way of storing the suffixes.

	```python
	def get_suffix(num):
		endings = {1:'st',2:'nd',3:'rd',4:'th'}
	```

1.  With a clever bit of maths, we can find out the suffix for any number. The rules are:

-   If the number is between 10 and 20 then the suffix is **th**, or...
-   If the last digit of the number is greater than 3, then the suffix is **th**, or...
-   If the last digit of the number is 0, then the suffix is **th**, or...
-   If the number ends in 1, 2, or 3 the suffix is **st**, **nd** and **rd**, respectively.

1.  So how do you get the last digit of a number? You can use a handy operator called *modulo*, that finds the remainder after a division. In Python you use the symbol `%`

2.  Try this in the interpreter to get the remainder of dividing by 2

	```python
	12 % 2
	11 % 2
	```

1.  Or to get the remainder of dividing by 5

	```python
	15 % 5
	14 % 5
	```

1.  Now see what happens when you find the remainder of division by 10

	```python
	20 % 10
	12 % 10
	6 % 10
	```

1.  You always get the last digit of the number. Go back to your `get_suffix` function, and you can code up the rules stated above.

	```python
	def get_suffix(num):
		endings = {1:'st',2:'nd',3:'rd',4:'th'}
		if 10 < num < 20 or num % 10 > 3 or num % 10 == 0:
			return 'th'
		else:
			return endings[num%10]
	```

Printing the whole song
-----------------------

The last step is to actually print your song

1.  Create a new function that takes the number of `days` in the song as an argument.

	```python
	def display_song(days):
	```

1.  You're going to keep the last five lines of the traditional song as they are, so the number of noun:verb pairs you will need is 5 less than the number of days.

	```python
	def display_song(days):
		matching = get_matching(days-5)
	```

1.  Now you can print the first line, including the correct suffix.

	```python
	def display_song(days):
		matching = get_matching(days-5)
		print('On the', str(days) + get_suffix(days), 'day of Christmas, my true love sent to me')
	```

1.  Next you want to to get a list of all the nouns in the `matching` dictionary.

	```python
	def display_song(days):
		matching = get_matching(days-5)
		print('On the', str(days) + get_suffix(days), 'day of Christmas, my true love sent to me')
		nouns = list(matching.keys())
	```

1.  You can iterate over this list, and so long as the day is greater than 5, you can print off matching noun and verb pairs. If the day hits 5, then the loop can break. Because there are 5 less nouns and verbs that *days of Christmas* and lists are indexed from 0, you'll need to subtract 6 from `days` to get the correct index.

	```python
	def display_song(days):
		matching = get_matching(days-5)

		print('On the', str(days) + get_suffix(days), 'day of Christmas, my true love sent to me')

		nouns = list(matching.keys())
		for day in range(days,0,-1):
			if day  <= 5:
				break
			else:
				print(day, nouns[day-6]+'s', 'a', choice(matching[nouns[day-6]]))
	```

1.  To finish off the function, you can print off the standard end to the song. The function should look like this:

	```python
	def get_suffix(num):
		endings = {1:'st',2:'nd',3:'rd',4:'th'}
		if 10 < num < 20 or num % 10 > 3 or num % 10 == 0:
			return 'th'
		else:
			return endings[num%10]

	def display_song(days):
		matching = get_matching(days-5)

		print('On the', str(days) + get_suffix(days), 'day of Christmas, my true love sent to me')

		nouns = list(matching.keys())
		for day in range(days,0,-1):
			if day  <= 5:
				break
			else:
				print(day, nouns[day-6]+'s', 'a', choice(matching[nouns[day-6]]))
		print('5 Gold rings')
		print('4 Calling birds')
		print('3 French hens')
		print('2 Turtle Doves')
		print('and a Partridge in a pair tree')
	```

1.  To finish off the song, you can ask the user for the number of days, and then run the `display_song` function.

	```python
	days = int(input('How many days of Christmas are there?'))
	display_song(days)
	```

1.  Run your code, and type in the total number of days you want to use. (There are only 2120 words in `nouns.txt` so that is the limit.)

