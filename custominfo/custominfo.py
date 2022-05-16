import discord
from dislash.application_commands._modifications.old import (
    send_with_components,
)
from dislash.interactions import ActionRow, Button, ButtonStyle
from redbot.core import commands, Config


class CustomInfo(commands.Cog):
    """
    Cog to setup a custom information command.
    """

    __author__ = ["JeffJrShim"]
    __version__ = "1.0.0"

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"

    def __init__(self, bot):
        self.bot = bot
        if not hasattr(commands.Context, "sendi"):
            commands.Context.sendi = send_with_components
        self.config = Config.get_conf(self, identifier=835238)
        default_config = {"thumbnail": None, "description": None, "button_url1"="", "button_url2"="", "button_url3"="", "button_url4"=""}
        self.config.register_global(**default_config)
    

    def cog_unload(self):
        global info_com
        if info_com:
            try:
                self.bot.remove_command("info")
            except Exception as e:
                log.info(e)
        self.bot.add_command(info_com)