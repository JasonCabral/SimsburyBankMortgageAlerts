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

# print(pageObj.extractText().splitlines()[96])

rate96 = pageObj.extractText().splitlines()[96]
rate149 = pageObj.extractText().splitlines()[149]

rate_list = [rate96, rate149]

rate_list_temp = []

for i in rate_list:
	if len(i) < 7:
		rate_list_temp.append(i)

if len(rate_list_temp) > 0:
	printrates2 = "\n".join(rate_list_temp)
else:
	printrates2 = "Need New Line"

print(printrates2)

apiKey = "API_KEY"
p = PushBullet(apiKey)
p.pushNote('EMAIL', 'Simsbury Bank 30 Year Rate', printrates2, recipient_type='email')

# import sys
# print(sys.executable)

### OLD DYNAMIC CODE
# if len(rate96) < 7:
# 	if len(rate149) < 7:
# 		printrates = str(rate96 + "\n" + rate149)
# 	else:
# 		printrates = str(rate96)
# else:
# 	if len(rate149) < 7:
# 		printrates = str(rate149)
# 	else:
# 		printrates = "Need New Line"