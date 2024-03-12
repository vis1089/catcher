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

captcha = False


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
    global captcha, desired_server_id

    # Check if the message is from the desired server
    if desired_server_id is not None and message.guild.id not in (556634910031478812,):
        # Your code here
        # This block will be executed if the condition is True
        return

    if message.author.id == 716390085896962058 and captcha:
        content = message.content
        if 'The pokémon is ' in content:
            pokemon = solve(content, "pokemon.txt")
            if pokemon is None:
                print('Pokemon not found.')
            else:
                await asyncio.sleep(random.randint(1, 3))
                await message.channel.send(f'<@716390085896962058> c {pokemon.lower()}')
    
    if message.author.id == 854233015475109888 and captcha:
        match = re.search(r'^(Possible Pokémon: )?(.+)\s?:', message.content)
        if match:
            possible_pokemon_prefix, pokemon = match.groups()
            if pokemon and "Possible Pokémon" not in pokemon:
                name = (possible_pokemon_prefix or '') + pokemon.strip()
                await asyncio.sleep(random.randint(6, 12))
                await message.channel.send(f'<@716390085896962058> c {name.lower()}')

        if 'That is the wrong pokémon!' in message.content:
            await asyncio.sleep(random.randint(1, 3))
            await message.channel.send(f'<@716390085896962058> h')

        elif 'human' in message.content:
            captcha = False
            channel = client.get_channel(CAPTCHA_CHANNEL_ID)
            await channel.send(f"@everyone Please verify the Poketwo captcha asap! \nafter captcha solve type `$start` https://verify.poketwo.net/captcha/{client.user.id}")

    await client.process_commands(message)


       

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
