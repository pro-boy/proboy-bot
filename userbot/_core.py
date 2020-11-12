import asyncio
import os
from datetime import datetime
from pathlib import Path
from telethon.tl.types import InputMessagesFilterDocument
from userbot.utils import admin_cmd, load_module, remove_plugin, edit_or_reply
from userbot import ALIVE_NAME
from userbot import bot

DELETE_TIMEOUT = 5
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Mr.X"




        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()

@bot.on(admin_cmd(pattern=r"unload (?P<shortname>\w+)$"))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Successfully unloaded {shortname}")
    except Exception as e:
        await event.edit(
            "Successfully unloaded {shortname}\n{}".format(
                shortname, str(e)
            )
        )


@bot.on(admin_cmd(pattern=r"load (?P<shortname>\w+)$"))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await event.edit(f"Successfully loaded {shortname}")
    except Exception as e:
        await event.edit(
            f"Sorry, could not load {shortname} because of the following error.\n{str(e)}"
        )
