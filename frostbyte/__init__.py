import hikari
import lightbulb
import typing as t
from lightbulb import plugins
import collections
from lightbulb.utils import nav
import sqlite3
from os import walk

'''
base_connection = sqlite3.connect("server_base.db")
base_cursor = base_connection.cursor()
initial_command = """CREATE TABLE IF NOT EXISTS
guilds(guild_id INTEGER PRIMARY KEY, log_id INTEGER)"""
setup_check = None
'''

with open("./secrets/token") as f:
    _token = f.read().strip()

error_emoji = "https://cdn3.emoji.gg/emojis/4934-error.png"
success_emoji = "https://cdn3.emoji.gg/emojis/4569-ok.png"
warning_emoji = "https://cdn3.emoji.gg/emojis/8649-warning.png"
default_emoji = "https://cdn3.emoji.gg/emojis/9396-info.png"

color_default = "#4A90E2"
color_warning = "#FF9800"
color_error =  "#D32F2F"
color_success = "#4CAF50"

def color(color=None, type=None):
    if type == None or str(type).lower() == "color":
        if str(color).lower() == "success":
            color = color_success
        elif f"{color}" == "error":
            color = color_error
        elif f"{color}" == "warning":
            color = color_warning
        else:
            color = color_default
        return color
    else:
        if str(color).lower() == "success":
            color = success_emoji
        elif f"{color}" == "error":
            color = error_emoji
        elif f"{color}" == "warning":
            color = warning_emoji
        else:
            color = default_emoji
        return color

COLOR = color

extensions = []
for (dirpath, dirnames, filenames) in walk("./frostbyte/extensions"):
    for filename in filenames:
        extensions.append(filename[:-3])
    break
e = extensions

class FrostByteHelp(lightbulb.DefaultHelpCommand):
    async def send_bot_help(self, context):
        embed = hikari.Embed(
            title = "Help Command",
            description = "**Prefix**: **`>help [command]`**\n*A collection of all commands I allow you to use.*",
            color = color("default")
        )
        embed.set_footer(f"The map you should have used earlier.", icon = color("default", "emoji"))
        for plugin in e:
            embed.add_field(name = plugin, value = "**`>na`**\n**`>dev`**\n**`>members`**", inline = True)
        await context.respond(embed = embed)

GUILD_ID = 1139789847838609460
BOT = lightbulb.BotApp(
    token = _token,
    prefix = ">",
    intents = hikari.Intents.ALL,
    default_enabled_guilds = GUILD_ID,
    help_class = FrostByteHelp,
    help_slash_command = True
)

ball_response = [
    "Definitely, the ice is in your favor!",
    "No way, the iceberg is blocking that path!",
    "I can’t tell, the snowstorm’s making it hard to see.",
    "Maybe in the future, when the Arctic warms up a bit.",
    "Absolutely, your future is as clear as the ice!",
    "Not likely, even the polar bears wouldn’t bet on that one.",
    "Ask again later, the winds are too wild right now.",
    "Chances are good, the snow is shifting in your favor.",
    "Nope, that’s a cold no-go from me!",
    "I see a glimmer of hope, but not quite yet.",
    "It’s all ice and no fire—sorry, it’s a no.",
    "For sure, you’ve got the strength of the tundra behind you.",
    "I can’t predict it, the ice is cracking under pressure!",
    "Definitely not, that’s an icy roadblock.",
    "It’s a maybe, the winds are shifting your way.",
    "You’re on the right track, but the ice needs time to settle.",
    "The future’s frozen solid, but I think it's a yes!",
    "Unclear for now, the snow’s too thick to tell.",
    "No chance, even the seals are laughing at that one!",
    "It’s a definite maybe, check back in the spring!",
    "Absolutely not, the polar bears are shaking their heads.",
    "It’s in the cards, but you’ll have to wait for the thaw.",
    "Yes, that’s a cold, hard yes from me!",
    "No way, not in this icy landscape.",
    "The answer’s frozen, but give it time to thaw!",
    "It’s a maybe, but it’s way too cold to make a decision now.",
    "Definitely not, even the ice would crack under that weight.",
    "Sure thing, the North Pole’s got your back!",
    "Can’t tell, the blizzards are clouding my view.",
    "Not happening, even the polar bears wouldn’t try that one!"
]