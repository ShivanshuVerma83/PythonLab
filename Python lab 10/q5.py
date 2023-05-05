import urllib.request

from re import findall

response = urllib.request.urlopen("https://www.summet.com/dmsi/html/codesamples/addresses.html")
html = response.read()
text = html.decode()

pattern ="(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

dataCrop = findall(pattern, text)
print("The data cropped out of the webpage is:", dataCrop)
