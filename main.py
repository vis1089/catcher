import re
import os
import asyncio
import random
import string
import discord
from discord.ext import commands, tasks

user_token = os.environ['token']
spam_id = os.environ['spam_id']
prefix = "."
desired_server_id = [1199106849526513926]

poketwo = 716390085896962058
pokename = 874910942490677270
P2Assistant = 854233015475109888
client = commands.Bot(command_prefix=prefix)
intervals = [3.4, 2.6, 2.8, 3.0, 3.2]

def in_allowed_channel():
    def predicate(ctx):
        return ctx.channel.name == 'cmd'
    return commands.check(predicate)

def solve(message, file_name):
    with open(file_name, "r") as f:
        pokemons = f.readlines()

    for pokemon in pokemons:
        if pokemon.strip().lower() in message.lower():
            return pokemon.strip()

    return None

@tasks.loop(seconds=random.choice(intervals))
async def spam():
    channel = client.get_channel(int(spam_id))
    await channel.send(''.join(random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 7) * 5))

async def on_ready():
    print('*' * 25)
    print(f'Logged in as {client.user.name} ✅:')
    print(f'With ID: {client.user.id}')
    print('*' * 25)
    guild = client.guilds[0]

@spam.before_loop
async def before_spam():
    await client.wait_until_ready()

spam.start()

@client.event
async def on_ready():
    print('*' * 25)
    print(f'Logged in as {client.user.name} ✅:')
    print(f'With ID: {client.user.id}')
    print('*' * 25)

@client.event
async def on_message(message):
    channel = client.get_channel(message.channel.id)

    # Logic for Pokename
    if message.author.id == pokename or message.author.id == P2Assistant:
        content = message.content

        if 'Rare Ping' in content or 'Rare ping' in content:
            await message.channel.send(f'<@{poketwo}> c {pokemon_detected}')

        elif 'Regional Ping' in content or 'Regional ping' in content:
            await message.channel.send(f'<@{poketwo}> c {pokemon_detected}')

        elif 'Collection Pings' in content or 'Collection pings' in content:
            await message.channel.send(f'<@{poketwo}> c {pokemon_detected}')

        elif 'Shiny Hunt Pings' in content or 'Shiny hunt pings' in content:
            await message.channel.send(f'<@{poketwo}> c {pokemon_detected}')
    else:
        content = message.content
        detected_pokemon = solve(content, 'pokemon.txt')
        if detected_pokemon:
            await message.channel.send(f'A wild {detected_pokemon} appeared!')

@client.command()
@commands.has_permissions(administrator=True)
async def start(ctx):
    spam.start()
    await ctx.send('Started Spammer!')
    print('Started Spammer! ✅:')

@client.command()
@commands.has_permissions(administrator=True)
async def stop(ctx):
    spam.cancel()
    await ctx.send('Stopped Spammer!')
    print('Stopped Spammer! ✅:')

client.run(user_token)




              
client.run(f"{user_token}")
