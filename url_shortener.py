import pyshorteners

input_url = input("Enter the URL: ")
s = pyshorteners.Shortener()
short_url = s.tinyurl.short(input_url)
print(f"Short URL is {short_url}")