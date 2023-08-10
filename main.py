import requests


api_key = "2ff36b6d46eb450b84f8ce14c7363096"
url = "https://newsapi.org/v2/everything?domains=wsj.com&" \
	  "apiKey=2ff36b6d46eb450b84f8ce14c7363096"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access to article titles and description
for article in content["articles"]:
	print(article["title"])
	print(article["description"])
