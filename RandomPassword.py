#/media/fucksociety/UBUNTU20_0/RubenLeo/RandomPassword.py
# Create Programs For Penetration Testing, Hacking, Encryption and Decryption, and CyberSecurity
# Written By: BenLeo CyberSecurity
# My Team: fSociety Hacker Syndicate
# The Reason I Make This Program Is To Help Me Understand Programming Logic and Practice Programming Skills
# Made On September 18 at 22:18 PM
# Okay Good Luck :)

# Import Python3 Module To Help Generate This Random Passwords Programs
import random # To Generate Numbers Or Strings Randomly
# Random = Acak (Indonesian Language)

import requests # Requests is a Python module that you can use to send various HTTP requests.
# Requests = Permintaan (Indonesian Language)

import os # OS module in python3 works to call other programs
# OS = Operating System

import sys # The sys module is used to access the interpreter configuration at runtime and interact with the operating system environment.
# Sys = Sistem (Indonesian Language)

from string import digits, punctuation, ascii_letters
# Strings are the most popular type in programming languages. We can make it just by enclosing the character in quotes. 
# Python treats single quotes the same as double quotes. Creating a string is as easy as assigning a value to a variable.

# Indonesia
# String adalah jenis yang paling populer di bahasa pemrograman. Kita bisa membuatnya hanya dengan melampirkan karakter dalam tanda kutip. 
# Python memperlakukan tanda kutip tunggal sama dengan tanda kutip ganda. Membuat string semudah memberi nilai pada sebuah variabel.
# String dalam KBBI memiliki arti: Tali, Senar, Deretan

length = input("[!] Length Passwords: ")
length = int(length)

symbols = digits + punctuation + ascii_letters
# Contoh unik dari struktur data yang didefinisikan oleh kelasnya. 
# Objek terdiri dari kedua anggota data (variabel kelas dan variabel contoh) dan metode.
random_password_secure = random.SystemRandom()
passwords = "".join(random_password_secure.choice(symbols)
for i in range(0, length))

print(passwords)


def make_a_program_to_clean_the_screen():
	import os, sys
	os.system("")
	os.system("")



def about_program_writer():
	print("""
		+=================================================================+
		.................... FSOCIETY HACKER SYNDICATE ....................
		+=================================================================+
		     [!] Author          : BenLeo Cyber Security
		     [!] Team            : fSociety Hacker Syndicate
		     [!] Created         : September 30, 2021 at 22:42 PM
		+=================================================================+
		""")
about_program_writer()
make_a_program_to_clean_the_screen()