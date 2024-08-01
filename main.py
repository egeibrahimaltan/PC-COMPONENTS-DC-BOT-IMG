import discord
from discord.ext import commands
from model import model_keras
import os

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
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def kontrol(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            fileName = attachment.filename
            fileUrl = attachment.url
            local_file_path = os.path.join(os.getcwd(), fileName)
            
            await attachment.save(local_file_path)
            await ctx.send(f"Gönderdiğiniz fotoğraf kayit Edildi. Fotoğrafın Adı: {fileName}, Fotoğrafın dosya yolu: {fileUrl}")

            model_path = "c:\\Users\\Ege\\Desktop\\DİSCORD BOT WİTH Aİ\\bot m7l2\\keras_model.h5"
            label_path = "c:\\Users\\Ege\\Desktop\\DİSCORD BOT WİTH Aİ\\bot m7l2\\labels.txt"
            
            try:
                result = model_keras(modelYolu=model_path, labelYolu=label_path, gorselYolu=local_file_path)
                await ctx.send(result)
            except FileNotFoundError as e:
                await ctx.send(f"File not found: {e}")
            except Exception as e:
                await ctx.send(f"An error occurred: {e}")
    else:
        await ctx.send("Fotoğraf yüklemeyi unuttun!")

bot.run("TOKEN")
