import os
from dotenv import load_dotenv
import interactions

load_dotenv()

bot = interactions.Client(
    token = os.getenv("TOKEN"),
    default_scope = int(os.getenv("SCOPE")),
)

@bot.command()
async def say(ctx: interactions.CommandContext):
    pass

@say.subcommand()
@interactions.option(description="Gimme number")
async def number(ctx: interactions.CommandContext, number: int = None):
    await ctx.send(f"You say {number}")

@say.subcommand()
@interactions.option(description="Gimme text")
async def text(ctx: interactions.CommandContext, second_option: str):
    await ctx.send(f"You say {second_option}")

bot.start()
