#!/usr/bin/env python
from bs4 import BeautifulSoup

import urllib2
import download
import os
import send_email
import configg

def main():
	book_name = raw_input("Enter a valid book name. Copy from Amazon website for better results!\n")
	book_format_num = int(input("Enter 1 for .pdf and 2 for .mobi\n"))
	# book_name = 'sas'

	getPages(book_name,book_format_num)


def getPages(book_name,book_format_num):
	print "Searching..."
	## this weird assignment is because I could compare the extensions "char" I got got from the website so I found the 
	## equivaent ascii value to compare
	if book_format_num == 1:
		book_format_ascii = 112  ## for pdf
	elif (book_format_num == 2):
		book_format_ascii = 109  ##for mobi

	book_name2 = "+".join(book_name.split(" "))
	url = "http://libgen.io/search.php?req="+book_name2
	print url
	# url = "http://libgen.io/search.php?req=The+Diary+of+a+Young+Girl"
	# print url

	html_page = urllib2.urlopen(url)
	
	soup = BeautifulSoup(html_page,"html.parser")
	trs = soup.find_all('tr')
	
	# print "   ===================================================     "
	i = 0
	# each loop has a set of url for a particular format of file
	for tr in trs:
		# print tr.prettify()
		tds = tr.find_all('td')

		# print len(tds), type(tds)
		if len(tds) == 14:
			print "Hell yeah! Found the book"
			# print tds[-8].text, tds[-9].text , tds[-10].text , tds[-11].text
			# print tds[8].text, type(tds[8].text.encode('ascii','ignore'))
			# b_format = tds[8].text.encode('ascii','ignore').strip()
			# print "Char 1st =", tds[8].text[0]
			# print ord(tds[8].text[0]), " b_format_ascii =", book_format_ascii

			if book_format_ascii != ord(tds[8].text[0]):
				# print " NOT SAME"
				continue


			print "----------------------------"
			# for td in tds:
			# 	print td.text


			book_links = []
			for td in tds[9:11]:
				book_links.append(td.a['href'])
				# print td.a['href']

			print book_links

			flag,book_name = download.download_ebook(book_links)

			if flag:
				print "Book is downloaded. HAPPY READING !!!"
				Kindle_flag = int(input("BTW do u want this file in ur KINDLE, Enter 1: \n"))
				if Kindle_flag == 1:
					print "SENDING file to kindle address..."
					dir_path = os.path.dirname(os.path.realpath(__file__))
					file_path = dir_path + "/" + book_name
					send_email.send_mail(configg.fromaddr,configg.password,configg.toaddr,"Ebook"+book_name,book_name,file_path)

					# os.remove(file_path)
				
				return
		print "+=====================================================================================+ ",i
		i = i+1
	
	
	print "Sorry Dude! can't find your specified format book try entering again with other format"
	print "try writing book name along with Author name"



if __name__ == "__main__":
    main()