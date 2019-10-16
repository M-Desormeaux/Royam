import discord
from discord.ext import commands


class Roles(commands.Cog):
    def __init__(self, client):
        self.client = client

# {{{ Hidden On_Ready
#   @commands.Cog.listener()
#   async def on_ready(self):
#       print("=> roles")
# }}}
# {{{ ???
    @commands.command()
    async def role(self, ctx):
        await ctx.send('PlaceholderCmd')
# }}}


def setup(cog):
    cog.add_cog(Roles(cog))
