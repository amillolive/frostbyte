import hikari
import lightbulb
import typing as t
from lightbulb import plugins
import collections
from lightbulb.utils import nav
import sqlite3

base_connection = sqlite3.connect("server_base.db")
base_cursor = base_connection.cursor()

initial_command = """CREATE TABLE IF NOT EXISTS
guilds(guild_id INTEGER PRIMARY KEY, log_id INTEGER)"""
setup_check = None

with open("./secrets/token") as f:
    _token = f.read().strip()

color_default = "#4A90E2"
color_warning = "#FF9800"
color_error =  "#D32F2F"
color_success = "#4CAF50"

def color(color=None):
    if f"{color}" == "success":
        color = color_success
    
    elif f"{color}" == "error":
        color = color_error
    
    elif f"{color}" == "warning":
        color = color_warning
    
    else:
        color = color_default
    return color

COLOR = color

class FrostByteHelp(lightbulb.DefaultHelpCommand):
    async def send_bot_help(self, context):
        pages = []
        categroized = []

        p_commands = await self._get_command_plugin_map(self.app._prefix_commands, context)
        s_commands = await self._get_command_plugin_map(self.app._slash_commands, context)
        m_commands = await self._get_command_plugin_map(self.app._message_commands, context)
        u_commands = await self._get_command_plugin_map(self.app._user_commands, context)

        plugin_pages: t.MutableMapping[t.Optional[plugins.Plugin], t.List[str]] = collections.defaultdict(list)
        self._add_cmds_to_plugin_pages(plugin_pages, p_commands, "Prefix")
        self._add_cmds_to_plugin_pages(plugin_pages, s_commands, "Slash")
        self._add_cmds_to_plugin_pages(plugin_pages, m_commands, "Message")
        self._add_cmds_to_plugin_pages(plugin_pages, u_commands, "User")

        for plugin, page in plugin_pages.items():
            if plugin is not None:
                categroized.append(plugin.name)
                description = f"{plugin.description}"
            if plugin is None:
                description = "Description not provided..."

            embed = hikari.Embed(
                title = "FrostByte Helper",
                description = "A collection of all commands I allow you to use.",
                color = None
            )
            embed.add_field(
                name = f"{plugin.name if plugin is not None else 'Uncategorized'}",
                value = description
            )
            embed.set_footer(f"Latency: {round(self.bot.heartbeat_latency * 1000)}ms")
            pages.append(embed)
        
        navigator = nav.ButtonNavigator(pages)
        await navigator.run(context)

GUILD_ID = 1139789847838609460
BOT = lightbulb.BotApp(
    token = _token,
    prefix = ">",
    intents = hikari.Intents.ALL,
    default_enabled_guilds = GUILD_ID,
    help_class = FrostByteHelp,
    help_slash_command = True
)