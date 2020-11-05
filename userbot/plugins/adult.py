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
    pbot = so.pattern_match.group(1)
    chat = "@Epornerbot"
    link = f"{pbot}"
      

    await event.edit("searching ur song Boss🔍")
    async with bot.conversation(chat) as conv:
        
           try:     
              msg = await conv.send_message(link)
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=105460780))
              await borg.send_message(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please unblock @asciiart_bot and try again🤐")
              return
          if response.text.startswith("Forward"):
             await event.edit("Cn you kindly disable your forward privacy settings for good?😒")
          else: 
             await borg.send_file(event.chat_id, response.message.media)  
                
