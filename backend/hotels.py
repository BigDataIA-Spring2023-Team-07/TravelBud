import numpy as np
import requests
from datetime import datetime, timedelta
import pandas as pd
import os
from dotenv import load_dotenv
import json

load_dotenv()

def get_location_id(destination):
  url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"

  querystring = {"name": destination,"locale":"en-gb"}

  headers = {
    "X-RapidAPI-Key": os.environ.get('RAPID_API_KEY'),
    "X-RapidAPI-Host": "booking-com.p.rapidapi.com"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  response = response.json()
  return response[1]['dest_id'], response[1]['dest_type']

def create_date_pairs(start_date, end_date, num_days):
    date_pairs = []
    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    while current_date <= end_date:
        pair_end_date = current_date + timedelta(days=num_days-1)
        if pair_end_date > end_date:
            pair_end_date = end_date
        date_pairs.append((current_date.strftime('%Y-%m-%d'), pair_end_date.strftime('%Y-%m-%d')))
        current_date += timedelta(days=num_days)

    return date_pairs


def get_hotel_cost(checkin_date, checkout_date, adults_number, type_des, id, rooms_cnt):

    url = "https://booking-com.p.rapidapi.com/v1/hotels/search"

    querystring = {
        "checkin_date": checkin_date,
        "checkout_date": checkout_date,
        "adults_number": adults_number,
        "dest_type": type_des,
        "units": "metric",
        "order_by": "review_score", #sorting by review score and then finding the lowest price
        "dest_id": id,
        "filter_by_currency": "USD",
        "locale": "en-gb",
        "room_number": rooms_cnt,
        "page_number": "0",
        "include_adjacency": "true"
    }

    headers = {
                "X-RapidAPI-Key": os.environ.get('RAPID_API_KEY'),
        "X-RapidAPI-Host": "booking-com.p.rapidapi.com"

    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.json()
    return result

def calculate_hotel_costs(start_date, end_date, num_days, adults_number, type_des, id, rooms_cnt):
    date_pairs = create_date_pairs(start_date, end_date, num_days)
    hotel_costs = []
    df_list = []

    for pair in date_pairs:
        checkin_date = datetime.strptime(pair[0], '%Y-%m-%d')
        checkout_date = datetime.strptime(pair[1], '%Y-%m-%d')
        response = get_hotel_cost(checkin_date.strftime('%Y-%m-%d'), checkout_date.strftime('%Y-%m-%d'), adults_number, type_des, id, rooms_cnt)
        hotel_names = []
        prices = []
        for val in response['result']:
            hotel_names.append(val['hotel_name'])
            prices.append(val['composite_price_breakdown']['all_inclusive_amount']['value'])
        hotel_names, prices = zip(*sorted(zip(hotel_names, prices), key=lambda x: x[1]))
        hotel_cost = {
            'start_date': checkin_date.strftime('%Y-%m-%d'),
            'end_date': checkout_date.strftime('%Y-%m-%d'),
            'hotel_names': list(hotel_names),
            'prices': list(prices)
        }
        hotel_costs.append(hotel_cost)

        for cost in hotel_costs:
            start_date = cost['start_date']
            end_date = cost['end_date']
            hotel_names = cost['hotel_names']
            prices = cost['prices']
            df_temp = pd.DataFrame({
                'start_date': [start_date]*len(hotel_names),
                'end_date': [end_date]*len(hotel_names),
                'hotel_name': hotel_names,
                'price': prices
            })
            df_list.append(df_temp)

        df = pd.concat(df_list, ignore_index=True)
        df_sorted = df.sort_values(by='price', ascending=True).reset_index(drop=True)
    return df_sorted


start_date = '2023-09-27'
end_date = '2023-10-07'
num_days = 3 #int
adults_number = 6 # int
num_rooms = '1' #str
des_id, type_des= get_location_id("New York")
hotel_costs = calculate_hotel_costs(start_date, end_date, num_days, adults_number, type_des, des_id, num_rooms)

print(hotel_costs)