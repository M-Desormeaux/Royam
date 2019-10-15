import discord
import os
from discord.ext import commands

token = open("token.txt", "r").readline()
bot = commands.Bot(command_prefix='.')

# {{{ On_Ready
@bot.event
async def on_ready():
    print("Bot ready to interact")
# }}}

# {{{ Cogs
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
async def reload(ctx, extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        await ctx.send('Cog reloaded')
        print(f'> Cog Reloaded: {extension}')
    except:
        await ctx.send('Cog not found')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'> Cog Loaded: {filename[:-3]}')
# }}}
bot.run(token.strip())
