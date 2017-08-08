## Getting all the verbs and nouns

Getting all the nouns is easy, as you can just pass the `nouns.txt` into your `load_words` function. The verbs are a little trickier: they're in `words.txt` somewhere, but you're going to have to find them.

1.  To start with you can load the words up into two separate lists and create an empty list, ready to store your verbs.

  ```python
	def get_matching(items):
		nouns = load_words('nouns.txt')
		words = load_words('words.txt')
		verbs = []
  ```

	You can locate all the verbs by finding words that end in '-ing'. A little bit of string slicing can help you here. Switch over to the interpreter and try out the examples outlined in the following steps.

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

1.  This technique can be used to check if a word ends in `ing`; if it does, you can add it to your list of verbs.

	```python
	def get_matching(items):
		nouns = load_words('nouns.txt')
		words = load_words('words.txt')

		verbs = []
		for word in words:
			if word[-3::] == 'ing':
				verbs.append(word)
	```
