#credits: @r4v4n4
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd

@borg.on(admin_cmd("r ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if reply_message.media:
       await event.edit("```reply to text message```")
       return
    chat = "@Epornerbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=432858024))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @sangmatainfo_bot and try again```")
                return
          await event.edit("`Sending Your Music...weit!😎`")
          await asyncio.sleep(1)
          await borg.send_file(so.chat_id, respond)
    await event.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await event.delete()
