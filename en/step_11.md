## Printing the whole song

The last step is to actually print your song

1.  Create a new function that takes the number of `days` in the song as an argument.

	```python
	def display_song(days):
	```

1.  You're going to keep the last five lines of the traditional song as they are, so the number of noun:verb pairs you will need is five fewer than the number of days.

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

1.  You can iterate over this list, and so long as the number of the day is greater than five, you can print off matching noun and verb pairs. If the number of the day hits five, then the loop can break. Because there are five fewer nouns and verbs than there are 'days of Christmas', and because lists are indexed from zero, you'll need to subtract six from `days` to get the correct index.

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
