import discord
from dislash.application_commands._modifications.old import send_with_components
from dislash.interactions import ActionRow,Button,ButtonStyle
from redbot.core import commands
class CustomInfo(commands.Cog):
	'\n    Cog to setup a custom information command.\n    ';__author__=['JeffJrShim'];__version__='0.0.1'
	def format_help_for_context(A,ctx):'Thanks Sinbad!';B=super().format_help_for_context(ctx);return f"{B}\n\nAuthors: {', '.join(A.__author__)}\nCog Version: {A.__version__}"
	def __init__(A,bot):
		A.bot=bot
		if not hasattr(commands.Context,'sendi'):commands.Context.sendi=send_with_components
	def cog_unload(A):
		global info_com
		if info_com:
			try:A.bot.remove_command('info')
			except Exception as B:log.info(B)
		A.bot.add_command(info_com)
	@commands.command()
	async def info(self,ctx):A=discord.Embed(description="<:umiko_love:976859459890577428>**__ABOUT UMIKO__**\nUmiko is a highly advance utility bot and is a fork of red.\nThe default prefix for the bot is `u!` and `@Umiko`.\nRun `@Umiko help` to see all the commands.\nRun `@umiko invite` to invite the bot to your server\nIf you have any issues with the bot feel free to contact `! JuliaNGaminG#3569`\nthrough his DM's or join the support server [`Support server`](https://discord.gg/A5Ww6HqXmz) or use `@umiko contact <Your_message>`\n\n<a:pink_dot:971950913923219476>**Instance Owned by:**> <a:umiko_crown:976892445579149402>`! JuliaNGaminG#3569 728797399836917771` \n\n<a:pink_dot:971950913923219476>**Bot's System** \n```\nOS - Windows 11\nProcessor - Intel(R) Core(TM) i5-1035G1 CPU @ 1.00GHz   1.19 GHz\nRAM - 8.00 GB\nSystem type - 64-bit operating system, x64-based processor\nPython version - 3.9.9\n```\n\n<a:pink_dot:971950913923219476>**Versions**\n> <:umiko_python:977488373834973234>[`3.9.9`](https://www.python.org/) • <:umiko_dpy:977488373834973234>[`1.7.3`](https://github.com/Rapptz/discord.py)\n> <a:umiko_sip:977488373834973234>[`Invite me`](https://discord.com/api/oauth2/authorize?client_id=962323485772881950&permissions=8&scope=bot) • <a:umiko_dance:977488373834973234>[`Support server`](https://discord.gg/A5Ww6HqXmz)");A.set_thumbnail(url='https://cdn.discordapp.com/attachments/975677956254990376/977188995974975529/umiko_resized.jpg');await ctx.send(embed=A)