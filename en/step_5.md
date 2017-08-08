## Importing the words

1.  Open Python 3 (IDLE) and create a new file called `christmas.py`. Save it in your `n-day` directory.
2.  To make the song as interesting as possible, you're going to need to randomly pick words. So at the top of your file, you can import the `choice` function from the `random` module.

	```python
	from random import choice
	```

1.  Next, you can create a function which will allow you to open text files.

  ```python
	def load_words(text_file):
		with open(text_file, 'r', encoding='utf8') as f:
			words = f.read()
		return words
  ```

1.  You can see what the first thirty characters in `words` contain by switching to the Python interpreter.

	```python
	words = load_words('nouns.txt') 
	words[0:30]
	```

1.  This isn't much use to you, but you can convert the long string into a list by using `splitlines()`. Edit your file so it looks like this:

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

1.  Now `words` consists of a list of words, the string having been broken up at every `newline`.
