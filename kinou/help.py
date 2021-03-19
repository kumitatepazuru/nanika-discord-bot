import csv

import discord

data = csv.reader(open("./data/help-kinou.csv"))
data2 = csv.reader(open("./data/help-hannou.csv"))
l1 = [row for row in data2]
l2 = [row for row in data2]


async def help(message):
    embed = discord.Embed()
    embed.add_field(name="こんにちは！ @discordを快適ライフに です！", value="このbotは多機能botと呼ばれ、いろんなことができます。\nほしい機能等は #普通のチャット で。",inline=False)
    embed.add_field(name="コマンド機能",value="そのままんまです。ミニゲームとかできます。",inline=False)
    for i in l1:
        embed.add_field(name=i[0],value=i[1],inline=True)
    embed.add_field(name="特定の単語に反応する機能", value="そのままんまです。下ネタとか好きなのでよく反応します。", inline=False)
    for i in l2:
        embed.add_field(name=i[0], value=i[1], inline=True)
    embed.add_field(name="作成者", value="Create by Riku Ueda\nhttps://github.com/kumitatepazuru/", inline=False)
    embed.add_field(name="ソースコード", value="https://github.com/kumitatepazuru/nanika-discord-bot/", inline=False)
    await message.channel.send(embed=embed)

