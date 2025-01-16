import lightbulb
import hikari
from frostbyte import BOT, color

plugin = lightbulb.Plugin("Moderation")
bot=BOT

@plugin.command
@lightbulb.command("kick", "Kick a member from the server.")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def kick(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(
        title = "All clear!",
        description = "User has been kicked.",
        color=color("success")
    )
    await ctx.respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)