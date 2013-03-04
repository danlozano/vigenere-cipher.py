"""
Daniel Lozano Valdes
10/1/2012
"""

# Import the 'filecmp' module for file comparison.
import filecmp

# Create the hard-coded key for the encryption, and convert to a list of chars for subscriptable access to the chars.
key = 'johny'
keyLength = len(key)
keyList = list(key)

# Options: Encrypt = 0, Decrypt = 1
def crypter(inputFileName, outputFileName, option):

	# This index value is used to know which char of the key to use to encrpyt or decrypt.
	i = 0

	# Open both files.
	inputFile = open(inputFileName, 'r')
	outputFile = open(outputFileName, 'w')

	# Loop until break statement is reached at end of file.
	while True:
		# Read one character from input file.
		c = inputFile.read(1)
		if not c:
			# End of File
			break
		if c.isalpha():
			# If char is a letter, then decrypt or encrypt.
			if i == keyLength:		# If the index used for the key has reached the end, loop back to 0.
				i = 0
			# Rotation is the number that will determine how much the char will be 'rotated'
			rotation = ord(keyList[i].upper())-ord('A')
			# If we are decrypting, then the rotation will be negative.
			if option == 1: rotation = rotation * -1
			i += 1
			# The char 'c' is rotated, or de/en-crpyted.
			ec = chr(((ord(c.upper()) - ord('A')) + rotation) % 26 + ord('A'))
			# The en/de-crypted char is writen to the output file. If it was originally lower case it is reconverted into lower case to mantain upper/lower case integrity.
			outputFile.write(ec if c.isupper() else ec.lower())
		else:
			# If char is not a letter then copy it as-is to the output file. 
			outputFile.write(c)

	# Close both files.
	inputFile.close()
	outputFile.close()


crypter('input.txt','encrypted.txt',0)	# Encrypt file.
crypter('encrypted.txt','decrypted.txt',1)	# Decrypth file.
print(filecmp.cmp('input.txt','decrypted.txt'))	   # Compare original & decrpyted file. 
