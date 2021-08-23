Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> import string
>>> id=''
>>> characters_list=list(string.ascii_letters+string.digits)
>>> for i in range(6):
	id+=random.choice(characters_list)
	print(id)