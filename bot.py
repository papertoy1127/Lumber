import discord
import asyncio
import time
import os
import json

client=discord.Client()

class vote:
    def __init__(self,subj,votes):
        self.subj = subj
        self.votes = votes
        self.votesAndCheck = []
        for i in self.votes:
            self.votesAndCheck.append([i,0])

    def getEmbed(self):
        self.embed = discord.Embed(title='주제 - [' + self.subj + ']', color=0x62c1cc)
        vote = self.votes
        for i in range(0, len(vote)):
            self.embed.add_field(name=i+1, value=vote[i], inline=False)
        return self.embed
    
    def getVotes(self):
        return self.votesAndCheck
    
    def getJson(self):
        self.json = {"subj":self.subj,"votes":self.votes,"votesAndCheck":self.votesAndCheck}
        return self.json
    def setByJson(self,jsonfile):
        self.subj = jsonfile.get('subj')
        self.votes = jsonfile.get('votes')
        self.votesAndCheck = jsonfile.get('votesAndCheck')
try:
    with open("vote_data.json", "r") as vote_json:
        vote_python = json.load(vote_json)
    nowvote = vote("",[""])
    nowvote.setByJson(vote_python)
except FileNotFoundError:
    nowvote=""

def doesNothing(txt):
    return txt

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
    global nowvote
    if message.author == client.user:
        return
    elif (message.content.split()[0]=="!embed"):
        try:
            await message.channel.send(embed=eval('embed(%s,foo="%s님의 임베드")' % (message.content.split(maxsplit=1)[1],message.author)))
            await message.delete()
        except Exception as inst:
            await message.channel.send("%s" % inst)
    if message.content.split()[0] == '!투표':
        if nowvote == "":
            await message.delete()
            votes = []
            for i in (message.content[4:].split("/")[1:]): #[1:]):
                votes.append(i)
            nowvote = vote(message.content[4:].split("/")[0],votes)
            await message.channel.send(embed=nowvote.getEmbed())
        else:
            await message.channel.send("이미 진행중인 투표가 있습니다.")
    if message.content.startswith("!투표하기"):
        if len(message.content.split()) <= 1:
            await message.channel.send("1~%d번의 숫자를 골라주세요." % len(nowvote.votes))
            return
        if (message.content.split()[1]).isdecimal():
            try:
                nowvote.votesAndCheck[int(message.content.split()[1])-1][1] += 1
                if int(message.content.split()[1]) < 1:
                    raise IndexError
                await message.delete()
                await message.author.send("성공적으로 %s번에 투표했습니다." % message.content.split()[1])
            except IndexError:
                await message.channel.send("1~%d번의 숫자를 골라주세요." % len(nowvote.votes))
            with open("vote_data.json", "w") as json_file:
                json.dump(nowvote.getJson(),json_file)
        else:
            await message.channel.send("1~%d번의 숫자를 골라주세요." % len(nowvote.votes))
    if message.content.startswith("!투표제거"):
        nowvote = ""
        os.remove("vote_data.json")
        await message.channel.send("투표가 제거되었습니다.")
    if message.content.startswith("!투표보기"):
        if nowvote == "":
            message.channel.send("현재 진행중인 투표가 없습니다.")
        await message.channel.send(embed=nowvote.getEmbed())
    if message.content.startswith("!투표수"):
        await message.channel.send(nowvote.getVotes())
        await message.channel.send("이 기능은 삭제예정입니다. 디버그를 위해 넣어놓은 기능")
    if message.content.startswith("!투표json"):
        await message.channel.send("test")
        with open("vote_data.json", "w") as json_file:
            json.dump(nowvote.getJson(),json_file)
access_token=os.environ["BOT_TOKEN"]
client.run(access_token)
