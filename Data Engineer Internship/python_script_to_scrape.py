"""import"""
import pandas as pd
import numpy as np
import requests
import json
import time
final_data = []
# Parameters
coordinates = ['23.777176,90.399452']
keywords = ['all_restaurants_in_bangladesh']
radius = '1000'
api_key = ''  # insert your Places API
for coordinate in coordinates:
    for keyword in keywords:
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + coordinate + '&radius=' + str(
            radius) + '&keyword=' + str(keyword) + '&key=' + str(api_key)
        while True:
            print(url)
            respon = requests.get(url)
            jj = json.loads(respon.text)
            results = jj['results']

            for result in results:
                name = result['name']
                lat = result['geometry']['location']['lat']
                lng = result['geometry']['location']['lng']
                rating = result['rating']
                number_of_reviews = result['user_ratings_total']

                data = [name, lat, lng, rating, number_of_reviews]
                final_data.append(data)
                time.sleep(5)
            if 'next_page_token' not in jj:
                break
            else:
                next_page_token = jj['next_page_token']
                url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=' + str(
                    api_key) + '&pagetoken=' + str(next_page_token)
                labels = ['Place Name', 'Latitude', 'Longitude', 'Rating', 'Number_Of_Reviews']
                export_dataframe_1_medium = pd.DataFrame.from_records(final_data, columns=labels)
                export_dataframe_1_medium.to_csv('DE_Assignment_Internship_ Quarter_One_MD_Shoayeb_Islam.csv')
