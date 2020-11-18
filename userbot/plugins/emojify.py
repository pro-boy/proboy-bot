"""
Created by @Jisan7509
Peru helper @mrconfused
Userbot plugin for CatUserbot
"""
from userbot import CMD_HELP
from userbot.utils import admin_cmd
from userbot.helpers import emojify




@bot.on(admin_cmd(pattern="remoji(?: |$)(.*)"))
async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What am I Supposed to do with this nibba/nibbi, Give me a text. `"
        )
        return
    string = "  ".join(args).lower()
    for chutiya in string:
        if chutiya in emojify.kakashitext:
            bsdk = emojify.kakashiemoji[emojify.kakashitext.index(chutiya)]
            string = string.replace(chutiya, bsdk)
    await event.edit(string)


@bot.on(admin_cmd(pattern="cemoji(?: |$)(.*)"))
async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What am I Supposed to do with this nibba/nibbi, Give me a text. `"
        )
        return
    emoji, args = args.split(" ", 1)
    string = "  ".join(args).lower()
    for chutiya in string:
        if chutiya in emojify.kakashitext:
            bsdk = emojify.itachiemoji[emojify.kakashitext.index(chutiya)].format(
                cj=emoji
            )
            string = string.replace(chutiya, bsdk)
    await event.edit(string)


CMD_HELP.update(
    {
        "emojify": "__**PLUGIN NAME :** Emojify__\
      \n\n📌** CMD ➥** `.remoji` <text>\
      \n**USAGE   ➥  **Converts your text to big emoji text, with default emoji. \
      \n\n📌** CMD ➥** `.cemoji` <emoji> <text>\
      \n**USAGE   ➥  **Converts your text to big emoji text, with your custom emoji.\
      \n\n**☞ NOTE :** For giving sapce between two words use **@** symbol.\
      \n**EXAMPLE :**  `.remoji fuck@u`\
      \n                    `.cemoji 😋 suck@mine`"
    }
)
