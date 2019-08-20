import requests

print('Beginning file download with requests')

url = 'https://www.python.org/downloads/windows/'
loc = 'W:/GITHUB/NLP_SO/Data/' + 'file001.html'

r = requests.get(url)

with open(loc, 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)