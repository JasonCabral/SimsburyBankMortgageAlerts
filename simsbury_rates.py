# from urllib.request import Request, urlopen
# import requests
# # url = "http://www.simsburybank.com/download-todays-rates/"
# # response = urllib.request.urlopen(url)
# # print(response.geturl()) # 'http://stackoverflow.com/'


# url = Request("http://www.simsburybank.com/download-todays-rates/", headers={'User-Agent': 'Mozilla/5.0'})
# # webpage = urlopen(url).read()
# # response = urllib.request.urlopen(url)
# print(dir(url))
# print(url.read())


import requests

# url = "http://www.simsburybank.com/download-todays-rates/"
# r = requests.get(url, allow_redirects=True)




# import re

# def get_filename_from_cd(cd):
#     """
#     Get filename from content-disposition
#     """
#     if not cd:
#         return None
#     fname = re.findall('filename=(.+)', cd)
#     if len(fname) == 0:
#         return None
#     return fname[0]


# url = 'http://google.com/favicon.ico'
# r = requests.get(url, allow_redirects=True)
# filename = get_filename_from_cd(r.headers.get('content-disposition'))
# print(filename)



# from urllib.request import urlopen, Request

# try:
#     from StringIO import StringIO
# except ImportError:
#     from io import StringIO, BytesIO

# url = "http://www.simsburybank.com/download-todays-rates/"

# open = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read()
# memoryFile = BytesIO(open)
# print(str(open,'utf-8'))
# parser = PDFParser(memoryFile)

# import PyPDF2
# pdfFileObj = open(filename, 'rb')
# pdfReader = PyPDF2.PdfFileReader(open)
# pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())

from urllib.request import Request, urlopen
from PyPDF2 import PdfFileWriter, PdfFileReader

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO, BytesIO

url = "http://www.simsburybank.com/download-todays-rates/"
writer = PdfFileWriter()

remoteFile = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read()
memoryFile = BytesIO(remoteFile)
pdfFile = PdfFileReader(memoryFile)

# pdfReader = PyPDF2.PdfFileReader(open)
pageObj = pdfFile.getPage(0)


print(pageObj.extractText().splitlines()[149])
rate = pageObj.extractText().splitlines()[149]

from pushbullet.pushbullet import PushBullet

apiKey = "o.wfqFCb4GrmwrOwlvyEzxfi2e96GpDlSR"
p = PushBullet(apiKey)
# Get a list of devices
devices = p.getDevices()
# print(devices)
p.pushNote('jcdrummr@gmail.com', 'Simsbury Bank 30 Year Rate', str(rate), recipient_type='email')

import sys
print(sys.executable)

