import datetime

from telethon import events

from telethon.errors.rpcerrorlist import YouBlockedUserError

from telethon.tl.functions.account import UpdateNotifySettingsRequest

from userbot import bot, CMD_HELP

from userbot.utils import admin_cmd

#@register(outgoing=True, pattern="^.q(?: |$)(.*)")

@borg.on(admin_cmd(pattern=r"pbot(?: |$)(.*)"))

async def _(event):

    if event.fwd_from:

        return 

    if not event.reply_to_msg_id:

       await event.edit("```Reply to any user message.```")

       return

    reply_message = await event.get_reply_message() 

    if not reply_message.text:

       await event.edit("```Reply to text message```")

       return

    chat = "@Epornerbot"

    sender = reply_message.sender

    if reply_message.sender.bot:

       await event.edit("```Reply to actual users message.```")

       return

    await event.edit("```Making a Quote```")

    async with bot.conversation(chat) as conv:

          try:     

              response = conv.wait_event(events.NewMessage(incoming=True,from_users=105460780))

              await bot.forward_messages(chat, reply_message)
              response = await conv.get_response()
              respond = await conv.get_response()

            
          except YouBlockedUserError: 

              await event.reply("```Please unblock @QuotLyBot and try again```")

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
