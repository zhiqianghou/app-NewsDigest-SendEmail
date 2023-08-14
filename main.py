import requests
from send_email import send_email


api_key = "2ff36b6d46eb450b84f8ce14c7363096"
url = "https://newsapi.org/v2/everything?domains=wsj.com&" \
	  "apiKey=2ff36b6d46eb450b84f8ce14c7363096"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access to article titles and description
body = ""
for article in content["articles"]:
	if article["title"] is not None:
		body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)