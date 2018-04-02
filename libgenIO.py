#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import wget

def main():
	a,b = download_libgen("http://libgen.io/ads.php?md5=002698355AB95C58BF0A41C293293D00")
	print a,b

def download_libgen(url):
	
	html_page = urllib2.urlopen(url)
	
	soup = BeautifulSoup(html_page,"html.parser")
	
	try:
		download_info = soup.find('td',{'align':'center'})

		download_url = download_info.a['href']
		print download_url
		file_name = wget.download(download_url) 
		# <td align="center" rowspan="2" valign="top">
		# <a href="http://download1.libgen.io/get.php?md5=002698355AB95C58BF0A41C293293D00&amp;key=SDJYM2DV37E1URZ6">
		# <h2>GET</h2></a></td>
		print("Dowload of %s Completed from libgen.io" % (file_name) )
		return 1,file_name

	except Exception as e:
		raise e
		print " ====+++++===Err in libgenIO.py for url = ", url
		return 0,""
if __name__ == "__main__":
    main()