import discord
from discord.ext import commands
import requests

headers = {'X-Auth-Token': 'YOUR_API_KEY'}
TOKEN = 'MTA3MDY0NjY0NjExNjk5NTA5Mg.GA6P9u.TcCcTqdHHo96VhKqwDpWtRcvdf78Jov1nz1FLs'
intents = discord.Intents.all()
description = '''let's see my option.'''
bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print('===================')
    print('     Login  as')
    print('       ' + bot.user.name + '.')
    print(bot.user.id)
    print('===================')

@bot.command()
async def add(ctx, left : int, right : int):
    '''บวกเลข ตัวอย่าง ?add 5 7'''
    await ctx.send(left + right)

@bot.command()
async def minus(ctx, left : int, right : int):
    '''ลบเลข ตัวอย่าง ?minus 3 1'''
    await ctx.send(left - right)

@bot.command()
async def muliply(ctx, left : int, right : int):
    '''คูณเลข ตัวอย่าง ?multiply 5 2'''
    await ctx.send(left * right)
    
@bot.command()
async def divide(ctx, left : int, right : int):
    '''หารเลข ตัวอย่าง ?divide 9 3'''
    if (right == 0 ):
        await ctx.send("Can not divide.")
    else : await ctx.send(left / right)
    
@bot.command()
async def poke(ctx, name : str):
    '''แสดงข้อมูลโปเกม่อน ตัวอย่าง ?poke pikachu'''
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"

    response = requests.get(url, headers=headers)
    if (response.status_code == 200):
        data = response.json()
        
        pokemon_name = data['name']
        base_experience = data['base_experience']
        img_pokemon = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{data['id']}.png"
        
        await ctx.send(img_pokemon)
        await ctx.send(pokemon_name.upper() + "\nHave exp = " + str(base_experience))
    else : await ctx.send("Pokemon not found.")

@bot.command()
async def crypto(ctx, currency1API : str):
    '''แสดงข้อมูลคริปโต ตัวอย่าง ?crypto bitcoin'''
    url = f"https://api.coingecko.com/api/v3/coins/{currency1API}?localization=false"
    
    response = requests.get(url, headers=headers)
    if (response.status_code == 200):
        data = response.json()
        currency = data['id']
        price_thb = data['market_data']['current_price']['thb']
        last_date = data['last_updated']
        img_currency = data['image']['large']
        
        await ctx.send(img_currency)
        await ctx.send(currency.upper() + " " + str(price_thb) + " BAHT.")
        await ctx.send(f'Last update : {last_date:.10}')
    else : await ctx.send("Coin not found.")
    
bot.run(TOKEN)


    # print(f"Currency: {c}")
    # print(f"Price: {price_thb} ฿")
    # print(f"Last Update: {last_date}")