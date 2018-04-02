
#!/usr/bin/env python
from bs4 import BeautifulSoup

import urllib2

import libgenPW
import libgenIO

def main():
	url_list = ['http://libgen.pw/view.php?id=249422', 'http://libgen.io/ads.php?md5=002698355AB95C58BF0A41C293293D00', 'http://b-ok.org/md5/002698355AB95C58BF0A41C293293D00', 'http://bookfi.net/md5/002698355AB95C58BF0A41C293293D00']
	download(url_list)


def download_ebook(url_list):
	print url_list
	
	flag_pw = libgenPW.download_libgen(url_list[0])
	if flag_pw:
		return flag_pw

	flag_io = libgenIO.download_libgen(url_list[1])
	if flag_io:
		return flag_io

if __name__ == "__main__":
    main()