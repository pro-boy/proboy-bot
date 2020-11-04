#port to userbot by @MoveAngel

import datetime

from telethon import events

from telethon.errors.rpcerrorlist import YouBlockedUserError

from telethon.tl.functions.account import UpdateNotifySettingsRequest

from userbot import bot, CMD_HELP

from userbot.utils import admin_cmd

#@register(outgoing=True, pattern="^.q(?: |$)(.*)")

#@borg.on(admin_cmd(pattern=r"pbot(?: |$)(.*)"))
@borg.on(admin_cmd(pattern="pbot ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("Sir reply to sticker message")
       return
    reply_message = await event.get_reply_message() 
    
    chat = "@Epornerbot"
    await event.edit("Making a image")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=105460780))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Unblock me (@stickers_to_image_bot) to work")
              return
          if response.text.startswith("I understand only stickers"):
              await event.edit("Sorry i cant't convert it check wheter is non animated sticker or not")
          else:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=105460780))
              response = await response
              if response.text.startswith("..."):
                  response = conv.wait_event(events.NewMessage(incoming=True,from_users=105460780))
                  response = await response
                  await event.delete()
                  await event.client.send_message(event.chat_id, response.message , reply_to = reply_message.id)
              else:
                  await event.edit("try again")
          await bot.send_read_acknowledge(conv.chat_id)
