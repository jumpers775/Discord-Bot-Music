import discord
import os

# Commands
from discord.ext import commands

# TOKEN
from dotenv import load_dotenv

# TOKEN
load_dotenv()
TOKEN = os.getenv('TOKEN')
print(TOKEN)

client = commands.Bot(command_prefix="/")


# Connect voice Channel
@client.command()
async def connect(ctx,url_: str):
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="General")
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  # if not voice.is_connected():
  await voiceChannel.connect()
  print("Connect voice channel")

# Disconnect voice Channel
@client.command()
async def disconnect(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  # if voice.is_connected():
  await voice.disconnect()
  print("Disconnect voice channel")
  # else:
  #   await ctx.send("the bot is not connect")

#Pause
@client.command()
async def pause(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice.is_playing():
    voice.pause()
    print("voice pause")
  else:
    print("voice no pause")
    # await ctx.send("voice no pause")

#Resume
@client.command()
async def resume(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice.is_paused():
    voice.resume()
    print("voice resume")
  else:
    print("voice no resume")
    # await ctx.send("voice no resume")

#Stop
async def stop(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  voice.stop()
 
  
client.run(TOKEN)