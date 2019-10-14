# {{{ Imports
import discord
from discord.ext import commands
# }}}

token = open("token.txt", "r").readline()

bot = commands.Bot(command_prefix=',')

# {{{ On_Ready
@bot.event
async def on_ready():
    print("\n\nLogged in as Royam!\nReady to Work!\n")
# }}}

# {{{ Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')
# }}}

# {{{ Echo
@bot.command()
async def echo(ctx, *args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await ctx.send(output)
# }}}

bot.run(token.strip())
