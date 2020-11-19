# HeHeHe  adult plugin is here lol
#  
# Created by @danish_00
# 
#
# Mi Iz pIrO 😂😂😂 

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="aboobs ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    reply_message = await event.get_reply_message()
    chat = "@Epornerbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=105460780))
              await event.client.send_message(chat, "/boobs")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Epornerbot ")
              return
          if response.text.startswith(" "):
             await event.edit("`Sorry sir, That @Epornerbot is dead now`")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)



@borg.on(admin_cmd(pattern="abutts ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    reply_message = await event.get_reply_message()
    chat = "@Epornerbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=105460780))
              await event.client.send_message(chat, "/butt")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Epornerbot ")
              return
          if response.text.startswith(" "):
             await event.edit("`Sorry sir, That @Epornerbot is dead now`")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)


@borg.on(admin_cmd(pattern="agifs ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    reply_message = await event.get_reply_message()
    chat = "@Epornerbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=105460780))
              await event.client.send_message(chat, "/gif")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Epornerbot ")
              return
          if response.text.startswith(" "):
             await event.edit("`Sorry sir, That @Epornerbot is dead now`")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)




# This Cmd is Not working in that Epornerbot bot so untill then lets leave this for future use hehe😂

"""

@borg.on(admin_cmd(pattern="agirl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    reply_message = await event.get_reply_message()
    chat = "@Epornerbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=105460780))
              await event.client.send_message(chat, "/random")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Epornerbot ")
              return
          if response.text.startswith(" "):
             await event.edit("`Sorry sir, That @Epornerbot is dead now`")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

"""
