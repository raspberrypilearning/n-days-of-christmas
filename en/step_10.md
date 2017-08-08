## Getting suffixes for numerals

How do we deal with numbers in our program? Remember that the first line of the song changes, depending on which day we begin with. You might have:

'On the third day of Christmas...'

**or**

'On the eighth day of Christmas...'

with the suffix on the number changing between **-st**, **-nd**, **-rd** and **-th**

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

-   If the number is between 10 and 20 then the suffix is **-th**, or...
-   If the last digit of the number is greater than 3, then the suffix is **-th**, or...
-   If the last digit of the number is 0, then the suffix is **-th**, or...
-   If the number ends in 1, 2, or 3 the suffix is **-st**, **-nd** and **-rd**, respectively.

1.  So how do you get the last digit of a number? You can use a handy operator called **modulo**, which finds the remainder after a division. In Python you use the symbol `%`

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
