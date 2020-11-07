import platform
import shutil
import sys
import time
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from datetime import datetime
from os import remove
from platform import python_version, uname
from shutil import which

import psutil
from telethon import __version__, version

from userbot import ALIVE_LOGO, ALIVE_NAME, CMD_HELP, USERBOT_VERSION, StartTime, bot
from userbot.events import register
	

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"	
modules = CMD_HELP

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):	
uptime = await get_readable_time((time.time() - StartTime))
    output = (
        "`Bot is running smoothly 😎🏓...`\n"
        "`▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱`\n"
        f"»✳️>⚙️ `Telethon     : v{version.__version__} `\n"
        f"»✳️>🐍 `Python       : v{python_version()} `\n"
        f"»✳️>👤 `User`        : {DEFAULTUSER}\n"
        "`▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱`\n"
        f"»✳️>💻 `Running on   :`[Hidden Repo](t.me/danish_00)\n"
        f"»✳️>🗃 `New Plugins  : {len(modules)} `\n"
        f"»✳️>🤖 `DanishBot    : v{USERBOT_VERSION} `\n"
        f"»✳️>⏱️ `Bot Uptime   : {uptime} `\n"
        "`▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱`"
    )
       if ALIVE_LOGO:
          try:
            logo = ALIVE_LOGO
            await bot.send_file(alive.chat_id, logo, caption=output)
            await alive.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *`The provided logo is invalid."
                "\nMake sure the link is directed to the logo picture`"
            )
    else:
        await alive.edit(output)
