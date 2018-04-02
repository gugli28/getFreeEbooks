#!/usr/bin/env python
from bs4 import BeautifulSoup

import urllib2
import wget

# browser = webdriver.Firefox()


def main():
	download_libgen("http://libgen.pw/view.php?id=249422")


def download_libgen(url):
	
	html_page = urllib2.urlopen(url)
	
	#get download_url
	soup = BeautifulSoup(html_page,"html.parser")

	try:
	
		download_info = soup.find('div',{'class':'book-info__download'})
		sub_url = download_info.a['href']
		temp = sub_url.split('/')
		download_url = "https://libgen.pw/download/book/"+ temp[-1]

		print download_url
		# response = urllib2.urlopen(download_url)
		# wget is awesome it did what urllib couldn't do
		# it downloaded the file without needing any "open('filename',wb)" object unlike urllib 
		file_name = wget.download(download_url) 
		print file_name

		print("Dowload of %s Completed" % (file_name) )

		return 1, file_name

	except Exception as e:
		raise e
		print " =======Err in libgenPW.py for url = ", url
		return 0, ""

if __name__ == "__main__":
    main()