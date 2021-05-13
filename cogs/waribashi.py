import copy
import resource
import time

import discord
import sys
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))
print(resource.getrlimit(resource.RLIMIT_STACK))

sys.setrecursionlimit(500000)


class waribashi:
    LEFT_ARROW: str = "\N{LEFTWARDS BLACK ARROW}\N{VARIATION SELECTOR-16}"
    RIGHT_ARROW: str = "\N{BLACK RIGHTWARDS ARROW}\N{VARIATION SELECTOR-16}"
    EMOJIS = [LEFT_ARROW, RIGHT_ARROW]

    def __init__(self):
        self.embed = discord.Embed()
        self.YOU = [1, 1]
        self.I = [1, 1]
        self.OUT = []

    async def msg_reaction_chk(self, client, msg, message, i2):
        def check(reaction: discord.Reaction, user: discord.User) -> bool:
            # リアクション先のメッセージや追加された絵文字が適切かどうか判断する。
            return str(reaction.emoji) in self.EMOJIS and reaction.message == msg and user == message.author

        self.embed.set_field_at(index=2, name="読み込み中...", value="ちょっとまってね", inline=False)
        await msg.edit(embed=self.embed)
        await msg.add_reaction(self.LEFT_ARROW)
        await msg.add_reaction(self.RIGHT_ARROW)
        self.embed.set_field_at(index=2, name="操作", value=i2, inline=False)
        await msg.edit(embed=self.embed)
        reaction, _ = await client.wait_for("reaction_add", check=check)
        if reaction.emoji == self.LEFT_ARROW:
            s = 0
        else:
            s = 1
        await msg.clear_reactions()
        return s

    async def waribashi_start(self, client: discord.Client, message):
        self.__init__()
        self.embed.set_author(name="わりばし")
        self.embed.add_field(name="読み込み中...", value="ちょっとまってね")
        msg: discord.Message = await message.channel.send(embed=self.embed)
        await msg.add_reaction(self.LEFT_ARROW)
        await msg.add_reaction(self.RIGHT_ARROW)
        self.embed.clear_fields()
        self.embed.add_field(name="", value="")
        self.embed.add_field(name="", value="")
        self.embed.add_field(name="", value="")

        while True:
            I_ = copy.deepcopy(self.I)
            YOU_ = copy.deepcopy(self.YOU)
            if self.I[0] >= 5:
                I_[0] = "\N{CROSS MARK}"
            if self.I[1] >= 5:
                I_[1] = "\N{CROSS MARK}"
            if self.YOU[0] >= 5:
                YOU_[0] = "\N{CROSS MARK}"
            if self.YOU[1] >= 5:
                YOU_[1] = "\N{CROSS MARK}"
            self.embed.set_field_at(index=0, name="BOT",
                                    value=self.LEFT_ARROW + str(I_[0]) + "  " + self.RIGHT_ARROW + str(I_[1]),
                                    inline=True)
            self.embed.set_field_at(index=1, name="あなた",
                                    value=self.LEFT_ARROW + str(YOU_[0]) + "  " + self.RIGHT_ARROW + str(
                                        YOU_[1]), inline=True)
            s1 = await self.msg_reaction_chk(client, msg, message, "自分の指を選択してください")
            s2 = await self.msg_reaction_chk(client, msg, message, "相手の指を選択してください")
            self.embed.set_field_at(index=2, name="BOTのターン", value="AIを駆使して本気に勝ちに行きます。ちょっとまってね。", inline=False)
            await msg.edit(embed=self.embed)
            self.I[s2] += self.YOU[s1]
            t = time.time()
            f_ = f()
            f_.find(copy.deepcopy(self.I), copy.deepcopy(self.YOU))
            f_.total()


class f:
    w = 0
    l = 0
    t = 0

    def find(self, I, YOU, c=0):
        self.t += 1
        if (I[0] < 5 or I[1] < 5) and (YOU[0] < 5 or YOU[1] < 5):
            ok = []
            for i in range(2):
                for j in range(2):
                    tmpI = copy.deepcopy(I)
                    tmpYOU = copy.deepcopy(YOU)
                    tmpYOU[i] += tmpI[j]
                    if tmpYOU[i] < 5 and tmpI[j] < 5:
                        ok.append([i,j])
                    else:
                        self.t += 1
                        self.w += 1

            for i in range(2):
                for j in range(2):
                    for k in ok:
                        tmpI = copy.deepcopy(I)
                        tmpYOU = copy.deepcopy(YOU)
                        tmpYOU[k[0]] += tmpI[k[1]]
                        tmpI[i] += tmpYOU[j]
                        if tmpI[i] < 5:
                            self.find(tmpI, tmpYOU, c + 1)
                        else:
                            self.t += 1
                            self.l += 1
        elif I[0] < 5 or I[1] < 5:
            self.w += 1
        elif YOU[0] < 5 or YOU[1] < 5:
            self.l += 1

    def total(self):
        print(self.t,self.w,self.l)
