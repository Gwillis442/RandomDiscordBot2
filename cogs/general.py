import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import logging
import os
from utils.ai_helpers import AIHelper

logger = logging.getLogger(__name__)

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info('General cog loaded')

    # Slash command example
    @app_commands.command(name="ping", description="Check bot latency")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Pong! Latency: {round(self.bot.latency * 1000)}ms')

    # Slash command with parameter
    @app_commands.command(name="hello", description="Say hello to someone")
    @app_commands.describe(name="The name of the person to greet")
    async def hello(self, interaction: discord.Interaction, name: str):
        await interaction.response.send_message(f'Hello, {name}!')

    # Regular prefix command
    @commands.command(name='info')
    async def info(self, ctx):
        """Get bot information"""
        embed = discord.Embed(
            title="Bot Information",
            description="A simple Discord bot",
            color=discord.Color.blue()
        )
        embed.add_field(name="Servers", value=len(self.bot.guilds), inline=True)
        embed.add_field(name="Users", value=len(self.bot.users), inline=True)
        await ctx.send(embed=embed)

    # AI command using OpenAI API
    @app_commands.command(name="ask_ai", description="Ask the AI a question")
    @app_commands.describe(question="Your question for the AI")
    async def ask_ai(self, interaction: discord.Interaction, question: str):
        await interaction.response.defer()
        api_key = os.getenv('OPENAI_API_KEY') or os.getenv('gptApiKey')

        if not api_key:
            await interaction.followup.send(
                'AI is not configured. Add OPENAI_API_KEY or gptApiKey to your .env file and restart the bot.',
                ephemeral=True,
            )
            return

        try:
            ai_helper = AIHelper(api_key=api_key)
            response = await asyncio.to_thread(ai_helper.generate_response, question)
        except Exception:
            logger.exception('ask_ai failed')
            await interaction.followup.send(
                'AI request failed. Check the bot logs for the backend error and verify the OpenAI API key.',
                ephemeral=True,
            )
            return

        await interaction.followup.send(response)

async def setup(bot):
    await bot.add_cog(General(bot))
