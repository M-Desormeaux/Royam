import discord

import os
from discord.ext import commands

token = open("token.txt", "r").readline()
bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="The Server"))
    print("Bot ready to interact")

@bot.command()
    async def ping(self, ctx):
        await ctx.send('Pong! 🏓')

@bot.command()
async def load(ctx, extension):
    try:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send('Cog enabled')
        print(f'> Cog Loaded: {extension}')
    except:
        await ctx.send('Cog not found')

@bot.command()
async def unload(ctx, extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send('Cog disabled')
        print(f'> Cog UnLoaded: {extension}')
    except:
        await ctx.send('Cog not found')

@bot.command()
async def cycle(ctx):
    await ctx.send('Reloading Cogs...')
    print('Reloading all cogs')
    try:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.unload_extension(f'cogs.{filename[:-3]}')
    except:
        pass
    try:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')
                await ctx.send(f'> Cog Loaded: {filename[:-3]}')
    except:
        pass
    await ctx.send('Cogs Reloaded')

print('\nCogs Loaded:')
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename[:-3]}')
print('')

bot.run(token.strip())