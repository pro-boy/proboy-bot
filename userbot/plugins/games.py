from telethon import events
import asyncio
from telethon.tl.types import InputMediaDice

from userbot import CMD_HELP
from userbot.utils import admin_cmd
from var import Var


@borg.on(admin_cmd(pattern="xo$"))
async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob) 
    await tap[0].click(event.chat_id)
    await event.delete()




@borg.on(admin_cmd(outgoing=True, pattern="dice(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice(""))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice(""))
        except BaseException:
            pass


@borg.on(admin_cmd(outgoing=True, pattern="dart(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice("🎯"))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🎯"))
        except BaseException:
            pass


@borg.on(admin_cmd(outgoing=True, pattern="bb(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice("🏀"))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🏀"))
        except BaseException:
            pass


CMD_HELP.update(
    {
        "games": "`.dice` 1-6 or `.dart`1-6 or `.bb`1-5 or `.xo`\
\nUsage: hahaha just a magic.\nWarning:`Don't use any other values or bot will crash`"
    }
)
