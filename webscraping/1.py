import requests


URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL)

print(r.url)
print('**********************************************************************************')

print(r.status_code)
print('**********************************************************************************')

# print(r.content)

