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

    await event.edit("```sending a  girl for u🍑```")

    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=105460780))
              await borg.send_message(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please do /start on  @Epornerbot and try again🤐")
              return
          if response.text.startswith("Forward"):
             await event.edit("Cn you kindly disable your forward privacy settings for good?😒")
          else: 
             await borg.send_file(event.chat_id, response.message.media)  
