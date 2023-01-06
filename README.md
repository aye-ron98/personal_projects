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
    / discord_bot.py
    / input_checks.py
├── unit_test                   
    / .__init__.py
    / test_get_user_password
    / test_get_user_name
├── booking.py                                   
├── booking_functions.py
├── notification.py
├── test_get_arrival_dates.py		# currently work in progress, working with freezegun method to create datetime object for unit testing
├── user_inputs.py      

subfolders and files of webscarper:
├── page_turner.py                                  
├── webscraper.py			# this version uses Selenium and BS4 not very optimized
├── webscraper2.py			# this version uses only BS4 faster and more optimized
    

```


