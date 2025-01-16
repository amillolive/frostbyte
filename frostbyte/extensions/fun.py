import lightbulb
import hikari
from frostbyte import BOT, color, ball_response
import random

plugin = lightbulb.Plugin("Moderation")
bot=BOT

@plugin.command
@lightbulb.option("question", "The question to ask the magical snow wizard.", type = str)
@lightbulb.command("8ball", "Ask the magical snow wizard a question.", pass_options = True)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def _8ball(ctx: lightbulb.Context, question: str) -> None:
    response = random.choice(ball_response)
    embed = hikari.Embed(
        title = "The Wizard has spoken...",
        description = "**`Better than the 8ball`**",
        color = color()
    )
    embed.add_field(name = "Question", value = question)
    embed.add_field(name = "Answer", value = response)
    embed.set_footer(text = "Wizardous greetings..", icon = color("default", "emoji"))
    await ctx.respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)