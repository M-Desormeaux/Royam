import discord
from discord.ext import commands


class Server(commands.Cog):
    def __init__(self, client):
        self.client = client