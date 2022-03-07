#Created by Jc Gaming
#Not For Sale
#Join Discord Server for more Updates and More Private Content
# https://dsc.gg/DeepMods



import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive

import os

#-----SETUP-----#

prefix = "Pls "

#use the .env feature to hide your token

keep_alive()
token = os.getenv("TOKEN")
#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.command()
async def dhelp(ctx):
	await ctx.message.delete()
	await ctx.send('__**Dark Mega Grind**__: /n-  **Show all Commands** /n```Pls dhelp ``` /n -  **Runs 31 Commands with Risk of Dying** /n ```Pls infn```to run and ```Pls ricn``` to stop /n -  **Runs 31 Commands without Dying** / n```Pls infs``` to run and ```Pls rics``` to stop /n -  **Runs all Commands (you need to click buttons) /n*** ```Pls infa``` to run and ```Pls rica``` to stop /n-  **Runs Gamble Commands(you need more coins) /n*** ```Pls infg``` to run and ```Pls ricg``` to stop /n~~Features of this Mod:~~ /n***Undetected***✅ /n***Auto Farm***✅ /n***Anti-Ban***✅ /n***Get a lot of Commands Ran***✅ /n***Make Millions of Coins***✅ /n__Created by__ ***Jc Gaming*** /nJoin Discord Server for more Updates: /n***dsc.gg/DeepMods***')


@bot.command(pass_context=True)
async def infn(ctx):
	await ctx.message.delete()
	await ctx.send('Pls info')
	global dmcs
	dmcs = True
	while dmcs:
    async with ctx.typing():
      await asyncio.sleep(3)
    async with ctx.typing():
      await ctx.send('Pls beg')
      print(f"{Fore.GREEN}succefully use beg")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls fish')
      print(f"{Fore.GREEN}succefully use fish")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls dig')
      print(f"{Fore.GREEN}succefully use dig")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls hunt')
      print(f"{Fore.GREEN}succefully use hunt")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls with 1')
      print(f"{Fore.GREEN}succefully with 1")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls slots 1')
      print(f"{Fore.GREEN}succefully use slots 1")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multil")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls rich')
      print(f"{Fore.GREEN}succefully use rich")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls profile')
      print(f"{Fore.GREEN}succefully use profile ")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls shop')
      print(f"{Fore.GREEN}succefully use shop")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls drop')
      print(f"{Fore.GREEN}succefully use drop")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls dep max')
      print(f"{Fore.GREEN}succefully use dep max")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)


@bot.command()
async def ricn(ctx):
	await ctx.message.delete()
	await ctx.send('Pls Rich')
	global dmcs
	dmcs = False


@bot.command(pass_context=True)
async def infs(ctx):
	await ctx.message.delete()
	await ctx.send('Pls info')
	global dmsafe
	dmsafe = True
	while dmsafe:
    async with ctx.typing():
      await asyncio.sleep(3)
    async with ctx.typing():
      await ctx.send('Pls beg')
      print(f"{Fore.GREEN}succefully use beg")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls fish')
      print(f"{Fore.GREEN}succefully use fish")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls dig')
      print(f"{Fore.GREEN}succefully use dig")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls with 1')
      print(f"{Fore.GREEN}succefully use with 1")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls slots 1')
      print(f"{Fore.GREEN}succefully use slots 1")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multil")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls rich')
      print(f"{Fore.GREEN}succefully use rich")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls profile')
      print(f"{Fore.GREEN}succefully use profile ")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls shop')
      print(f"{Fore.GREEN}succefully use shop")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls drop')
      print(f"{Fore.GREEN}succefully use drop")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls dep max')
      print(f"{Fore.GREEN}succefully use dep max")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await a asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)

      
@bot.command()
async def rics(ctx):
	await ctx.message.delete()
	await ctx.send('Pls rich')
	global dmsafe
	dmsafe = False


@bot.command(pass_context=True)
async def infa(ctx):
	await ctx.message.delete()
	await ctx.send('Pls info')
	global dmcall
	dmcall = True
	while dmcall:
    async with ctx.typing():
      await asyncio.sleep(3)
    async with ctx.typing():
      await ctx.send('Pls beg')
      print(f"{Fore.GREEN}succefully use beg")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls fish')
      print(f"{Fore.GREEN}succefully use fish")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls dig')
      print(f"{Fore.GREEN}succefully use dig")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls hunt')
      print(f"{Fore.GREEN}succefully use hunt")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls hl')
      print(f"{Fore.GREEN}succefully use hl")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls search')
      print(f"{Fore.GREEN}succefully use search")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls trivia')
      print(f"{Fore.GREEN}succefully use trivia")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls pm')
      print(f"{Fore.GREEN}succefully use pm")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls crime')
      print(f"{Fore.GREEN}succefully use crime")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls with 1')
      print(f"{Fore.GREEN}succefully use with 1")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls se 1')
      print(f"{Fore.GREEN}succefully use se 1")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls profile')
      print(f"{Fore.GREEN}succefully use profile ")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls shop')
      print(f"{Fore.GREEN}succefully use shop")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls drop')
      print(f"{Fore.GREEN}succefully use drop")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls dep max')
      print(f"{Fore.GREEN}succefully use dep max")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls stream')
      print(f"{Fore.GREEN}succefully use stream")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bal')
      print(f"{Fore.GREEN}succefully use bal")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls multi')
      print(f"{Fore.GREEN}succefully use multi")
      await asyncio.sleep(2)

@bot.command()
async def rica(ctx):
	await ctx.message.delete()
	await ctx.send('Pls rich')
	global dmcall
	dmcall = False

@bot.command(pass_context=True)
async def infg(ctx):
	await ctx.message.delete()
	await ctx.send('Pls info')
	global dmgam
	dmgam = True
	while dmgam:
    async with ctx.typing():
      await asyncio.sleep(3
    async with ctx.typing():
      await ctx.send('Pls with 10k')
      print(f"{Fore.GREEN}succefully use with")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls gamble 1500')
      print(f"{Fore.GREEN}succefully use gamble")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls slots 1')
      print(f"{Fore.GREEN}succefully use slots")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls se 1500')
      print(f"{Fore.GREEN}succefully use se")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls bj 1500')
      print(f"{Fore.GREEN}succefully use bj")
      await asyncio.sleep(2)
    async with ctx.typing():
      await ctx.send('Pls scratch 1500')
      print(f"{Fore.GREEN}succefully use scratch")
      await asyncio.sleep(2)

@bot.command()
async def ricg(ctx):
	await ctx.message.delete()
	await ctx.send('Pls rich')
	global dmgam
	dmgam = False

bot.run(token, bot=False) 

#Created by Jc Gaming
#Not For Sale
#Join Discord Server for more Updates and More Private Content
# https://dsc.gg/DeepMods