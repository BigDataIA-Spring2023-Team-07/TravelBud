# TravelBud

> [Codelabs Documentation](https://codelabs-preview.appspot.com/?file_id=1jhLIlc8r7w5w6xI9wYMLNCgZBmF4S3Pl0wPJ1eCel9I#0)<br>


### Introduction

Travel Bud is an all-in-one vacation planning application designed to simplify the process of researching and booking flights, accommodations, and local attractions. The Personalized Travel Itinerary Planner creates tailored travel itineraries based on user preferences and budget constraints, making vacation planning a more efficient and enjoyable experience. An example of the generated itinerary can be seen [here](/Goyal%20Itinerary.pdf)

### Features

- Personalized recommendations based on user areas of interest
- Ability for users to update their password and preferences
- Rate limiting based on selected plans
- Application-level analytics for detailed insights into application usage
- Top 10 list of locations based on the user's destination, along with **optimal pairing** between the locations
- Leveraging Booking.com API and Skyscanner API to help users find suitable accommodations and flights
- Assistance in creating an itinerary using the Chatgpt API and optimal prompting techniques (Custom Prompt created can be seen [here](/prompt.py))
- Option to download itinerary in three languages (English, Spanish, and Hindi) delivered via Hugging Face models
- Coverage of a wide demographic, making it a global application

### Architecture Diagram
<img src="Architecture Diagram.jpeg" alt="Architecture Diagram">

### Demo 

[Watch the video](https://youtu.be/K9pOR9n-TbQ?si=mqgg8lBWjGLJ9HHY)


### Optimization 
**Location Optimization:**

At Travel Bud, we understand that time is a valuable commodity for travelers, and therefore, we strive to provide the most efficient and effective itinerary planning experience possible. Our optimization algorithm is designed to retrieve the top 10 locations from the Google Maps API based on the user's destination, ensuring that they have access to the best and most popular local attractions.

Once the user selects their areas of interest from the 10 available options, our algorithm creates pairs of two locations that are in close proximity to each other. This ensures that the user can visit both locations in a single day, maximizing their vacation experience and making the most of their time. If there are any remaining locations, the user can visit them on their last day, making their itinerary as comprehensive as possible.

We understand that every traveler is different and has unique needs and preferences. Therefore, we recommend the optimal number of locations for the user to visit based on the number of days they plan to stay at their destination. Typically, we recommend no more than twice the number of days the user plans to stay, ensuring that they have enough time to relax and enjoy their vacation.

**Booking Optimization:**

We understand that budget is a key factor for many travelers when planning their vacation. Therefore, we offer the option for users to select their desired start and end days and budget, allowing them to tailor their itinerary to their specific needs.

Using this information, our algorithm creates groupings of all possible options and searches for hotels and airlines that fit the user's criteria. We search for options that fit within the user's budget, while also ensuring that they have access to the best possible accommodations and flights.

Our algorithm then finds the optimal cost that fits the user's budget, giving them the best possible experience for their money. Users can choose from four airline options: best, cheapest, fastest, and direct, providing them with the flexibility to select the airline that best suits their needs.

In cases where the user's budget does not match their desired options, we recommend the lowest possible cost to the user, ensuring that they get the most out of their vacation while saving money.

Overall, our optimization algorithms for location and booking ensure that Travel Bud users have the best possible vacation experience while also optimizing their time and budget.

### Steps to reproduce
To run it locally please follow the steps below - 
- clone the repo 
- create a virtual environment and install requirements.txt
- subscribe to both these free tiers on Rapid API [Booking.com](https://rapidapi.com/tipsters/api/booking-com) and [Skyscanner.com](https://rapidapi.com/3b-data-3b-data-default/api/skyscanner44/)
- create a .env file with the following variables
```
OPENAI_API_KEY=
AWS_ACCESS_KEY=
AWS_SECRET_KEY=
AWS_LOG_ACCESS_KEY = 
AWS_LOG_SECRET_KEY = 
bucket_name= <Enter AWS Bucket Name>
RAPID_API_KEY =
GOOGLE_MAPS_API_KEY =
DB_USER_NAME=
DB_PASSWORD= 
DB_HOST=
DB_NAME= 
SECRET_KEY= <secret key generated using secrets package>
ALGORITHM=HS256
```


Attestation
WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK

Contribution:

- Dhanush Kumar Shankar: 25% 
- Nishanth Prasath: 25%
- Shubham Goyal: 25%
- Subhash Chandran Shankarakumar: 25%
