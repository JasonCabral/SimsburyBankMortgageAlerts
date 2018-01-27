from urllib.request import Request, urlopen
from PyPDF2 import PdfFileWriter, PdfFileReader
from pushbullet.pushbullet import PushBullet
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO, BytesIO

url = "http://www.simsburybank.com/download-todays-rates/"
writer = PdfFileWriter()

remoteFile = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read()
memoryFile = BytesIO(remoteFile)
pdfFile = PdfFileReader(memoryFile)

pageObj = pdfFile.getPage(0)

# print(pageObj.extractText().splitlines()[149])
rate = pageObj.extractText().splitlines()[149]

apiKey = "API_KEY"
p = PushBullet(apiKey)
p.pushNote('EMAIL', 'Simsbury Bank 30 Year Rate', str(rate), recipient_type='email')

# import sys
# print(sys.executable)

