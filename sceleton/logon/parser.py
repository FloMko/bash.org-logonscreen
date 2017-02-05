# coding: utf-8
'''
Created on 2017-02-05

@author: flomko
'''
import requests
import re

def question():
	data = requests.get ('http://bash.im/forweb/?u')
	answer = data.text
	print (answer)
#def cut_text():
	pos_start = re.search('1em 0;">',answer)
	pos_end = re.search('small>',answer)
	html_text = [pos_start,pos_end]
	print (html_text)
question()
#cut_text()
