Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib.request as req
>>> req.urlopen('https://www.flipkart.com/watches/pr?sid=r18&marketplace=FLIPKART&p%5B%5D=facets.ideal_for%255B%255D%3DWomen&p%5B%5D=facets.ideal_for%255B%255D%3DMen&p%5B%5D=facets.ideal_for%255B%255D%3DMen%2B%2526%2BWomen&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&offer=nb:mp:08b4e61d21&fm=neo%2Fmerchandising&iid=M_04f70c4e-1412-476a-ba4a-c670427e5e79_2.5UMSD0DDK28G&ssid=ktt1y3yr1s0000001570353341152&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_2.dealCard.OMU_5UMSD0DDK28G_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_2&cid=5UMSD0DDK28G')
<http.client.HTTPResponse object at 0x10909ca58>
>>> response = req.urlopen('https://www.flipkart.com/watches/pr?sid=r18&marketplace=FLIPKART&p%5B%5D=facets.ideal_for%255B%255D%3DWomen&p%5B%5D=facets.ideal_for%255B%255D%3DMen&p%5B%5D=facets.ideal_for%255B%255D%3DMen%2B%2526%2BWomen&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&offer=nb:mp:08b4e61d21&fm=neo%2Fmerchandising&iid=M_04f70c4e-1412-476a-ba4a-c670427e5e79_2.5UMSD0DDK28G&ssid=ktt1y3yr1s0000001570353341152&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_2.dealCard.OMU_5UMSD0DDK28G_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_2&cid=5UMSD0DDK28G')
>>> import bs4
>>> htmlSource = bs4.BeautifulSoup(response)
>>> htmlSourc
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    htmlSourc
NameError: name 'htmlSourc' is not defined
>>> htmlSource

>>> htmlSource.find('div', _class='IIdQZO')
>>> htmlSource.find('div', _class='IIdQZO _1R0K0g _1SSAGr')
>>> htmlSource.find('div', _id='container')
>>> htmlSource.find('div', class_='IIdQZO')
<div class="IIdQZO _1R0K0g _1SSAGr"><div class="_1K7fCP"><span>Ad</span></div><a class="_3dqZjq" href="/lois-caron-lcs-4116-white-day-date-series-se-croco-strap-functioning-analog-watch-men/p/itmf3zhe9mff8dee?pid=WATEKM96SZGSYFJN&amp;lid=LSTWATEKM96SZGSYFJNXZ4BBR&amp;marketplace=FLIPKART&amp;srno=b_1_1&amp;otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_2.dealCard.OMU_5UMSD0DDK28G_2&amp;otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_2&amp;fm=organic&amp;iid=en_q8YaDx3v78g%2BV6%2ByE9UIE1byy4sw7Zqr50yvrFeZHZNo34XFXWV9oVmYRnCMCnivMa88gXmGtTyYeVqdWObkyw%3D%3D&amp;ssid=gcorah4jcw0000001570354085206" rel="noopener noreferrer" target="_blank"><div><div><div class="_3JlYXy" style="padding-top:120.00%"><div class="_3ZJShS _31bMyl" style="padding-top:120.00%"><img alt="" class="_3togXc" src=""/></div></div></div></div><div></div><div class="_3gDSOa _2HqUcN _2RN9ef"><div class="DsQ2eg"><svg class="_2oLiqr" height="28" viewbox="0 0 20 16" width="28" xmlns="http://www.w3.org/2000/svg"><path class="_35Y7Yo" d="M8.695 16.682C4.06 12.382 1 9.536 1 6.065 1 3.219 3.178 1 5.95 1c1.566 0 3.069.746 4.05 1.915C10.981 1.745 12.484 1 14.05 1 16.822 1 19 3.22 19 6.065c0 3.471-3.06 6.316-7.695 10.617L10 17.897l-1.305-1.215z" fill="#2874F0" fill-rule="evenodd" opacity=".9" stroke="#FFF"></path></svg></div></div><div class="_2DOcq6"></div></a><div class="_2LFGJH" style="transform:translate3d(0, 0, 0)"><div class="_2B_pmu">Lois Caron</div><a class="_2mylT6" href="/lois-caron-lcs-4116-white-day-date-series-se-croco-strap-functioning-analog-watch-men/p/itmf3zhe9mff8dee?pid=WATEKM96SZGSYFJN&amp;lid=LSTWATEKM96SZGSYFJNXZ4BBR&amp;marketplace=FLIPKART&amp;srno=b_1_1&amp;otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_2.dealCard.OMU_5UMSD0DDK28G_2&amp;otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_2&amp;fm=organic&amp;iid=en_q8YaDx3v78g%2BV6%2ByE9UIE1byy4sw7Zqr50yvrFeZHZNo34XFXWV9oVmYRnCMCnivMa88gXmGtTyYeVqdWObkyw%3D%3D&amp;ssid=gcorah4jcw0000001570354085206" rel="noopener noreferrer" target="_blank" title="LCS-4116 WHITE DAY &amp; DATE SERIES SE CROCO STRAP DAY AND DATE FUNCTIONING Analog Watch  - For Men">LCS-4116 WHITE DAY &amp; DATE SERIES SE CROCO STRAP DAY AND...</a><div class="_3AqcXr"><img height="18" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/></div><a class="_2W-UZw" href="/lois-caron-lcs-4116-white-day-date-series-se-croco-strap-functioning-analog-watch-men/p/itmf3zhe9mff8dee?pid=WATEKM96SZGSYFJN&amp;lid=LSTWATEKM96SZGSYFJNXZ4BBR&amp;marketplace=FLIPKART&amp;srno=b_1_1&amp;otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_2.dealCard.OMU_5UMSD0DDK28G_2&amp;otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_2&amp;fm=organic&amp;iid=en_q8YaDx3v78g%2BV6%2ByE9UIE1byy4sw7Zqr50yvrFeZHZNo34XFXWV9oVmYRnCMCnivMa88gXmGtTyYeVqdWObkyw%3D%3D&amp;ssid=gcorah4jcw0000001570354085206" rel="noopener noreferrer" target="_blank"><div class="_1uv9Cb"><div class="_1vC4OE">₹312</div><div class="_3auQ3N">₹<!-- -->1,899</div><div class="VGWI6T"><span>83% off</span></div></div></a></div></div>
>>> div htmlSource.find('div', class_='IIdQZO')
SyntaxError: invalid syntax
>>> div = htmlSource.find('div', class_='IIdQZO')
>>> div.find('a', class_='_2mylT6')
<a class="_2mylT6" href="/lois-caron-lcs-4116-white-day-date-series-se-croco-strap-functioning-analog-watch-men/p/itmf3zhe9mff8dee?pid=WATEKM96SZGSYFJN&amp;lid=LSTWATEKM96SZGSYFJNXZ4BBR&amp;marketplace=FLIPKART&amp;srno=b_1_1&amp;otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_2.dealCard.OMU_5UMSD0DDK28G_2&amp;otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_2&amp;fm=organic&amp;iid=en_q8YaDx3v78g%2BV6%2ByE9UIE1byy4sw7Zqr50yvrFeZHZNo34XFXWV9oVmYRnCMCnivMa88gXmGtTyYeVqdWObkyw%3D%3D&amp;ssid=gcorah4jcw0000001570354085206" rel="noopener noreferrer" target="_blank" title="LCS-4116 WHITE DAY &amp; DATE SERIES SE CROCO STRAP DAY AND DATE FUNCTIONING Analog Watch  - For Men">LCS-4116 WHITE DAY &amp; DATE SERIES SE CROCO STRAP DAY AND...</a>
>>> div.find('a', class_='_2mylT6').text
'LCS-4116 WHITE DAY & DATE SERIES SE CROCO STRAP DAY AND...'
>>> div.find('div', class_='_1vC4OE')
<div class="_1vC4OE">₹312</div>
>>> div.find('div', class_='_1vC4OE').text
'₹312'
>>> divs = htmlSource.find_all('div', class_='IIdQZO')
>>> len(divs)
40
>>> type(divs)
<class 'bs4.element.ResultSet'>
>>> for div in divs:
	print(div.find('a', class_='_2mylT6').text + " - " + div.find('div', class_='_1vC4OE').text)

	
LCS-4116 WHITE DAY & DATE SERIES SE CROCO STRAP DAY AND... - ₹312
Sws-9042-Silver Analog Watch  - For Women - ₹331
LCS-8075 BLUE DIAL DAY & DATE FUNCTIONING Analog Watch ... - ₹312
Perfect Multicolor Leather Strap Combo Pack of 4 Analog... - ₹399
2038-WH Day and Date Analog Watch  - For Men - ₹322
1164-BR Brown Day and Date Unique New Analog Watch  - F... - ₹322
LS2804 All Black Mesh Strap Day and Date Functioning Qu... - ₹331
LCS-8049 BLACK DIAL DAY & DATE FUNCTIONING Analog Watch... - ₹331
2104-GL ION Gold Platted Day & Date Analog Watch  - For... - ₹499
2038-BL Day and Date Analog Watch  - For Men - ₹322
CR8063 DayAndDate Functioning Analog Watch  - For Men - ₹312
4054-PK Pink Day and Date Analog Watch  - For Women - ₹331
2058-BL Printed Blue Day and Date Analog Watch  - For M... - ₹322
2097-BK Black Day and Date Unique New Analog Watch  - F... - ₹329
Festive Way Farer Combo Designer Series Analog Watch  -... - ₹474
2058-BK Printed Black Day and Date Analog Watch  - For ... - ₹322
2058-WH Printed White Day and Date Analog Watch  - For ... - ₹322
LS2727 Avatar Day and Date Functioning Crocodile Strap ... - ₹312
LS2845 Day and Date Functioning Tan Strap Quartz Analog... - ₹312
LS2847 Mesh Strap Date Functioning DATEJUST 31 Series S... - ₹331
B-GR5046-BWH-CH White & Blue Dial Day & Date Functionin... - ₹312
Exclusive Smoky Grey Analog Watch  - For Men - ₹284
2074-BK Black Day And Date Analog Watch  - For Men - ₹296
New Arrival Stylish Attractive Ethnic Blue Bracelet Loo... - ₹189
428-429-438 New Best Artist Designer Combo Watch For me... - ₹499
MF13 Expedition Analog-Digital Watch  - For Men & Women - ₹1,657
LS2842 All Black Mesh Strap Day and Date Functioning Wa... - ₹331
LCS-8074 WHITE DIAL DAY & DATE FUNCTIONING Analog Watch... - ₹312
O-51610LMLI Attivo Collection Analog Watch  - For Women - ₹1,463
DE2022LG Analog Watch  - For Women - ₹285
LS2803 All Black Mesh Strap Day and Date Functioning Qu... - ₹331
LCS-8101 DAY & DATE FUNCTIONING Analog Watch  - For Men - ₹312
4049-BK Elegant Analog Watch  - For Women - ₹312
2080-BK-GL New Gold Platted Day & Date Analog Watch  - ... - ₹569
LCS-8404 ORIGINAL GOLD PLATED DAY & DATE FUNCTIONING An... - ₹569
LS2734 Wolf Gents Exclusive Mesh Strap Analog Analog Wa... - ₹249
Abx8010-Gents Exclusive (Casual+PartyWear+Formal) Desig... - ₹398
Professional Rich Look Analog Watch  - For Men - ₹379
LCS-8093 BLUE DIAL DAY & DATE FUNCTIONING Analog Watch ... - ₹312
LG 1131 Exclusive & Royal Slim Leather Watch Analog Wat... - ₹338
>>> import urllib.request as req
>>> req.urlopen('url comes here')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    req.urlopen('url comes here')
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 510, in open
    req = Request(fullurl, data)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 328, in __init__
    self.full_url = url
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 354, in full_url
    self._parse()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 383, in _parse
    raise ValueError("unknown url type: %r" % self.full_url)
ValueError: unknown url type: 'url comes here'
>>> #import urllib.request as req
>>> #req.urlopen('url comes here')
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #import urllib.request as req
>>> #req.urlopen('url comes here')
>>> #response = req.urlopen('url comes here')
>>> #htmlPage = bs4.BeautifulSoup(response)
>>> #div = htmlPage.find( tagname,  class_ = '')     or use find_all()
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #Step 1 - > Install python in C drive
>>> #Step 2 -> Go to Command Prompt, run ->    pip install bs4
>>> #Step 3 -> Then use the above given code to perform web crawling
>>> 
