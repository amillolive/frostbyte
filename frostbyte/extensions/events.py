import lightbulb
import hikari
from frostbyte import BOT, color

plugin = lightbulb.Plugin("Events")
bot=BOT

@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        raise event.exception
    
    exception = event.exception.__cause__ or event.exception

    if isinstance(exception, lightbulb.CommandNotFound):
        embed = hikari.Embed(
            title = "Hmm..",
            description = "My paws can’t track that one! Maybe **`>help`** will point you in the right direction!",
            color = color("error")
        )
        embed.set_footer(text = f"The help command is your map.", icon = color("error", "emoji"))
        await event.context.respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)