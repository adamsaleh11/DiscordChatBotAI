import discord
import time
import asyncio
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://adamsaleh:Galino356@cluster0.ouv1mzq.mongodb.net/?retryWrites=true&w=majority") ##connects to MongoDB Atlas
db = cluster["theta"] #specifies which database we are working with
collection = db["message Logs"]


messages = joined = 0
client = discord.Client()

@client.event
async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")
            messages = 0
            joined = 0
            await asyncio.sleep(5)

        except Exception as e:
            print(e)
            await asyncio.sleep(5)

@client.event
async def on_member_update(before, after):
    nickname = after.nickname
    if nickname:
        if nickname.lower().count == "adam" > 0:
            last = before.nickname
            if last:
                await after.edit(nick=last)

            else:
                await after.edit(nick="Stinky Brownie")

@client.event
async def on_member_join(member):
    global joined
    joined+=1
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the server {member.mention}""")

@client.event
async def on_message(message):
    global messages
    messages += 1
    id = client.get_guild(761800211995426816)
    valid_users = ["WetLekWatta#2007", "soccer101#6988", "Black Magic#2215", "calminnit#6179",
                   "GreenCatapult__#3519", "Brshil#8757", "kahsaifs#5546", "renno#1061", "SK#8868", "VarshanJ#8509" ]
    bad_words = ["Fuck", "Fuck you", "Shit", "Piss off", "Dick head", "Bitch", "Bollocks", "Wanker", "Shut up"]

    if message.channel.name == "general":
        for word in bad_words:
            if message.content.count(word)> 0:
                await message.channel.send("A bad word was detected. Plz dont swear again or ur admitting to liking men.")

    if message.channel.name == "general":
        if message.content == "Members" or message.content == "members" or message.content == "Member count":
            embed = discord.Embed(title="Members of FS", description="Some bitchass fags ngl")
            embed.add_field(name="Aaryan", value="Team Leader")
            embed.add_field(name="Karan", value="Other")
            embed.add_field(name="VJ", value="Other")
            embed.add_field(name="Suyog", value="Other")
            embed.add_field(name="Shubo", value="Other")
            embed.add_field(name="Vini", value="Other")
            embed.add_field(name="Shil", value="Other")
            embed.add_field(name="Krish", value="Other")
            embed.add_field(name="Kahsai", value="Other")
            embed.add_field(name="Adam", value="Other")
            await message.channel.send(embed=embed)


    ##allows bot to only be deployed within the "bot" channel
    if message.channel.name == "general" and str(message.author) in valid_users:
        if message.content.startswith("Whats that smell bro..."):
            await asyncio.sleep(2)
            await message.channel.send("Karan shat on the floor again fammmmm")

        elif message.content.startswith("theta") or message.content.startswith("Theta") :
            await asyncio.sleep(2)
            await message.channel.send("Dont bother me, Man City stomped on them Gunna bois")


        elif message.content.startswith("hey") or message.content.startswith("hi") or message.content.startswith("hello"):
            await asyncio.sleep(2)
            await message.channel.send("heyyy")

        elif message.content.startswith("What time is it") or message.content.startswith("What time is it?"):
            await asyncio.sleep(2)
            await message.channel.send("Its time to level up croski")

        elif message.content.startswith("Thanks"):
            await asyncio.sleep(2)
            await message.channel.send("np")

        elif message.content.startswith("Member count"):
            await asyncio.sleep(2)
            await message.channel.send(f"""# of Members is: {id.member_count}""")

        elif message.content.startswith("Whats the time"):
            await asyncio.sleep(2)
            await message.channel.send(f"""The time is: {int(time.time())}""")

        elif message.content.startswith("Whats up"):
            await asyncio.sleep(2)
            await message.channel.send("Automating a few tasks...yourself?")

        elif message.content.startswith("How was your day?"):
            await asyncio.sleep(2)
            await message.channel.send("Automating a few tasks...yourself?")

        elif message.content.startswith("lol") or message.content.startswith("Lol"):
            await  asyncio.sleep(2)
            await  message.channel.send("Lol")

        elif message.content.startswith("theta"):
            await  asyncio.sleep(2)
            await  message.channel.send("hi")

        else:
            print(f"""User: {message.author} \nContent: {message.content} \nChannel: {message.channel}""")
            post = {"User": str(message.author), "Content": str(message.content), "Channel": str(message.channel)}
            collection.insert_one(post)


client.loop.create_task(update_stats())
client.run("MTA0NjIyOTgwOTA0ODU4ODM0MA.GpFW1K.qEeCo1kR4sTTWTqIkalK2H_qfCoGe5dsppS644")
