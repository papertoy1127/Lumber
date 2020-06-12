import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="???", case_insensitive=True)
whiteListedRoles = ["Map Editor", "Gamer"]
admin = "Manager"

@bot.event
async def on_ready():
    print("Ready!")
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('???Rank Gamer/Map Editor'))

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
            await ctx.send(embed=discord.Embed(description = ctx.author.mention + ' 님에게서 ' + giveRole.mention + '역할이 삭제되었습니다.'))
        else:
            await ctx.author.add_roles(giveRole)
            await ctx.send(embed=discord.Embed(description = ctx.author.mention + ' 님에게 ' + giveRole.mention + '역할이 지급되었습니다.'))
    else:
        await ctx.send(embed=discord.Embed(description = '지급이 불가능한 역할입니다.'))
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

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token, bot=True, reconnect=True)
