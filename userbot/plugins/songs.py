from telethon import events
import asyncio
from userbot.utils import admin_cmd
from userbot import bot, CMD_HELP
from telethon.errors.rpcerrorlist import YouBlockedUserError
import os
try:
 import subprocess
except:
 os.system("pip install instantmusic")



os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s "+name)

@borg.on(admin_cmd(pattern='song ?(.*) '))
@borg.on(events.NewMessage(pattern='.song (.*)'))
async def getmusic(so):
    if so.fwd_from:
        return
    song = so.pattern_match.group(1)
    chat = "@vkmusic_bot"
    link = f"{song}"
    await so.edit("searching ur song Boss🔍")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await so.edit("select the song ßoss😅😅")
          try:
              msg = await conv.send_message(link)
              response = await conv.get_response()
              respond = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await so.edit("```Please unblock @vkmusic_bot and try again```")
              return
          await so.edit("ur download is here😁")
          await asyncio.sleep(1)
          await bot.send_file(so.chat_id, respond)
    await so.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await so.delete()
