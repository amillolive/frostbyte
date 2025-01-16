import lightbulb
import hikari
from frostbyte import BOT

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
            color = None
        )
        embed.set_footer(f"Latency: {round(bot.heartbeat_latency * 1000)}ms")
        await event.context.respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)