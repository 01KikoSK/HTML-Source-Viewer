from selenium import webdriver

url = "https://example.com"  # Replace with the desired URL
browser = webdriver.Firefox()  # You can use other browsers too
browser.get(url)
html_source = browser.page_source
print(html_source)
