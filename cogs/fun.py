import discord
from discord.ext import commands
from discord import app_commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Fun cog loaded')

    @app_commands.command(name="roll", description="Roll a dice")
    @app_commands.describe(sides="Number of sides on the dice (default: 6)")
    async def roll(self, interaction: discord.Interaction, sides: int = 6):
        if sides < 1:
            await interaction.response.send_message("Please provide a valid number of sides!")
            return
        result = random.randint(1, sides)
        await interaction.response.send_message(f'🎲 You rolled a {result}!')

    @app_commands.command(name="flip", description="Flip a coin")
    async def flip(self, interaction: discord.Interaction):
        result = random.choice(['Heads', 'Tails'])
        await interaction.response.send_message(f'🪙 {result}!')

    @app_commands.command(name="8ball", description="Ask the magic 8-ball a question")
    @app_commands.describe(question="Your question for the 8-ball")
    async def eightball(self, interaction: discord.Interaction, question: str):
        responses = [
            "It is certain.", "It is decidedly so.", "Without a doubt.",
            "Yes definitely.", "You may rely on it.", "As I see it, yes.",
            "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
            "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
            "Cannot predict now.", "Concentrate and ask again.",
            "Don't count on it.", "My reply is no.", "My sources say no.",
            "Outlook not so good.", "Very doubtful."
        ]
        await interaction.response.send_message(f'🎱 {random.choice(responses)}')

async def setup(bot):
    await bot.add_cog(Fun(bot))
