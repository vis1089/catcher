import re, os, asyncio, random, string, discord
from discord.ext import commands, tasks

user_token = os.environ['token']
spam_id = os.environ['spam_id']
prefix = "."

poketwo = 716390085896962058
pokename = 874910942490677270
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
    if message.author.id == pokename:
      content = message.content
      
      if 'Rare Ping' in content:
        await message.channel.send('<@716390085896962058> h')
      
      elif 'Regional Ping' in content:
        await message.channel.send(f'<@716390085896962058> h')

      elif 'Collection Pings' in content:
        await message.channel.send(f'<@716390085896962058> h')

      elif 'Shiny Hunt Pings' in content:
        await message.channel.send(f'<@716390085896962058> h')        
    else:
            content = message.content
            solution = None
          
            if 'The pokémon is ' in content: ##collection pokemon
                    solution = solve(content, 'collection.txt') 
                    if solution:
                      await channel.clone()
                      category_name = 'Collection 1'
                      new_category = [c for c in message.guild.categories if c.name == category_name][0]
                      print(f"{category_name} category have {len(new_category.channels)} now! 🟢")
                      if len(new_category.channels) <= 48:
                       await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                      if len(new_category.channels) >= 48:
                       category_name = 'Collection 2'
                       old_category = channel.category
                       new_category = [c for c in message.guild.categories if c.name == category_name][0]
                       print(f"{category_name} category have {len(new_category.channels)} now! 🟢")
                       if len(new_category.channels) <= 48:
                        await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                       if len(new_category.channels) >= 48:
                        category_name = 'Collection 3'
                        old_category = channel.category
                        new_category = [c for c in message.guild.categories if c.name == category_name][0]
                        print(f"{category_name} category have {len(new_category.channels)} now! 🟢")
                        if len(new_category.channels) <= 48:
                         await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                        if len(new_category.channels) >= 48:
                          category_name = 'Collection 4'
                          old_category = channel.category
                          new_category = [c for c in message.guild.categories if c.name == category_name][0]
                          print(f"{category_name} category have {len(new_category.channels)} now! 🟢")
                          if len(new_category.channels) <= 48:
                           await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                          if len(new_category.channels) >= 48:
                            category_name = 'Collection 5'
                            old_category = channel.category
                            new_category = [c for c in message.guild.categories if c.name == category_name][0]
                            num_channels = len(new_category.channels)
                            print(f"{category_name} category have {len(new_category.channels)} now! 🟢")
                            if len(new_category.channels) <= 48:
                             await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                            if len(new_category.channels) >= 48:
                              category_name = 'Collection 6'
                              old_category = channel.category
                              new_category = [c for c in message.guild.categories if c.name == category_name][0]
                              num_channels = len(new_category.channels)
                              print(f"{category_name} category have {len(new_category.channels)} now! 🟢")
                              if len(new_category.channels) <= 48:
                               await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                              if len(new_category.channels) >= 48:
                                category_name = 'Collection 7'
                                old_category = channel.category
                                new_category = [c for c in message.guild.categories if c.name == category_name][0]
                                print(f"{category_name} category have {len(new_category.channels)} now! 🟢")
                                if len(new_category.channels) <= 48:
                                 await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                                if len(new_category.channels) >= 48:
                                  category_name = 'Collection 8'
                                  old_category = channel.category
                                  new_category = [c for c in message.guild.categories if c.name == category_name][0]
                                  print(f"{category_name} category have {len(new_category.channels)} now! 🟢")
                                  if len(new_category.channels) <= 48: 
                                   await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                                  if len(new_category.channels) >= 48:
                                    category_name = 'Collection 9'
                                    old_category = channel.category
                                    new_category = [c for c in message.guild.categories if c.name == category_name][0]
                                    print(f"{category_name} category have {len(new_category.channels)} now! 🟢")
                                    if len(new_category.channels) <= 48: 
                                     await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                                    if len(new_category.channels) >= 48:
                                      category_name = 'Collection 10'
                                      old_category = channel.category
                                      new_category = [c for c in message.guild.categories if c.name == category_name][0]
                                      print(f"{category_name} category have {len(new_category.channels)} now! 🟢")
                                      if len(new_category.channels) <= 48: 
                                       await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                      await channel.send(f'<@716390085896962058> redirect 1 2 3 4 5 6 7 8 9 10')
                      await asyncio.sleep(2)
                      await channel.edit(sync_permissions=True)
                      
                    if not solution: ##rare pokemon
                      solution = solve(content, 'rare.txt')
                      if solution:
                       await channel.clone()
                       category_name = 'Rare 1'
                       old_category = channel.category
                       new_category = [c for c in message.guild.categories if c.name == category_name][0]
                       print(f"{category_name} category have {len(new_category.channels)} now! 🟣")
                       if len(new_category.channels) <= 48:
                         await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                       if len(new_category.channels) >= 48:
                        category_name = 'Rare 2'
                        old_category = channel.category
                        new_category = [c for c in message.guild.categories if c.name == category_name][0]
                        print(f"{category_name} category have {len(new_category.channels)} now! 🟣")
                        if len(new_category.channels) <= 48:
                         await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                        if len(new_category.channels) >= 48:
                         category_name = 'Rare 3'
                         old_category = channel.category
                         new_category = [c for c in message.guild.categories if c.name == category_name][0]
                         print(f"{category_name} category have {len(new_category.channels)} now! 🟣")
                         if len(new_category.channels) <= 48:
                          await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                         if len(new_category.channels) >= 48:
                          category_name = 'Rare 4'
                          old_category = channel.category
                          new_category = [c for c in message.guild.categories if c.name == category_name][0]
                          print(f"{category_name} category have {len(new_category.channels)} now! 🟣")
                          if len(new_category.channels) <= 48:
                           await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                          if len(new_category.channels) >= 48:
                            category_name = 'Rare 5'
                            old_category = channel.category
                            new_category = [c for c in message.guild.categories if c.name == category_name][0]
                            print(f"{category_name} category have {len(new_category.channels)} now! 🟣")
                            if len(new_category.channels) <= 48:
                             await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                       await channel.send(f'<@716390085896962058> redirect 1 2 3 4 5 6 7 8 9 10')
                       await asyncio.sleep(2)
                       await channel.edit(sync_permissions=True)

                    if not solution: ##regional pokemon
                      solution = solve(content, 'regional.txt')
                      if solution:
                       await channel.clone()
                       category_name = 'Regional 1'
                       old_category = channel.category
                       new_category = [c for c in message.guild.categories if c.name == category_name][0]
                       print(f"{category_name} category have {len(new_category.channels)} now! 🟠")
                       if len(new_category.channels) <= 48:
                         await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                       if len(new_category.channels) >= 48:
                        category_name = 'Regional 2'
                        old_category = channel.category
                        new_category = [c for c in message.guild.categories if c.name == category_name][0]
                        print(f"{category_name} category have {len(new_category.channels)} now! 🟠")
                        if len(new_category.channels) <= 48:
                         await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                        if len(new_category.channels) >= 48:
                         category_name = 'Regional 3'
                         old_category = channel.category
                         new_category = [c for c in message.guild.categories if c.name == category_name][0]
                         print(f"{category_name} category have {len(new_category.channels)} now! 🟠")
                         if len(new_category.channels) <= 48:
                          await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                         if len(new_category.channels) >= 48:
                          category_name = 'Regional 4'
                          old_category = channel.category
                          new_category = [c for c in message.guild.categories if c.name == category_name][0]
                          print(f"{category_name} category have {len(new_category.channels)} now! 🟠")
                          if len(new_category.channels) <= 48:
                           await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                          if len(new_category.channels) >= 48:
                            category_name = 'Regional 5'
                            old_category = channel.category
                            new_category = [c for c in message.guild.categories if c.name == category_name][0]
                            print(f"{category_name} category have {len(new_category.channels)} now! 🟠")
                            if len(new_category.channels) <= 48:
                             await channel.edit(name=solution[0].lower().replace(' ', '-'), category=new_category)
                       await channel.send(f'<@716390085896962058> redirect 1 2 3 4 5 6 7 8 9 10')
                       await asyncio.sleep(2)
                       await channel.edit(sync_permissions=True)
                      
                      if not solution: ## normal pokemon
                       solution = solve(content, 'pokemon.txt')
                       if solution:
                         #await message.channel.send(f'c {solution[0]}')
                         await asyncio.sleep(2)
            else:
               await asyncio.sleep(1)
            if 'human' in content:
                    spam.cancel()
                    channel = client.get_channel(int(spam_id))
                    await channel.send(f'<@&{admin_id}> Captcha Dectected')
              
    if not message.author.bot:
         await client.process_commands(message)
  
@client.command()
@commands.has_permissions(manage_channels=True)
async def say(ctx, *, args):
  await ctx.send(args)

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You require the manage channel permission to use this command")
      
@client.command()
@commands.has_permissions(manage_channels=True)
async def delete(ctx):
  await ctx.channel.delete()
  print(f'Channel Deleted ✅:')

@delete.error
async def delete_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You require the manage channel permission to use this command")
  
@client.command()
@commands.has_permissions(manage_channels=True)
async def clone(ctx):
  await ctx.channel.clone()
  await ctx.send('Cloned')
  print(f'Channel Cloned ✅:')
  
@clone.error
async def clone_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You require the manage channel permission to use this command")

@client.command()
@commands.has_permissions(administrator=True)
async def start(ctx):
  spam.start()
  await ctx.send('Started Spammer!')
  print(f'Started Spammer! ✅:')

@start.error
async def start_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You require the administrator permission to use this command")
      
@client.command()
@commands.has_permissions(administrator=True)
async def stop(ctx):
  spam.cancel()
  await ctx.send('Stopped Spammer!')
  print(f'Stopped Spammer! ✅:')

@stop.error
async def stop_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You require the administrator permission to use this command")


print(f'*'*25)
print(f'Made by PlayHard ✅:')
print(f'*'*25)
client.run(f"{user_token}")
