import requests
from PIL import Image, ImageDraw, ImageFont
import random

# Define the font to use for the text
font_path = "arial.ttf"
font_size = 25
font = ImageFont.truetype(font_path, font_size)
bold_font = ImageFont.truetype(font_path, font_size)

# Assign a variable to get the country
country = input("Enter Country's 2 letter code for news: ")

url = 'https://newsapi.org/v2/top-headlines'
api_key = 'Enter API key here'

# Set up query parameters
query_params = {
    'country': country,  # news from the country
    'pageSize': 10,  # number of articles to retrieve
    # 'page': random.randint(1, 10)  # random page number
}

# Set up request headers
headers = {
    'Authorization': f'Bearer {api_key}'
}

# Make the API request
response = requests.get(url, headers=headers, params=query_params)

# Check if the request was successful
if response.status_code == 200:
    # Create an empty image to place the headlines on
    img = Image.new("RGBA", (1500, 500), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Print the titles of the retrieved articles on the image
    articles = response.json()['articles']
    y_offset = 10
    for article in articles:
        title = article['title']
        draw.text((10, y_offset), title, font=bold_font, fill=(255, 255, 255), stroke_fill=(0, 0, 0), stroke_width=1)
        y_offset += 30

    # Save the image to a file
    news = 'news.png'
    img.save(news)
    #img.show(news)
else:
    print('Error: Request failed with status code', response.status_code)
