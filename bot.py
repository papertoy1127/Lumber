import discord
import asyncio
#import time
import os

client=discord.Client()

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
async def on_message(message):
    global qjsgh
    if message.author == client.user:
        return
    elif (message.content.split()[0]=="!embed"):
        try:
            await message.channel.send(embed=eval('embed(%s,foo="%s님의 임베드")' % (message.content.split(maxsplit=1)[1],message.author)))
            await message.delete()
        except:
            await message.channel.send("님 잘못쓴듯 아니면 봇 오류입니다")
'''    if message.content.startswith('!투표'):
        if True:
            await message.delete()
            qjsgh = 0
            vote = message.content[4:].split("/")
            embed = discord.Embed(title='주제 - [' + vote[0] + ']', color=0x62c1cc)
            for i in range(1, len(vote)):
                qjsgh += 1
                embed.add_field(name=qjsgh, value=vote[i], inline=False)
            choose = await message.channel.send(embed=embed)
            qjsgh = 0
            for i in range(1, len(vote)):
                qjsgh += 1
                if qjsgh == 1:
                    await choose.add_reaction('1️⃣')
                else:
                    if qjsgh == 2:
                        await choose.add_reaction('2️⃣')
                    else:
                        if qjsgh == 3:
                            await choose.add_reaction('3️⃣')
                        else:
                            if qjsgh == 4:
                                await choose.add_reaction('4️⃣')
                            else:    
                                if qjsgh == 5:
                                    await choose.add_reaction('5️⃣')
                                else:    
                                    if qjsgh == 6:
                                        await choose.add_reaction('6️⃣')
                                    else:
                                        if qjsgh == 7:
                                            await choose.add_reaction('7️⃣')
                                        else:
                                            if qjsgh == 8:
                                                await choose.add_reaction('8️⃣')
                                            else:
                                                if qjsgh == 9:
                                                    await choose.add_reaction('9️⃣')
                                                else:    
                                                    if qjsgh == 10:
                                                        await choose.add_reaction('🔟')
                                                    else:
                                                        await choose.add_reaction('🔢')'''

#access_token=os.environ["BOT_TOKEN"]
client.run("NzAwOTUyNzAxMzg2NzUyMDYw."+"Xp8INQ.AMWgUYw-ZcjZ3JYooghsutFPTPI")
