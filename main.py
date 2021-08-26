import discord
from discord.ext import commands
from datetime import date
import time
import requests
import json

# old code maybe not working properly

today = date.today()

version = '0.0.2'

client = discord.Client()
bot = commands.Bot(command_prefix='%')


@client.event
async def on_ready():
    print('Bot on')


@client.event
async def on_message(message):
    if message.author == client.user:
        return


@client.event
async def on_message(message):

    if message.content.startswith('%version'):
        await message.channel.send(f'Versão {version}')

    if message.content.startswith('%spamserver'):
        await message.channel.send(f'@everyone ')
        await message.channel.send(f'@everyone ')
        await message.channel.send(f'@everyone ')
        await message.channel.send(f'@everyone ')

    if message.content.startswith('%temperature'):
        api_key = 'weather api key'
        city_id = 'weather api city id here'
        url = f'https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        umidade = data['main']['humidity']
        hora = (time.strftime("%H:%M"))
        fdate = date.today().strftime('%d/%m/%y')
        await message.channel.send(f':calendar::{fdate} | :alarm_clock:: {hora}')
        await message.channel.send(f'Temperatura em Colina agora: {int(temp)}°c')
        await message.channel.send(f'Sensação térmica de: {int(feels_like)}°c')
        print(temp, feels_like)
        await message.channel.send(f'Umidade: {umidade}%')
        if temp < float(25.0):
            await message.channel.send('https://media.tenor.com/images/db718014cb7224b6e460317406d3aeeb/tenor.gif')
        elif temp > float(25.0):
            await message.channel.send('https://media.tenor.com/images/0e8a4e8e55f651d9c34a7abaca8d1f44/tenor.gif')

client.run('discord bot key here')
