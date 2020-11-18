import asyncio

import requests
from telethon import functions
from userbot.helpers import yaml_format
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Noob"

HELPTYPE = Config.HELP_INLINETYPE or True


@borg.on(admin_cmd(outgoing=True, pattern="help ?(.*)"))
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
        input_str = event.pattern_match.group(1)
        if tgbotusername is None or input_str == "text":
            string = ""
            for i in CMD_LIST:
                string += "ℹ️ " + i + "\n"
                for iter_list in CMD_LIST[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                with io.BytesIO(str.encode(string)) as out_file:
                    out_file.name = "cmd.txt"
                    await bot.send_file(
                        event.chat_id,
                        out_file,
                        force_document=True,
                        allow_cache=False,
                        caption="**COMMANDS**",
                        reply_to=reply_to_id
                    )
                    await event.delete()
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "Commands found in {}:".format(input_str)
                for i in CMD_LIST[input_str]:
                    string += "    " + i
                    string += "\n"
                await event.edit(string)
            else:
                await event.edit(input_str + " is not a valid plugin!")
        else:
            help_string = """Userbot Helper.. \nProvided by @TechnoAyanBoT\n
`Userbot Helper to reveal all the commands`"""
            results = await bot.inline_query(  # pylint:disable=E0602
                tgbotusername,
                help_string
            )
            await results[0].click(
                event.chat_id,
                reply_to=event.reply_to_msg_id,
                hide_via=True
            )
            await event.delete()
    else:
        if HELPTYPE is True:
            help_string = f"Userbot Helper.. Provided by {DEFAULTUSER}\
                          \nUserbot Helper to reveal all the plugin names"
                          
            tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
            results = await bot.inline_query(  # pylint:disable=E0602
                tgbotusername, help_string
            )
            await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
            await event.delete()
        else:
            string = "<b>Please specify which plugin do you want help for !!\
                \nNumber of plugins : </b><code>{count}</code>\
                \n<b>Usage:</b> <code>.help</code> plugin name\n\n"
            catcount = 0
            for i in sorted(CMD_LIST):
                string += "• " + f"<code>{str(i)}</code>"
                string += "   "
                catcount += 1
            await event.edit(string.format(count=catcount), parse_mode="HTML")




@borg.on(admin_cmd(outgoing=True, pattern="check ?(.*)"))

async def info(event):
    """ For .info command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            event = await event.edit("Please specify a valid plugin name.")
            await asyncio.sleep(4)
            await event.delete()
    else:
        string = "<b>Please specify which plugin do you want help for !!\
            \nNumber of plugins : </b><code>{count}</code>\
            \n<b>Usage : </b><code>.info</code> <plugin name>\n\n"
        catcount = 0
        for i in sorted(CMD_HELP):
            string += "• " + f"<code>{str(i)}</code>"
            string += "   "
            catcount += 1
       
            await event.edit(string.format(count=catcount), parse_mode="HTML")


@borg.on(admin_cmd(pattern="dc$"))
async def _(event):
    result = await bot(functions.help.GetNearestDcRequest())
    result = (
        yaml_format(result)
        + "\n\n**List Of Telegram Data Centres:**\
                \nDC1 : Miami FL, USA\
                \nDC2 : Amsterdam, NL\
                \nDC3 : Miami FL, USA\
                \nDC4 : Amsterdam, NL\
                \nDC5 : Singapore, SG\
                "
    )
    await event.edit(result)


@borg.on(admin_cmd(outgoing=True, pattern="setinline (true|false)"))
async def _(event):
    global HELPTYPE
    input_str = event.pattern_match.group(1)
    if input_str == "true":
        type = True
    else:
        type = False
    if HELPTYPE is True:
        if type is True:
            await event.edit("`inline mode is already enabled`")
        else:
            HELPTYPE = type
            await event.edit("`inline mode is disabled`")
    else:
        if type is True:
            HELPTYPE = type
            await event.edit("`inline mode is enabled`")
        else:
            await event.edit("`inline mode is already disabled`")
