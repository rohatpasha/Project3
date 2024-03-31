import discord
import proje2
import time

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        time.sleep(1)
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$euro'):
        print("düşünülüyor...")
        time.sleep(2)
        await message.channel.send("34,91!")
        print("düşünülüyor...")
        time.sleep(2)
    elif message.content.startswith('$dolar'):
        print("düşünülüyor...")
        time.sleep(2)
        await message.channel.send("32,37!")
    elif message.content.startswith('$sifre'):
        print("düşünülüyor...")
        time.sleep(2)
        await message.channel.send(proje2.x(8))
    elif message.content.startswith('$ownere'):
        print("düşünülüyor...")
        time.sleep(2)
        await message.channel.send("**Musab&Rohat**")

client.run("BURAYA KENDİ TOKENİNİZİ YAPIŞTIRIN")
