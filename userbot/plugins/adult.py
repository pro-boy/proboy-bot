import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import admin_cmd
from userbot import bot

borg.on(admin_cmd(pattern='r ?(.*) '))
@borg.on(events.NewMessage(pattern='.r (.*)'))
async def getmusic(so):
    if so.fwd_from:
        return
    r = so.pattern_match.group(1)
    chat = "@Epornerbot"
    link = f"{r}"
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
              await so.edit("```Please unblock @NeosMusicBot and try again```")
              return
          await so.edit("ur download is here😁")
          await asyncio.sleep(1)
          await bot.send_file(so.chat_id, respond)
    await so.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await so.delete()
