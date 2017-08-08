## Getting some random nouns

1.  You can get some random nouns by shuffling the list of nouns, and then popping off the end of the list inside a loop.

	```python
	rand_nouns = []
	shuffle(nouns)
	for item in range(items):
		rand_nouns.append(nouns.pop())
	```
