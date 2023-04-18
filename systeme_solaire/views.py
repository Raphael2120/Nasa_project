from django.shortcuts import render
from django.http import HttpResponse
import requests

def apod(request):
    # API Endpoint URL
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    #url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": "8j8gXVM40xA1J3GFT0V3bEQFU6puV4a18sgOAIpL"
    }
    response = requests.get(url, params=params)
    data = response.json()
   
    # Create a list to store the image data
    images = []

    # Iterate over the JSON data and extract the necessary information
    for item in data:
        image_date = item['date']
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{image_date[:4]}/{image_date[5:7]}/{image_date[8:10]}/png/{item['image']}.png"
        title = item['caption']
        coords = item['centroid_coordinates']

        # Split the coordinates string to extract the latitude and longitude
        lat, lon = coords['lat'],coords['lon']

        # Create an object to store the image data and add it to the list
        image = {
            'title': title,
            'date': image_date,
            'url': image_url,
            'latitude': lat,
            'longitude': lon
        }
        images.append(image)

    # Create a dictionary to store the data that will be passed to the template
    context = {
        'title': 'NASA EPIC Images',
        'images': images
    }

    return render(request, 'apod.html', context=context)
