import discord


async def process_output(p, m, msg, ctx):
    for line in iter(p.stdout.readline, b''):
        msg += line.rstrip().decode("utf-8") + "\n"
        try:
            await m.edit(content=msg)
        except discord.errors.HTTPException:
            msg = msg.splitlines()[-1]
            m = await ctx.send(msg)
    return msg, m