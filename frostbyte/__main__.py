import os
import hikari
import hikari.presences
import lightbulb
from frostbyte import GUILD_ID, BOT, COLOR

with open("./secrets/token") as f:
    _token = f.read().strip()

bot=BOT
bot.load_extensions_from("./frostbyte/extensions", must_exist = True)

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop
        uvloop.install()

    bot.run(
        activity = hikari.presences.Activity(
            name = "the igloo | >help",
            state = "FrostByte", 
            type = hikari.ActivityType.STREAMING
        )
    )