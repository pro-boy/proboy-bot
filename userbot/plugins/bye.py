# creator: @HELLBOY_OP
# Take credits if u gonna kang this LOL u noobs
# pic is inserted by @NOOB_GUY_OP
# Kangers stay away
from userbot.utils import admin_cmd, edit_or_reply
import asyncio
from telethon import events


@borg.on(admin_cmd(pattern="bye (.*)", outgoing=True))
async def _(event):
    name = event.pattern_match.group(1)
    Hell = await event.edit("Hey!")
    await asyncio.sleep(1)
    await Hell.edit("B")
    await asyncio.sleep(1)
    await Hell.edit("Y")
    await asyncio.sleep(1)
    await Hell.edit("BYE...")
    msg = f"BYE {name}"
    if name is None:
        await Hell.client.send_message(event.chat_id, "Bye", file="https://telegra.ph/file/8f1cbeef021f22eb96915.jpg")
    elif name is not None:
        await Hell.client.send_message(event.chat_id, msg, file="https://telegra.ph/file/8f1cbeef021f22eb96915.jpg")
