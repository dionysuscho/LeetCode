"""Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

def addBinary(a: str, b: str) -> str:
	"""
	Given two binary strings, return their sum (also a binary string).
	Input strings are both non-empty and contains only characters 1 or 0.

	>>> addBinary("1", "0")
	'1'
	>>> addBinary("11", "1")
	'100'
	>>> addBinary("1010", "1011")
	'10101'
	>>> addBinary("1111", "1111")
	'11110'
	"""
	# Base Case

	if len(a) < len(b):
		a, b = b, a

	if a == "":
		return ""
	if b == "":
		rem = int(a[max(0, len(a) - 1)])
	else:
		rem = int(a[max(0, len(a) - 1)]) + int(b[max(0, len(b) - 1)])

	if rem <= 1:
		return addBinary(a[:-1], b[:-1]) + str(rem)
	else:
		if len(a) > 1:
			new_a = a[:-2] + str(int(a[-2]) + 1)
			return addBinary(new_a, b[:-1]) + str(rem - 2)
		else:
			return "1" + str(rem - 2)


if __name__ == "__main__":
	import doctest
	doctest.testmod()
	print("*" * 20)
	print("doctests: done")
	print("*" * 20)
