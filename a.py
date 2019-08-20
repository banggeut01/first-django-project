import requests
response = requests.get('http://artii.herokuapp.com/make?text=GENIE&fone=acrobatic')
print(response.text)