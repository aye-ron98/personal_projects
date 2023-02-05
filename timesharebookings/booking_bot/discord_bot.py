import asyncio
import os
from datetime import datetime

import discord
from discord import Embed
from discord.ext import commands
from dotenv import load_dotenv
from selenium import webdriver

import booking_functions_bot
import input_checks

load_dotenv()
intents = discord.Intents(messages=True, presences=True, message_content=True)
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_message(message):
    if message.content.startswith('$book'):
        channel = message.channel

        await channel.send('Where would you like to go?')
        destination = await bot.wait_for('message', check=None)

        while True:
            await channel.send('how long will your stay be?')
            length = await bot.wait_for('message', check=None)

            if length.content.isnumeric():
                break
            else:
                await channel.send('Please enter a valid number')
                continue

        while True:
            await channel.send('Enter your arrival date in DD-month-YYYY, eg-01-Jan-2023')
            start = await bot.wait_for('message', check=None)

            if input_checks.check_user_date(start.content):
                break
            else:
                await channel.send('Arrival date must be in DD-month-YYYY format, eg 01-Jan-2023, '
                                   'please ensure arrival is not in the past.')
                continue

        while True:
            await channel.send('Enter your departure date in DD-month-YYYY')
            end = await bot.wait_for('message', check=None)

            if input_checks.check_user_date(end.content):
                break
            else:
                await channel.send('Departure date must be in DD-month-YYYY format, eg 01-Jan-2023, '
                                   'please ensure arrival is not in the past.')
                continue

        while True:
            await channel.send('how many people will be present?')
            people = await bot.wait_for('message', check=None)

            if people.content.isnumeric():
                break
            else:
                await channel.send('Please enter a valid number')
                continue

        while True:
            await channel.send('How many hours would you like to be check for')
            hours = await bot.wait_for('message', check=None)

            if hours.content.isnumeric():
                break
            else:
                await channel.send('Please enter a valid number')
                continue

        driver = webdriver.Chrome()
        driver.get('https://member.embarcresorts.com/')

        booking_functions_bot.login(driver)
        booking_functions_bot.page_navigation(driver)

        booking_functions_bot.check_for_popup(driver)

        flag = False
        while datetime.now() < input_checks.get_time_to_check(hours.content):
            booking_functions_bot.check_for_bookings(driver, destination.content, start.content, end.content,
                                                     length.content, people.content)

            if booking_functions_bot.check_avalability(driver):
                flag = True
                await channel.send('I found some bookings, check them out!')
                bookings = booking_functions_bot.print_avaliability(driver)

                response = f"Here are bookings from {start.content} to {end.content}:\n\n"
                for item in bookings:
                    response += f"{item[0]}    |     {item[1]}\n"

                embed = Embed(title="Available bookings", description=response)

                await channel.send(embed=embed)
                driver.close()
                break
            else:
                await asyncio.sleep(300)
                driver.refresh()
                flag = False
                continue

        if not flag:
            await channel.send('time is up, unfortunately i have found no bookings')
            driver.close()


bot.run(os.getenv('Token'))
