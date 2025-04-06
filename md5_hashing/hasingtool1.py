import hashlib
from hashlib import *
import os.path
import pathlib
from os import path



print("===============================================")
print("Cheking Hash [1]  > This option for checking the hash")
print("Hash length  [2]  > This option for length hash")
print("Hash Type    [3]  > This option for know the type of the hash")
print("MD5 Encrypt  [4]  > This option for text to md5")
print("MD5 Decrypt  [5]  > This option for decryption")
print("Exist        [6]  > To exist")
print("===============================================")
listx = input("choose one of list : ")
print("-----------------------------------------------")


if listx == "1" :
	
	first = input("Enter first Hash 	: ")
	second = input("Enter second Hash	: ")
	if first == second :
		print("This Hash is > Clean")
	else : print("This Hash is > Virus")

if listx == "2" :
	length = input("Enter the hash : ")
	print("The length of this hash is : " , len(length) )

if listx == "3" :
	hash = input("Enter the hash : ")
	length = len(hash)
	if length == 32 :
		print("This hash is MD5")
	if length == 40 :
		print("This hash is SHA1")
	if length == 64 :
		print("This hash is SHA256")
if listx == "4" :
	word = input("Enter Text  : ")
	md5 = hashlib.md5(word.encode())
	print("The hash is :" ,md5.hexdigest())
	
if listx == "5" :
	hash = input("Enter your Hash : ")
	file = input("write file name : ")
	with open(file , mode='r') as f :
		for line in f :
			line = line.strip()
			if md5(line.encode()).hexdigest() == hash :
				print("[-] Password found :" +line)
			elif line != hash :
				print("Text not found")
				