

import wget

print('Beginning file download with wget module')

url = 'https://www.python.org/downloads/windows/'
loc = 'W:/GITHUB/NLP_SO/Data/' + 'file.html'

wget.download(url, loc)



