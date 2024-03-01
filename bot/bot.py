import os
from dotenv import load_dotenv
from interactions

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

button1 = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="hello world!",
    custom_id="hello",
)

button2 = interactions.Button(
    style=interactions.ButtonStyle.DANGER,
    label="bye bye!",
    custom_id="bye!",
)

row = interactions.spread_to_rows(button1, button2)

@bot.command()
async def test(ctx):
    await ctx.send("rows!", components=row)

@bot.component("hello")
async def button_response(ctx):
    await ctx.send("You clicked the hello Button :O", ephemeral=True)

@bot.component("bye!")
async def button_response(ctx):
    await ctx.send("You clicked the bye Button :O", ephemeral=True)

@bot.command()
async def my_cool_modal_command(ctx):
    modal = interactions.Modal(
        title="Application Form",
        custom_id="mod_app_form",
        components=[interactions.TextInput(
                        style=interactions.TextStyleType.SHORT,
                        label="Let's get straight to it: what's 1 + 1?",
                        custom_id="text_input_response",
                        min_length=1,
                        max_length=3,)],
    )

    await ctx.popup(modal)
@bot.modal("mod_app_form")
async def modal_response(ctx, response: str):
    await ctx.send(f"You wrote: {response}", ephemeral=True)

bot.start()
