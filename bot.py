import discord
import asyncio
import time
import os
import json

client=discord.Client()
badWords=['10새', '10새기', '10새리', '10세리', '10쉐이', '10쉑', '10스', '10쌔', ' 10쌔기', '10쎄', '10알', '10창', '10탱', '18것', '18넘', '18년', '18노', '18놈', '18뇬', '18럼', '18롬', '18새', '18새끼', '18색', '18세끼', '18세리', '18섹', '18쉑', '18스', '18아', 'ㄱㅐ', 'ㄲㅏ', 'ㄲㅑ', 'ㄲㅣ', 'ㅅㅂㄹㅁ', 'ㅅㅐ', 'ㅆㅂㄹㅁ', 'ㅆㅍ', 'ㅆㅣ', 'ㅆ앙', 'ㅍㅏ', '凸', ' 갈보', '갈보년', '강아지', '같은년', '같은뇬', '개같은', '개구라', '개년', '개놈', '개뇬', '개대중', '개독', '개돼중', '개랄', '개보지', '개뻥', '개뿔', '개새', '개새기', '개새끼', '개새키', '개색기', '개색끼', '개색키', '개색히', '개섀끼', '개세', '개세끼', '개세이', '개소리', '개쑈', ' 개쇳기', '개수작', '개쉐', '개쉐리', '개쉐이', '개쉑', '개쉽', '개스끼', '개시키', '개십새기', ' 개십새끼', '개쐑', '개씹', '개아들', '개자슥', '개자지', '개접', '개좆', '개좌식', '개허접', '걔새', '걔수작', '걔시끼', '걔시키', '걔썌', '걸레', '게색기', '게색끼', '광뇬', '구녕', '구라', '구멍', '그년', '그새끼', '냄비', '놈현', '뇬', '눈깔', '뉘미럴', '니귀미', '니기미', '니미', '니미랄', '니미럴', '니미씹', '니아배', '니아베', '니아비', '니어매', '니어메', '니어미', '닝기리', '닝기미', '대가리', '뎡신', '도라이', '돈놈', '돌아이', '돌은놈', '되질래', '뒈져', '뒈져라', '뒈진', '뒈진다', '뒈질', ' 뒤질래', '등신', '디져라', '디진다', '디질래', '딩시', '따식', '때놈', '또라이', '똘아이', '똘아이', '뙈놈', '뙤놈', '뙨넘', '뙨놈', '뚜쟁', '띠바', '띠발', '띠불', '띠팔', '메친넘', '메친놈', '미췬', ' 미췬', '미친', '미친넘', '미친년', '미친놈', '미친새끼', '미친스까이', '미틴', '미틴넘', '미틴년', ' 미틴놈', '바랄년', '병자', '뱅마', '뱅신', '벼엉신', '병쉰', '병신', '부랄', '부럴', '불알', '불할', '붕가', '붙어먹', '뷰웅', '븅', '븅신', '빌어먹', '빙시', '빙신', '빠가', '빠구리', '빠굴', '빠큐', '뻐큐', '뻑큐', '뽁큐', '상넘이', '상놈을', '상놈의', '상놈이', '새갸', '새꺄', '새끼', '새새끼', '새키', '색끼', '생쑈', '세갸', '세꺄', '세끼', '섹스', '쇼하네', '쉐', '쉐기', '쉐끼', '쉐리', '쉐에기', '쉐키', '쉑', '쉣', '쉨', '쉬발', '쉬밸', '쉬벌', '쉬뻘', '쉬펄', '쉽알', '스패킹', '스팽', '시궁창', '시끼', '시댕', '시뎅', '시랄', '시발', '시벌', '시부랄', '시부럴', '시부리', '시불', '시브랄', '시팍', '시팔', '시펄', '신발끈', '심발끈', '심탱', '십8', '십라', '십새', '십새끼', '십세', '십쉐', '십쉐이', '십스키', '십쌔', '십창', '십탱', '싶알', '싸가지', '싹아지', '쌉년', '쌍넘', '쌍년', '쌍놈', '쌍뇬', '쌔끼', ' 쌕', '쌩쑈', '쌴년', '썅', '썅년', '썅놈', '썡쇼', '써벌', '썩을년', '썩을놈', '쎄꺄', '쎄엑', ' 쒸벌', '쒸뻘', '쒸팔', '쒸펄', '쓰바', '쓰박', '쓰발', '쓰벌', '쓰팔', '씁새', '씁얼', '씌파', '씨8', ' 씨끼', '씨댕', '씨뎅', '씨바', '씨바랄', '씨박', '씨발', '씨방', '씨방새', '씨방세', '씨밸', '씨뱅', '씨벌', '씨벨', '씨봉', '씨봉알', '씨부랄', '씨부럴', '씨부렁', '씨부리', '씨불', '씨붕', '씨브랄', ' 씨빠', '씨빨', '씨뽀랄', '씨앙', '씨파', '씨팍', '씨팔', '씨펄', '씸년', '씸뇬', '씸새끼', '씹같', '씹년', '씹뇬', '씹보지', '씹새', '씹새기', '씹새끼', '씹새리', '씹세', '씹쉐', '씹스키', '씹쌔', '씹이', '씹자지', '씹질', '씹창', '씹탱', '씹퇭', '씹팔', '씹할', '씹헐', '아가리', '아갈', '아갈이', '아갈통', '아구창', '아구통', '아굴', '얌마', '양넘', '양년', '양놈', '엄창', '엠병', '여물통', '염병', '엿같', '옘병', '옘빙', '오입', '왜년', '왜놈', '욤병', '육갑', '은년', '을년', '이년', '이새끼', '이새키', '이스끼', '이스키', '임마', '자슥', '잡것', '잡넘', '잡년', '잡놈', '저년', '저새끼', '접년', '젖밥', '조까', '조까치', '조낸', '조또', '조랭', '조빠', '조쟁이', '조지냐', '조진다', '조찐', '  조질래', '존나', '존나게', '존니', '존만', ' 존만한', '좀물', '좁년', '좆', '좁밥', '좃까', '좃또', '좃만', '좃밥', '좃이', '좃찐', '좆같', '좆까', '좆나', '좆또', '좆만', '좆밥', '좆이', '좆찐', '좇같', '좇이', '좌식', '주글', '주글래', '주데이', '주뎅', '주뎅이', '주둥아리', '주둥이', '주접', '주접떨', '죽고잡', '죽을래', '죽통', '쥐랄', '쥐롤', '쥬디', '지랄', '지럴', '지롤', '지미랄', '짜식', '짜아식', '쪼다', '쫍빱', '찌랄', '창녀', '캐년', '캐놈', '캐스끼', '캐스키', '캐시키', '탱구', '팔럼', '퍽큐', '호로', '호로놈', '호로새끼', '호로색', '호로쉑', '호로스까이', '호로스키', '후라들', '후래자식', '후레', '후뢰', '씨ㅋ발', 'ㅆ1발', '씌발', '띠발', '띄발', '뛰발', '띠ㅋ발', '뉘뮈']

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
    global badWords
    for i in badWords:
        if i in message.content:
            await message.delete()
            await message.author.send('!경고:욕설/상대를 비난하는 글을 적을시 메시지가 삭제됩니다.')
            변수명 = client.get_channel(702413785838649444)
            embed = discord.Embed(title="욕설감지", description="욕설 을(를) 감지했습니다.", color=0x62c1cc)
            embed.add_field(name="사용자", value=message.author.mention, inline=True)
            embed.add_field(name="확인된 채널", value=message.channel, inline=True)
            embed.add_field(name="확인된 채팅", value=message.content, inline=False)
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
        await message.channel.send("투표가 제거되었습니다.")
        os.remove("vote_data.json")
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

#access_token=os.environ["BOT_TOKEN"]
client.run("NzAwOTUyNzAxMzg2NzUyMDYw."+"Xp8OLQ.xkW-ATsqNyHvu9BbsEqk88D9Tbg")#access_token)
