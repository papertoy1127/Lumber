import discord
import asyncio
import time
import os
#from math import *

def doesNothing(txt):
    return txt
client=discord.Client()

def embed(title="제목",*args,des="",color=0x62c1cc,foo=""):
    global em
    embed = discord.Embed(title=str(title), description=str(des), color=color)
    embed.set_footer(text=str(foo))
    for i in args:
        if str(type(i))!="<class 'tuple'>":
            break
        if len(i)!=2:
            break
        embed.add_field(name=i[0], value=i[1], inline=True)
    em=embed

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    #await message.channel.send("test")
    if message.author == client.user:
        return
    elif (message.content.split()[0]=="!embed"):
        try:
            eval("embed(%s,foo="%s님의 임베드")" % message.content.split(maxsplit=1)[1],message.author.mention)
            await message.channel.send(embed=em)
        except:
            await message.channel.send("잘못된 구문입니다.")
    elif (message.content=="!MEE6 MEE6"):
        await message.channel.send("Not A MEE6")
    elif (message.content.split()[0]=="!me"):
        await message.channel.send(str(message.author.mention))
    elif (message.content.split()[0]=="!you"):
        await message.delete()
        await message.channel.send(message.content.split(maxsplit=1)[1])
    elif (message.content.split()[0]=="!각도계산"):
        if message.content=="!각도계산":
            await message.channel.send("!각도계산 <계산할 각도>")
        else:
            getAngle=str(message.content.split(maxsplit=1)[1])
            if "/" in getAngle:
                relativeAngle=int(eval(getAngle)*7)
            elif getAngle.isnumeric():
                relativeAngle=int(getAngle)*7
            else:
                await message.channel.send("```%s도는 현재 얼불춤에서 만들 수 없습니다.```" % (getAngle))
                return
            print(relativeAngle)
            if getAngle=="360":
                await message.channel.send("```스페이스 바를 눌러 360도를 만들 수 있습니다.```")
                return
            if getAngle=="0":
                await message.channel.send("```탭 키를 눌러 탭드스핀을 만들 수 있습니다.\n실제 미드스핀을 원하신다면, 연구에 참여해주세요!```")
                return
            angles=(0,30,45,60,90,120,135,150,180,210,225,240,270,300)
            check=0
            sendMsg="```\n"
            for i in angles:
                #print(i)
                for j in angles:
                    #print(j)
                    for k in range(5):
                        #print(k)
                        for m in range(7):
                            #print(m)
                            if relativeAngle==(((7*i+7*108*k+900*m)-7*j)%2520):
                                print(str((((7*i+7*108*k+900*m))-7*j)%2520)+":")
                                check+=1
                                if k==0:
                                    if m==0:
                                        sendMsg=sendMsg+("%d도와 %d도로 %d도를 만들 수 있습니다." % ((i+108*k+(900/7)*m)%360,j,relativeAngle/7))+"\n"
                                    else:
                                        sendMsg=sendMsg+("%f도(%d + (900/7 × %d)도)와 %d도로 %s도를 만들 수 있습니다." % ((i+108*k+(900/7)*m)%360,i,m,j,getAngle))+"\n"
                                else:
                                    if m==0:
                                        sendMsg=sendMsg+("%d도(%d + (108 × %d)도)와 %d도로 %d도를 만들 수 있습니다." % ((i+108*k+(900/7)*m)%360,i,k,j,relativeAngle/7))+"\n"
                                    else:
                                        sendMsg=sendMsg+("%f도(%d + (108 × %d) + (900/7 × %d)도)와 %d도로 %s도를 만들 수 있습니다." % ((i+108*k+(900/7)*m)%360,i,k,m,j,getAngle))+"\n"
                           
            if check==0:
                await message.channel.send("```%s도는 현재 얼불춤에서 만들 수 없습니다.```" % (getAngle))
            else:
                await message.channel.send(sendMsg+"```")

access_token=os.environ["BOT_TOKEN"]
client.run(access_token)

