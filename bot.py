import discord
import asyncio
import time
import os
#from math import *

def doesNothing(txt):
    return txt
client=discord.Client()

def bmj():
    mym=""
    for i in range(random.randrange(15)):
        int(i)
        mym = mym+chr(random.randrange(0xAC00,0xD7A4))
    return mym

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('아무것도 안'))
        
def embed(title="제목",*args,des="",color=0x62c1cc,foo=""):
    embed = discord.Embed(title=str(title), description=str(des), color=color)
    embed.set_footer(text=str(foo))
    for i in args:
        if str(type(i))!="<class 'tuple'>":
            break
        if len(i)!=2:
            break
        embed.add_field(name=i[0], value=i[1], inline=True)
    return embed

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    '''ch = client.get_channel(701698774711402507)
    if message.channel == ch:
        return
    await ch.send("[%s:%s:%s:%s] %s" %(time.strftime('%c', time.localtime(time.time())),message.guild,message.channel,message.author,message.content))
    '''
    if message.author == client.user:
        return
    elif (message.content.split()[0]=="!embed"):
        try:
            await message.channel.send(embed=eval('embed(%s,foo="%s님의 임베드")' % (message.content.split(maxsplit=1)[1],message.author)))
            await message.delete()
        except:
           await message.channel.send("잘못된 구문입니다.")

#access_token=os.environ["BOT_TOKEN"]
client.run("NzAwOTUyNzAxMzg2NzUyMDYw."+"Xp8INQ.AMWgUYw-ZcjZ3JYooghsutFPTPI")
