#!python3

import requests
import sys
import time
from pyshorteners import Shortener
from bs4 import BeautifulSoup as bs
from termcolor import colored, cprint

cprint("Musa ŞANA-musana.net", "white", "on_red", end="\n", attrs=['bold'])

key = "YOUR API KEY FOR SHORTING URL"
shortener = Shortener('Google', api_key=key)


if(len(sys.argv) == 1):
	sys.argv = ['-', 'haber7', 'cnnturk', 'sabah', 12]

if(sys.argv[1].isnumeric()):
	adet = sys.argv[1]
	sys.argv = ['-', 'haber7', 'cnnturk', 'sabah', adet]


class haberBotu:

	def sabah():
		cprint("\n"+"~"*35+"SABAH.COM.TR"+"~"*35, "white", "on_cyan", attrs=['bold'])
		req = requests.get("http://sabah.com.tr/")
		bea = bs(req.text, "lxml")
		url_list = list()
		sabah_no = 0

		manset = bea.find("div", {"id":"surmanset2"})

		for i in manset.findAll("a"):
			sabah_no+=1

			if sabah_no <= int(sys.argv[-1]):
				if not "http://www.sabah.com.tr" in i["href"]:
					url_list.append("http://www.sabah.com.tr"+i["href"])
				else:
					url_list.append(i["href"])
			else:
				break

		for i in url_list:
			reqq = requests.get(i)
			bsp = bs(reqq.text, "lxml")
			x = bsp.title.string.split("-")
			url_kisa = colored(shortener.short(i), "white", "on_magenta")
			print(url_kisa+" - "+x[0])

	def haber7():
		cprint("\n"+"~"*35+"HABER7.COM"+"~"*35, "white", "on_cyan", attrs=['bold'])
		req = requests.get("http://www.haber7.com/")
		bsp = bs(req.text, "lxml")
		haber7_no = 0

		r = bsp.find("div", {"class":"bx-secondary-headline-pager"})

		for i in r.findAll("div", {"class":"bx-pager-item"}):
			haber7_no += 1
			if haber7_no <= int(sys.argv[-1]):
				lnk = i.find("a")
				url_kisa = colored(shortener.short(lnk["href"]), "white", "on_blue")
				print(url_kisa+" - "+lnk["title"])
				time.sleep(1)
			else:
				break

	def cnnturk():
		cprint("\n"+"~"*35+"CNNTURK.COM"+"~"*35, "white", "on_cyan", attrs=['bold'])
		req = requests.get("http://cnnturk.com")
		bh = bs(req.text, "lxml")
		cnnturk_no = 0

		cnn = bh.find("div", {"class":"col-md-8"})

		for i in cnn.findAll("li",{"class":"swiper-pagination-bullet"}):
			cnnturk_no += 1
			if cnnturk_no <= int(sys.argv[-1]):
				lnk = i.find("a")
				url_kisa = colored(shortener.short("http://cnnturk.com"+lnk["href"]), "white", "on_green")
				print(url_kisa+" - "+lnk["title"])
				time.sleep(1)

for i in sys.argv[1:-1]:
	try:
		getattr(haberBotu, i)()
	except AttributeError:
		cprint("\nHATA! "+i+" adında bir argüman bulunmamaktadır. Sadece haber7 | cnnturk | sabah argümanları geçerlidir.", "magenta", attrs=['bold'])
