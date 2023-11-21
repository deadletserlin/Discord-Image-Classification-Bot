import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def hello(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f'Menyimpan gambar ke ./{attachment.filename}')
            hasil = get_class('keras_model.h5', 'labels.txt', f',/{attachment.filename}')
            # inferensi
            if hasil[0] == 'kunyit\n' and hasil[1] >= 0.65:
                await ctx.send(f'Gambar yang kamu kirim adalah {hasil[0]}')
                await ctx.send('khasiat dari kunyit adalah...')
                await ctx.send('harga kunyit ini sekitaran RP.15k-RP.30k perkilo')
            elif hasil[0] == 'kencur\n' and hasil[1] >= 0.65:
                await ctx.send(f'Gambar yang kamu kirim adalah {hasil[0]}')
                await ctx.send('khasiat dari kencur adalah...')
                await ctx.send('harga kencur ini sekitaran RP.15k-RP.30k perkilo')
            elif hasil[0] == 'jahe\n' and hasil[1] >= 0.65:
                await ctx.send(f'Gambar yang kamu kirim adalah {hasil[0]}')
                await ctx.send('khasiat dari jahe adalah...')
                await ctx.send('harga jahe ini sekitaran RP.15k-RP.30k perkilo')
            else:
                await ctx.send('GAMBAR MU KEMUNGKINAN: salah format/blur/corrupt')
                await ctx.send('KIRIM GAMBAR BARU!!!')
    else:
        await ctx.send('KAMU TIDAK MENGIRIM GAMBAR APAPUN :D')

bot.run("MTExMDU1Nzk4MDM4NDA0NzE5NA.GZux-u.DDpFbYN-3NbcfqOg7e6-HCgyYuSzns3gMgpRnc")