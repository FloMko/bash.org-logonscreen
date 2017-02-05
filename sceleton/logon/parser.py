# coding: utf-8
'''
Created on 2017-02-05

@author: flomko
'''
import requests

def init():
	data = requests.get ('http://bash.im/forweb/?u')
	answer = data.text
	print (answer)
init()
