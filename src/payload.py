


TOKEN = 'placeyourtokenhere'





##################################################################




import discord
from discord.ext import commands
import subprocess

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f"Bot is online! You're logged in as {bot.user.name} (ID: {bot.user.id})")
    print('------')

@bot.command()
async def cmd(ctx, *, command: str):
    await ctx.send(f"Running command: `{command}`... Hang tight!")

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, executable='/bin/bash')

        if result.stdout:
            await ctx.send(f"**Output:**\n```\n{result.stdout}\n```")
        
        if result.stderr:
            await ctx.send(f"**Error:**\n```\n{result.stderr}\n```")
    except Exception as e:
        await ctx.send(f"Ouch! Something went wrong: {e}")

bot.run(TOKEN)
