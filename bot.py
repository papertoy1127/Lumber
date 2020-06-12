import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="???", case_insensitive=True)
whiteListedRoles = ["Map Editor", "Gamer"]
admin = "Manager"

@bot.event
async def on_ready():
  print("Ready!")

@bot.command(pass_context=True)
async def rank(ctx, *args):
    role = ''
    for i in args:
        role += i
        role += ' '
    role = role[:-1]
    print(role)
    if role in whiteListedRoles:
        giveRole = discord.utils.get(ctx.guild.roles, name=role)
        if giveRole in ctx.author.roles:
            await ctx.author.remove_roles(giveRole)
        else:
            await ctx.author.add_roles(giveRole)
@bot.command(pass_context=True)
async def clear(ctx, amount):
        adminRole = discord.utils.get(ctx.guild.roles, name=admin)
        try:
            if adminRole in ctx.author.roles:
                await ctx.channel.purge(limit = int(amount))
            else:
                raise discord.ext.commands.errors.CommandInvokeError
        except Exception as E:
            raise E
            #await ctx.send('권한이 부족합니다!' + str(E))

access_token = 'NzAwNTM1OTA3MjExODA0Njcy.XuMO9A.NVkPZSXZv9MRiN314xVzUJh22Iw'
bot.run(access_token, bot=True, reconnect=True)
