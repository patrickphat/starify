# starify

Convert part of strings to asterisks to display confidential information
# Installation
```bash
pip install starify
```
# Usage:
```python
import starify

credential = "ABCDEFGHI_TH1SCR3D3ENTIAL"
starify.star(credential) 
# "***************TH1SCR3D3ENTIAL"
```
# Customization
With Starify you can change how the starring would be performed. 
```python
# Starify.star() by default parameter
starify.star(
	string,            	# Input your string here
	star_percent = 0.6,	# The portion of the string that will be starred
	star_head = True, 	# Star from head (True) or tail (False),
	max_len = 25, 		# Trim the string to max_len before starring,
)
```
For example

```python
string = "ABCDEFGHIJKLMNOP_123_QRSTUVWXYZ"

starify.star(string)
# '***************QRSTUVWXYZ'

starify.star(string, star_percent=0.8)
# '********************VWXYZ'

starify.star(string, star_percent=0.2)
# '*****LMNOP_123_QRSTUVWXYZ'

starify.star(string, star_percent=0.2, star_head=False)
# 'ABCDEFGHIJKLMNOP_123*****'

starify.star(string, star_percent=0.2, star_head=False, max_len=15)
# 'ABCDEFGHIJKL***'
```

```
