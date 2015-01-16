import urllib, json
url = "http://letsrevolutionizetesting.com/challenge.json?id=995287801"
response = urllib.urlopen(url);
data = json.loads(response.read())
print data