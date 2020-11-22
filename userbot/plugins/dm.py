# hehe hehe hehe

import os
import re
from userbot import bot
from userbot.utils import admin_cmd
from userbot import CMD_HELP


@borg.on(admin_cmd(pattern="dm ?(.*)"))
async def _(dc):
 
    d = dc.pattern_match.group(1)
    
    c = d.split(" ")#hehe

    chat_id = c[0]
    try:  #dc hehe
        chat_id = int(chat_id)
    #hmm 🤔🤔🤔🤔
    except BaseException:#lalalala
        
        pass
  
    msg = ""
    for i in c[1:]:
        msg += i + " "
    if msg == "":#hoho
        return
    try:
        await borg.send_message(chat_id, msg)
        await dc.edit("`🔰Message Delivered!`")
    except BaseException:#hmmmmmmmmm🤔🤔
        await dc.edit(".dm (username) (text)")


CMD_HELP.update({"dm": ".dm (username) (text)"})
