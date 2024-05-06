import urllib2

url = "https://example.com"  # Replace with the desired URL
response = urllib2.urlopen(url)
page_source = response.read()
print(page_source)
