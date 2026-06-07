"""
Helper functions for the Discord bot
"""

import discord
from typing import Optional

def create_embed(title: str, description: str, color: discord.Color = discord.Color.blue()) -> discord.Embed:
    """
    Create a simple embed with title and description
    
    Args:
        title: The embed title
        description: The embed description
        color: The embed color (default: blue)
    
    Returns:
        discord.Embed: The created embed
    """
    embed = discord.Embed(
        title=title,
        description=description,
        color=color
    )
    return embed

def create_error_embed(error_message: str) -> discord.Embed:
    """
    Create an error embed
    
    Args:
        error_message: The error message to display
    
    Returns:
        discord.Embed: Error embed with red color
    """
    return create_embed("Error", error_message, discord.Color.red())

def create_success_embed(message: str) -> discord.Embed:
    """
    Create a success embed
    
    Args:
        message: The success message to display
    
    Returns:
        discord.Embed: Success embed with green color
    """
    return create_embed("Success", message, discord.Color.green())


def random_number(min_value: int, max_value: int) -> int:
    """
    Generate a random number between min_value and max_value
    
    Args:
        min_value: The minimum value (inclusive)
        max_value: The maximum value (inclusive)
    
    Returns:
        int: A random number between min_value and max_value
    """
    import random
    return random.randint(min_value, max_value)