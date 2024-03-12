import asyncio
import discord
from discord.ext import commands
import random
import re

client = commands.Bot(command_prefix='$')
captcha = True  # Assuming captcha is initially enabled

# Global variables
desired_server_id = 1199106849526513926
CAPTCHA_CHANNEL_ID = 1204568374097481749  # Replace with your captcha channel ID



# Function to read Pokémon names from file
def read_pokemon_names(filename):
    with open(filename, 'r') as file:
        pokemon_names = [line.strip() for line in file.readlines() if line.strip()]
    return pokemon_names

pokemon_names = read_pokemon_names('pokemon.txt')

@client.event
async def on_message(message):
    global captcha, desired_server_id

    # Check if the message is from the desired server
    if desired_server_id is not None and message.guild.id not in (desired_server_id,):
        # This block will be executed if the condition is True
        return

    if message.author.id == 716390085896962058 and captcha:
        content = message.content
        if 'The pokémon is ' in content:
            if not len(solve(content)):
                print('Pokemon not found.')
            else:
                for i in solve(content):
                    await asyncio.sleep(random.randint(1, 3))
                    await message.channel.send(f'<@716390085896962058> c {i.lower()}')
    
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

