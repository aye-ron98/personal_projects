# Personal Projects

## 1. Project Description
This repo is dedicated to my personal projects 
* webscraper.py
* booking_bot.py
* discord_bot.py
	
## 2. Technologies Used
Technologies used for this project:
* Python3
* Selenium Web module
* Beautiful Soup 4

## 3. Complete setup/installion/usage
This program requires Selenium and Beautiful Soup to run. Some unit test require freezegun. Intallation can be done using:
* pip install Selenium
* pip install BS4
* pip install freezegun

Here are the steps ...
* clone this repo
* open in VS code
* navigate to the desired program
* run in VS code

## 5. Known Bugs
Here are some known bugs:
* discord bot has double messaged at times, causing user inputs to lag one behind the user prompts
* while checking for hotel avaliability in hotel booker, the while loop will throw a couroutine exception as the check while loop has not completed however this will not cause the program to crash
	
## 6. Contents of Folder
Content of the project folder:

```
 Top level of project folder: 
├── timesharebookings               
├── webscraper
└── README.md

subfolders and files of timesharebookings:
├── booking_bot
    / booking_functions_bot.py       
    / discord_bot.py                   # main program to execute for discord bot
    / input_checks.py
├── unit_test                    
├── booking.py                         # main program to execute for python only program                               
├── booking_functions.py
├── notification.py	
├── user_inputs.py      

subfolders and files of webscarper:
├── page_turner.py                                  
├── webscraper.py			# this version uses Selenium and BS4 not very optimized
├── webscraper2.py			# this version uses only BS4 faster and more optimized

subfolders and files of unit_test:
├── user_inputs_unit_tests 
    / .__init__.py
    / test_get_user_password.py
    / test_get_user_name.py
    / test_get_arrival_dates.py         # requires freezegun module
    / test_get_departure_date.py        # requires freezegun module
    / test_get_number_of_occupants.py
    / test_get_number_of_nights.py
├── booking_functions_test
    / .__init__.py
    / test_booking_functions.py

```


