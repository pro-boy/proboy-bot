
from telethon import events

import asyncio

from uniborg.util import admin_cmd



@borg.on(admin_cmd(pattern="pornhub"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 8)

    await event.edit("`Connecting...`")

    animation_chars = [

            "P_",

            "PO_",

            "POR_",

            "PORN_",
            
            "PORNH_",
            
            "PORNHU_",
            
           "PORNHUB_", 
           
           "[PORNHUB](www.porn93.cc)"

        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 8])


@borg.on(admin_cmd(pattern=r"xvideos"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 7)

    await event.edit("`Connecting...`")

    animation_chars = [

            "X_",

            "XV_",

            "XVI_",

            "XVID_",
            
            "XVIDE_",
            
            "XVIDEO_",
            
            "[XVIDEOS](www.xvideos4.com)"

        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 7])




from telethon import events

import asyncio





@borg.on(admin_cmd(pattern=r"xnxx"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 5)

    await event.edit("`Connecting...`")

    animation_chars = [

            "X_",

            "XN_",

            "XNX_",

            "XNXX_",
            
            "[XNXX](www.xnxx.wapca.cc)👄_"
            
            
            
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 5])
