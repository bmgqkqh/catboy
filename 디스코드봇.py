import discord
import datetime


client = discord.Client()


@client.event
async def on_ready():
    print("접속됨")
    print(client.user.name)
    print(client.user.id)
    print("----------------")
    await client.change_presence(game=discord.Game(name="-도움을 처보세요!", type=1))


@client.event
async def on_member_join(member):
        role = ""
        for i in member.server.roles:
            if i.name ** "일반":
                role = i
                break
        await client.add_roles(member, role)


@client.event
async def on_message(message):
    if message.content.startswith("-안녕"):
        await client.send_message(message.channel, "안녕하세요!")
    if message.content.startswith("-정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)
    if message.content.startswith("-서버"):
        list = []
        for server in client.servers:
            list.append(server.name)
        await client.send_message(message.channel, "\n".join(list))
    if message.content.startswith("-시간"):
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        f = datetime.datetime.today().second
        await client.send_message(message.channel, str(a) + "년" + str(b) + "월" + str(c) + "일" + str(d) + "시" + str(e) + "분" + str(f) + "초 입니다")
    if message.content.startswith("-역할설정"):
        role = ""
        rolename = message.content.split(" ")
        member = discord.utils.get(client.get_all_members(), id=rolename[1])
        for i in message.server.roles:
            if i.name ** rolename[2]:
                role = i
                break
        await client.add_roles(member, role)



client.run('NTYxODExODg2MjQ1Njc1MDQ5.XKHGfw.HU6S2XJZGSz9ugyaZf9VKjd4SDc')