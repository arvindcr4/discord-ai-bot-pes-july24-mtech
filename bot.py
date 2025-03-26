import os
import discord
from discord.ext import commands
import aiohttp
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

async def get_ai_response(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://localhost:3000",
        "X-Title": "Discord Bot"
    }
    
    payload = {
        "model": "google/gemini-pro",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(OPENROUTER_URL, json=payload, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data['choices'][0]['message']['content']
            else:
                return f"Error: {response.status}"

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print('Using Gemini Pro model for responses')

@bot.command(name='ask')
async def ask(ctx, *, question):
    """Ask the AI a question"""
    async with ctx.typing():
        response = await get_ai_response(question)
        await ctx.send(response)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('Please provide a question. Usage: !ask <your question>')
    else:
        await ctx.send(f'An error occurred: {str(error)}')

# Run the bot
bot.run(os.getenv('DISCORD_BOT_TOKEN')) 