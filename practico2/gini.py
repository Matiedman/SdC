#Author: Robles, Karen Yesica;Rodriguez Luciano;Magin Matias
#Version: 1.0.0

import requests
import json
import ctypes

libsuma = ctypes.CDLL('./libsuma.so')
libsuma._suma.argtypes = [ctypes.c_float]
libsuma._suma.restype = ctypes.c_int

def show_menu():
	print("1. Select pais")
	print("2. Exit")

def get_url(country):
    url = f"https://api.worldbank.org/v2/en/country/{country}/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1"
    return url

def get_suma(num):
	return libsuma._suma(num)

def option_1():
	 country = input ("Please enter a string:")
	 url = get_url(country)
	 response = requests.get(url)
	 data = response.json()
	 elementos = data[1]
	 for elem in elementos:
	     element = elem.get('value')
	     num = get_suma(element) if element is not None else "None"
	     dat = elem.get('date')
	     print (f"Date : {dat} Indice GINI : {element} ---> {num}")


while True:
	show_menu()
	option = input("Select an option: ")

	if option == "1":
         option_1()
		
	elif option =="2":
	     print("Exiting the program...")
	     break
	else:
	    print("Invalid option")	