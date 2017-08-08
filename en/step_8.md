## Pairing verbs and nouns

In The Twelve Days of Christmas, the verbs and nouns are often alliterative, which means they share the same first letter:

-   Swans a Swimming
-   Maids a Milking
-   Lords a Leaping
-   Pipers Piping
-   Drummers Drumming

In your version of the song, nouns and verbs will always be alliterative, so you're going to need to build up a dictionary of nouns, with corresponding verbs that share the same letter.

1.  You can start by creating an empty dictionary inside the `get_matching()` function:

	```python
	matching = {}
	```

1.  Next you want to iterate through the random nouns you have selected, and add each one to the dictionary as a key, with an empty list as its value.

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
