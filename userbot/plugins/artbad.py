import asyncio
import re
from userbot.uniborgConfig import Config
from userbot import bot, ALIVE_NAME
from userbot.utils import admin_cmd


USERID = bot.uid
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "HeHe"

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


# ==================================================================

C = (
    "\n......................................../´¯/) "
    "\n......................................,/¯../ "
    "\n...................................../..../ "
    "\n..................................../´.¯/"
    "\n..................................../´¯/"
    "\n..................................,/¯../ "
    "\n................................../..../ "
    "\n................................./´¯./"
    "\n................................/´¯./"
    "\n..............................,/¯../ "
    "\n............................./..../ "
    "\n............................/´¯/"
    "\n........................../´¯./"
    "\n........................,/¯../ "
    "\n......................./..../ "
    "\n....................../´¯/"
    "\n....................,/¯../ "
    "\n.................../..../ "
    "\n............./´¯/'...'/´¯¯`·¸ "
    "\n........../'/.../..../......./¨¯\ "
    "\n........('(...´...´.... ¯~/'...') "
    "\n.........\.................'...../ "
    "\n..........''...\.......... _.·´ "
    "\n............\..............( "
    "\n..............\.............\..."
)


GAMBAR_TITIT = """
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆       🍆🍆
"""

# =======================================================




@bot.on(admin_cmd(pattern=r"ohnoo$"))
async def kakashi(bsdk):
    if bsdk.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(11)
    bsdk = await bsdk.edit(f"**Ohhh nooooo **💦💦...")
    animation_chars = [
        "**Ohhh Baby..**😈",
        "__**Ohh Yeaah..**__\n\n 😈\n  |\  \n  |  \   \n 8=👊-D\n  |   \         \n 👟 👟       😲",
        "__**Ohh ohhh..**__\n\n 😈\n  |\  \n  |  \   \n  8=👊-D\n  |   \         \n 👟 👟       😲",
        "__**Ohh.. **__\n\n 😈\n  |\  \n  |  \   \n 8=👊-D\n  |   \         \n 👟 👟       😲",
        "__**Ohh baby..**__\n\n 😈\n  |\  \n  |  \   \n8=👊-D💦\n  |   \         \n 👟 👟       😲",
        "__**Yeaah..**__\n\n 😣\n  |\  \n  |  \   \n 8=👊-D💦\n  |   \         \n 👟 👟       😲",
        "__**Yeaah Yaaah..**__\n\n 😣\n  |\  \n  |  \   \n  8=👊-D💦\n  |   \         💦\n 👟 👟       😲",
        "__**Yaah baby..**__\n\n 😘\n  |\  \n  |  \   \n 8=👊-D💦\n  |   \         💦\n 👟 👟       🤤",
        "__**Ohhh..**__\n\n 😍\n  |\  \n  |  \   \n8=👊-D💦\n  |   \         💦\n 👟 👟       🤤",
        "__**Love u..**__\n\n 😘\n  |\  \n  |  \   \n 8=👊-D💦\n  |   \         \n 👟 👟       🤤",
        "__**Love u babe**__\n\n 😍\n  |\  \n  |  \   \n 8=👊-D\n  |   \         \n 👟 👟       🤤",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await bsdk.edit(animation_chars[i % 11])

@bot.on(admin_cmd(pattern=r"ohyaah$"))
async def kakashi(baby):
    await baby.edit(
        "**💪💪Ohhh Yeeah Baby**...\n\n"
        "／ イ  ..........(((ヽ   \n"
        "(  ﾉ       ￣—--＼    \n"
        "| (＼  (\🎩/)   ｜    )  \n"
        "ヽ ヽ` ( ͡° ͜ʖ ͡°) _ノ    /  \n"
        " ＼ | ⌒Ｙ⌒ /  /  \n"
        "   ｜ヽ  ｜  ﾉ ／  \n"
        "     ＼トー仝ーイ \n"
        "        ｜ ミ土彡/ \n"
        "         ) \      °   /  \n"
        "        (     \🌿 /  \n"
        "         /       /ѼΞΞΞΞΞΞΞD💨💦\n"
        "      /  /     /      \ \   \  \n"
        "      ( (    ).           ) ).  ) \n"
        "     (      ).            ( |    | \n"
        "      |    /                \    |\n"
        "      👞.                  👞",
    )


@bot.on(admin_cmd(pattern=r"foff$"))
async def bluedevilfooku(fooku):
    await fooku.edit(
        ".                       /¯ )\n"
        "                      /¯  /\n"
        "                    /    /\n"
        "              /´¯/'   '/´¯¯`•¸\n"
        "          /'/   /    /       /¨¯\ \n"
        "        ('(   (   (   (  ¯~/'  ')\n"
        "         \                        /\n"
        "          \                _.•´\n"
        "            \              (\n"
        "              \  \n"
        "Roses are RED\n"
        "Violets are BLUE\n"
        "This is my middle finger\n"
        "It just for U🖕😂\n",
    )


@bot.on(admin_cmd(pattern=r"mf$"))
async def kakashi(mf):
    await mf.edit(C)





@bot.on(admin_cmd(pattern=r"dick (.*)"))
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)
    titid = GAMBAR_TITIT
    if emoji:
        titid = titid.replace("🍆", emoji)
    await e.edit(titid)
