## Turning loops to list comprehensions

You can skip this step if you like as you are only going to re-factor your code. If you don't want to play with comprehensions, just move down to the next section. Otherwise, read on!

At the moment you have a three loops all producing data structures such as lists and dictionaries.

There's another way of producing these, though, using list and dictionary comprehensions.

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

1.  You can use either of your `get_matching` functions, but remember to comment out the one you don't use.
