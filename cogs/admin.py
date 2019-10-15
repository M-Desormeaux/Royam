import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

#   @commands.Cog.listener()
#   async def on_ready(self):
#       print("=> admin")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong! 🏓')


def setup(cog):
    cog.add_cog(Admin(cog))
