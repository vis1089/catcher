import re, os, asyncio, random, string, discord
from discord.ext import commands, tasks

user_token = os.environ['token']
spam_id = os.environ['spam_id']
prefix = "."
desired_server_id = [1199106849526513926]

poketwo = 716390085896962058
pokename = 874910942490677270
P2Assistant = 854233015475109888
client = commands.Bot(command_prefix= prefix )
intervals = [3.4, 2.6, 2.8, 3.0, 3.2]

def in_allowed_channel():
  def predicate(ctx):
    return ctx.channel.name == 'cmd'
  return commands.check(predicate)
  
def solve(message, file_name):
    hint = []
    for i in range(15,len(message) - 1):
        if message[i] != '\\':
            hint.append(message[i])
    hint_string = ''
    for i in hint:
        hint_string += i
    hint_replaced = hint_string.replace('_', '.')
    with open(f"{file_name}", "r") as f:
        solutions = f.read()
    solution = re.findall('^'+hint_replaced+'$', solutions, re.MULTILINE)
    if len(solution) == 0:
        return None
    return solution

@tasks.loop(seconds=random.choice(intervals))
async def spam():
    channel = client.get_channel(int(spam_id))
    await channel.send(''.join(random.sample(['1','2','3','4','5','6','7','8','9','0'],7)*5))

async def on_ready():
    print(f'Logged into account: {client.user.name}')
    guild = client.guilds[0]

@spam.before_loop
async def before_spam():
    await client.wait_until_ready()

spam.start()

@client.event
async def on_ready():
    print(f'*'*25)
    print(f'Logged in as {client.user.name} ✅:')
    print(f'With ID: {client.user.id}')
    print(f'*'*25)

@client.event
async def on_message(message):
    channel = client.get_channel(message.channel.id)
    
    # Logic for Pokename
    if message.author.id == pokename or message.author.id == P2Assistant:
        content = message.content

        if 'Rare Ping' in content or 'Rare ping' in content:
            await message.channel.send(f'<@716390085896962058> c {pokemon_detected}')
        
        elif 'Regional Ping' in content or 'Regional ping' in content:
            await message.channel.send(f'<@716390085896962058> c {pokemon_detected}')
          
        elif 'Collection Pings' in content or 'Collection pings' in content:
            await message.channel.send(f'<@716390085896962058> c {pokemon_detected}')

        elif 'Shiny Hunt Pings' in content  or 'Shiny hunt pings' in content:
            await message.channel.send(f'<@716390085896962058> c {pokemon_detected}')     
    else:
        content = message.content
        solution = None

        if 'The pokémon is ' in content: ##collection pokemon
            solution = solve(content, 'collection.txt') 
              
@client.command()
@commands.has_permissions(administrator=True)
async def start(ctx):
    spam.start()
    await ctx.send('Started Spammer!')
    print(f'Started Spammer! ✅:')

@client.command()
@commands.has_permissions(administrator=True)
async def stop(ctx):
    spam.cancel()
    await ctx.send('Stopped Spammer!')
    print(f'Stopped Spammer! ✅:')



              
client.run(f"{user_token}")
