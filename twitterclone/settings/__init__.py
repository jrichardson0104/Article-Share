from .base import *


try:
	from .local import *
	live = False
except:
	live = True
	pass

if live:
	try:
		from .production import *
	except:
		pass
