import discord
from discord.ext import commands
import datetime
import random
import requests

bot = commands.Bot(command_prefix="!", intents= discord.Intents.all())
bot.remove_command("help")


def get_duck_image_url():    
  url = 'https://random-d.uk/api/random'
  res = requests.get(url)
  data = res.json()
  return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Po wywołaniu polecenia duck program wywołuje funkcję get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.event
async def on_ready():
    print("The bot is now online!")

@bot.command()
async def hello(ctx):
    username=ctx.message.author.mention
    await ctx.send("hello" + username)


@bot.command()
async def lfg(ctx):
    channel= "Please go to <#1188989608566992937>"
    username= ctx.message.author.mention
    await ctx.send(username + channel + "to play with other :)")

@bot.command()
@commands.has_any_role("Owner", "Administrator" ,"Moderator" )
async def ban(ctx, member:discord.member, * , reason:None):
    if reason == None:
        reason = "This user has been banned by" + ctx.message.author.name
        await member.ban(reason=reason)
        await ctx.send(f"***{member.name} was banned***")
        midlegs= bot.get_channel(1189293177954369587)
        await ctx.send(f"{member.name} was banned by {ctx.author.mention}")

@bot.command()
@commands.has_any_role("Owner", "Administrator" ,"Moderator" )
async def kick(ctx, member:discord.member, * , reason:None):
    if reason == None:
        reason = "This user has been kicked by" + ctx.message.author.name
        await member.kick(reason=reason)
        await ctx.send(f"***{member.name} was kicked***")
        midlegs= bot.get_channel(1189293177954369587)
        await ctx.send(f"{member.name} was kicked by {ctx.author.mention}")


@bot.command()
@commands.has_any_role("Owner", "Administrator" ,"Moderator" )
async def mute(ctx, member:discord.Member, timelimit):
    if "s" in timelimit:
        gettime= timelimit.strip("s")
        if int(gettime) > 241900:
            print("The time out is too long!")
        else:
            newtime = datetime.timedelta(seconds=int(gettime))
            await member.edit(timed_out_until= discord.utils.utcnow() + newtime)
            midlegs= bot.get_channel(1189293177954369587)
            await ctx.send(f"{member.name} was muted for {str(gettime)} seconds by {ctx.message.author.mention}")
    elif "m" in timelimit:
        gettime= timelimit.strip("m")
        if int(gettime) > 43200:
            print("The time out is too long!")
        else:
            newtime = datetime.timedelta(minutes=int(gettime))
            await member.edit(timed_out_until= discord.utils.utcnow() + newtime)
            midlegs= bot.get_channel(1189293177954369587)
            await ctx.send(f"{member.name} was muted for {str(gettime)} minutes by {ctx.message.author.mention}")
    elif "h" in timelimit:
        gettime= timelimit.strip("h")
        if int(gettime) > 672:
            print("The time out is too long!")
        else:
            newtime = datetime.timedelta(hours=int(gettime))
            await member.edit(timed_out_until= discord.utils.utcnow() + newtime)
            midlegs= bot.get_channel(1189293177954369587)
            await ctx.send(f"{member.name} was muted for {str(gettime)} hours by {ctx.message.author.mention}")
    elif "d" in timelimit:
        gettime= timelimit.strip("h")
        if int(gettime) > 28:
            print("The time out time is too long!")
        else:
            newtime = datetime.timedelta(days=int(gettime))
            await member.edit(timed_out_until= discord.utils.utcnow() + newtime)
            midlegs= bot.get_channel(1189293177954369587)
            await ctx.send(f"{member.name} was muted for {str(gettime)} days by {ctx.message.author.mention}")

@bot.command()
@commands.has_any_role("Owner", "Moderator", "Administrator")
async def unmute(ctx, member:discord.Member):
    await member.edit(timed_out_until= None)
    midlegs= bot.get_channel(1189293177954369587)
    await ctx.send(f"{member.name} was umuted by {ctx.message.author.mention}")


@bot.command()
async def help(ctx):
    embed= discord.Embed(title="Command Hub", description="This command displays all the commands you can do!", color=0x020ff)
    embed.add_field(name="!ban", value="this command can ban a user",inline=False)
    embed.add_field(name="!hello", value="this command makes the bot say hello back to user",inline=False)
    embed.add_field(name="!kick", value="this command can kick a user", inline=False)
    embed.add_field(name="!unmute", value="this command can unmute a user", inline=False)
    embed.add_field(name="!mute", value="this command can mute a user", inline=False)
    embed.add_field(name="!lfg", value="channel to play with other people" ,inline=False)
    embed.add_field(name="!help", value="this command displays all the commands you can do!", inline=False)
    embed.add_field(name="!coinflip", value="coinflip game", inline=False)
    embed.add_field(name="!emoji", value="this command generates an emoji", inline=False)
    embed.add_field(name="!number", value="this command can generate a random number", inline=False)
    embed.add_field(name="!double", value="double letter when a word is inputed", inline=False)
    embed.add_field(name="!library", value="this command can define slang words", inline=False)
    embed.add_field(name="!jk", value="this command generates a joke", inline=False)
    embed.add_field(name="!password", value="this command can generate a password", inline=False)
    embed.add_field(name="!developer", value="this command shows developer who made spacerV2", inline=False)
    embed.add_field(name="!social", value="pick from instagram/twitter/youtube/twitch", inline=False)
    embed.add_field(name="!name", value="this command can generate random name", inline=False)
    embed.add_field(name="!clr", value="this command can generate random colour", inline=False)
    embed.add_field(name="!comp", value="this command can help user with finding competition channel", inline=False)
    embed.add_field(name="!invite", value="this command gives you the link to the server", inline=False)
    embed.add_field(name="!song", value="this command displays best songs!!!", inline= False)
    embed.add_field(name="!meme", value="this command displays random meme", inline=False)
    embed.add_field(name="!logo", value="this command displays the bots logo", inline=False)
    embed.add_field(name="!duck", value="this command shows funny duck videos and pictures", inline=False)
    embed.add_field(name="!rps", value="this command is a rock paper scissors game", inline=False)
    embed.set_footer(text="This bot is made by Hugo B")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_any_role("Owner", "Administrator" ,"Moderator")
async def coinflip(ctx):
  num = random.randint(1,10)
  computer = random.randint(1,10)
  if num == computer:
    await ctx.send("Its a tie!!!")
  elif num > computer:
    await ctx.send(f"{ctx.message.author.mention} You won!!!!!!!!!")
  else:
    await ctx.send(f"{ctx.message.author.mention} Computer won :(")


@bot.command()
async def emoji(ctx):
  with open("emji.txt", "r") as file:
    a = random.choice(file.readlines())
    await ctx.send(f"{ctx.message.author.mention} This is your generated emoji:   " + a)

@bot.command()
@commands.has_any_role( "Owner", "Administrator" ,"Moderator")
async def number(ctx):
  num = random.randint(1,10000000)
  await ctx.send(num)

@bot.command()
@commands.has_any_role( "Owner", "Administrator" ,"Moderator")
async def double(ctx, str):
  result = ''
  for letter in str:
      result += letter * 2
  await ctx.send(result)

@bot.command()
@commands.has_any_role( "Owner", "Administrator" ,"Moderator")
async def library(ctx):
  library = {
      "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
      "LOL": "Częsta reakcja na coś zabawnego",
      "ROFL": "odpowiedź na żart",
      "SHEESH" : "lekka dezaprobata",
      "CREEPY": "straszny, złowieszczy",
      "AGGRO": "stać się agresywnym/zły",
      }
  word = ctx.message.content.split()[1].upper()
  if word in library:
      await ctx.send(library[word])
  else:
      await ctx.send("Sorry, that word is not in the library.")

@bot.command()
async def password(ctx):
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ213413253245436546"
  x = ''.join(random.choice(characters) for i in range(10))
  await ctx.send(f"{ctx.message.author.mention} this is your generated password: {x}")

@bot.command()
async def developer(ctx):
  await ctx.send("This bot was made by Hugo B")

@bot.command()
async def social(ctx, platform):
  if platform == "youtube":
    await ctx.send("This is my youtube: "+"https://www.youtube.com/@discord")
  elif platform == "twitch":
    await ctx.send("My twitch: " "https://www.twitch.tv/coolez1234")
  elif platform == "twitter":
    await ctx.send("My twitter: " + "https://twitter.com/discord")
  elif platform == "instagram":
    await ctx.send("My instagram: " + "https://www.instagram.com/discord/")
  else:
    await ctx.send("Sorry, that platform is not supported.")

@bot.command()
async def name(ctx):
    with open("name.txt", "r") as file:
      a = random.choice(file.readlines())
      await ctx.send(a)


@bot.command()
async def clr(ctx):
    with open("clr.txt", "r") as file:
      a = random.choice(file.readlines())
      await ctx.send("Your generated colour is :  " + a)

@bot.command()
async def comp(ctx):
  x = "<#1212461269185990686>"
  a = ctx.message.author.mention
  await ctx.send(f"{a} To find out more about upcoming competions: " + x)

@bot.command()
async def invite(ctx):
  inv = "https://discord.gg/muAAjVmn"
  await ctx.send(f"{ctx.message.author.mention} this is the invite link: {inv}")

@bot.command()
@commands.has_any_role("Owner")
async def read(ctx):
  with open("discordbot.txt", "r") as file:
    i = file.readlines()
    channel = bot.get_channel(1189293177954369587)
  await channel.send(f"{ctx.message.author.mention} these are the mod log reports: ")
  await channel.send("\n".join(i))

@bot.command()
@commands.has_any_role("Owner")
async def r(ctx, reason, date, member:discord.Member):
  with open("discordbot.txt", "a") as file:
    file.write(f"{reason} {date} {member.name}\n")
  await ctx.send(f"Report done by {ctx.message.author.mention}")


@bot.command()
@commands.has_any_role("Owner", "Administrator", "Moderator")
async def clear(ctx):
  await ctx.send("Clearing...")
  await ctx.channel.purge()

@bot.command()
@commands.has_any_role("Owner", "Administrator", "Moderator")
async def shelp(ctx):
    embed= discord.Embed(title="Command Hub", description="This command displays all the commands you can do!", color=0x020ff)
    embed.add_field(name="!ban", value="this command can ban a user",inline=False)
    embed.add_field(name="!hello", value="this command makes the bot say hello back to user",inline=False)
    embed.add_field(name="!kick", value="this command can kick a user", inline=False)
    embed.add_field(name="!unmute", value="this command can unmute a user", inline=False)
    embed.add_field(name="!mute", value="this command can mute a user", inline=False)
    embed.add_field(name="!lfg", value="channel to play with other people" ,inline=False)
    embed.add_field(name="!help", value="this command displays all the commands you can do!", inline=False)
    embed.add_field(name="!coinflip", value="coinflip game", inline=False)
    embed.add_field(name="!emoji", value="this command generates an emoji", inline=False)
    embed.add_field(name="!number", value="this command can generate a random number", inline=False)
    embed.add_field(name="!double", value="double letter when a word is inputed", inline=False)
    embed.add_field(name="!library", value="this command can define slang words", inline=False)
    embed.add_field(name="!jk", value="this command generates a joke", inline=False)
    embed.add_field(name="!password", value="this command can generate a password", inline=False)
    embed.add_field(name="!developer", value="this command shows developer who made spacerV2", inline=False)
    embed.add_field(name="!social", value="pick from instagram/twitter/youtube/twitch", inline=False)
    embed.add_field(name="!name", value="this command can generate random name", inline=False)
    embed.add_field(name="!clr", value="this command can generate random colour", inline=False)
    embed.add_field(name="!comp", value="this command can help user with finding competition channel", inline=False)
    embed.add_field(name="!invite", value="this command gives you the link to the server", inline=False)
    embed.add_field(name="!r", value="this command is to report bad behaviour", inline=False)
    embed.add_field(name="!clear", value="this command clears chat", inline=False)
    embed.add_field(name="!read", value="this command lets you look at records", inline=False)
    embed.set_footer(text="This bot is made by Hugo B")
    embed.add_field(name="!song", value="this command displays best songs!!!", inline= False)
    channel = bot.get_channel(1189293177954369587)
    await channel.send(embed=embed)

@bot.command()
async def song(ctx):
  embed= discord.Embed(title="Best songs", description="This command displays the best tunes!!", color=0x020ff)
  embed.add_field(name="1: ", value="song 1", inline=False)
  embed.add_field(name="2: ", value="song 2", inline=False)
  embed.add_field(name="3: ", value="song 3", inline=False)
  await ctx.send(embed=embed)
  
@bot.command()
async def jk(ctx):
  with open("jk.txt", "r") as file:
    a = random.choice(file.readlines())
    await ctx.send(a)
      
@bot.command()
async def logo(ctx):
  with open('chatbot.jpg', 'rb') as f:
    picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def meme(ctx):
    x = random.randint(1,3)
    meme1 = (f"mem{x}.jpg")
    with open(f'meme/{meme1}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def rps(ctx, user):
  computer=random.choice(["rock", "paper", "scissors"])
  while user.upper() != "ROCK" and user.upper() != "PAPER" and user.upper() != "SCISSORS":
    await ctx.send("Invalid input. Please choose rock, paper, or scissors.")
    return
    
  if user.upper() == computer.upper():
    await ctx.send(f"Its a tie {ctx.message.author.mention}")
  elif computer.upper() == "ROCK" and user.upper() == "SCISSORS":
    await ctx.send(f"Computer wins! {ctx.message.author.mention}")
  elif computer.upper() == "PAPER" and user.upper() == "ROCK":
    await ctx.send(f"Computer wins! {ctx.message.author.mention}")
  elif computer.upper() == "SCISSORS" and user.upper() == "PAPER":
    await ctx.send(f"Computer wins! {ctx.message.author.mention}")
  elif user.upper() == "END":
    await ctx.send(f"See you later :) {ctx.message.author.mention}")
  else:
    await ctx.send(f"You picked option {user} and won!!! {ctx.message.author.mention}")

@bot.event
async def on_member_join(member):
    logschannel= bot.get_channel(1189289751363203112)
    embed=discord.Embed(title="New Member!", description=f"{member.mention} joined the server!!", color=0xFA9F00)
    embed.set_footer(text="Hope you enjoy the server!!")
    await logschannel.send(embed=embed)

@bot.event
async def on_member_leave(member):
    logschannel= bot.get_channel(1189289751363203112)
    embed=discord.Embed(title="Left server", description=f"{member.mention} left the server!!", color=0x0035FA)
    embed.set_footer(text="Sad to see you go :(")
    await logschannel.send(embed=embed)

bot.run("BOT TOKEN")
