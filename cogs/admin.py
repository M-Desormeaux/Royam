import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

# {{{ Hidden On_Ready
#   @commands.Cog.listener()
#   async def on_ready(self):
#       print("=> admin")
# }}}

# {{{ Ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong! 🏓')
# }}}

# {{{ Clear
    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)
# }}}

# {{{ Kick
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        if reason is None:
            await ctx.send(f'{member.mention} was kicked')
        else:
            await ctx.send(f'{member.mention} was kicked for {reason}')
# }}}

# {{{ Ban
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        if reason is None:
            await ctx.send(f'{member.mention} was banned')
        else:
            await ctx.send(f'{member.mention} was banned for {reason}')
# }}}

# {{{ Unban
    @commands.command()
    async def unban(self, ctx, member: discord.Member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} unbanned')
                return
# }}}


def setup(cog):
    cog.add_cog(Admin(cog))