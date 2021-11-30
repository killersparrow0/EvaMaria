# Ported from [CatUb/UniBorg]
# < Made by @e3ris for Ultroid >

"""✘ **Commands Available **

>>  {i}dart | 🎯 <1-6>
>>  {i}dice | 🎲  <1-6>
>>  {i}football | ⚽ <1-5>
>>  {i}ball | 🏀 <1-5>
>>  {i}bowl | 🎳 <1-6>
>>  {i}slot | 🎰
"""

from telethon import events
from telethon.tl.types import InputMediaDice

from . import *

# EMOJIS
DART_E_MOJI = "🎯"
DICE_E_MOJI = "🎲"
BALL_E_MOJI = "🏀"
FOOT_E_MOJI = "⚽️"
SLOT_E_MOJI = "🎰"
BOWL_E_MOJI = "🎳"


@ultroid_cmd(pattern=f"({DART_E_MOJI}|dart)( ([1-6])|$)")
async def emojigames(e):
    if e.fwd_from:
        return
    here = e.chat_id
    emoticon = e.pattern_match.group(1)
    args = e.pattern_match.group(2)
    try:
        await e.delete()
    except Exception:
        pass
    if emoticon == "dart":
        emoticon = "🎯"
    r = await e.client.send_file(
        here,
        InputMediaDice(emoticon=emoticon),
    )
    if args:
        try:
            required_number = int(args)
            while r.media.value != required_number:
                await r.delete()
                r = await e.client.send_file(here, InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass
    

@ultroid_cmd(pattern=f"({DICE_E_MOJI}|dice)( ([1-6])|$)")
async def emojigames(e):
    if e.fwd_from:
        return
    here = e.chat_id
    emoticon = e.pattern_match.group(1)
    input_str = e.pattern_match.group(2)
    try:
        await e.delete()
    except Exception:
        pass
    if emoticon == "dice":
        emoticon = "🎲"
    r = await e.client.send_file(here, InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await e.client.send_file(here, InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass



@ultroid_cmd(pattern=f"({BALL_E_MOJI}|ball)( ([1-5])|$)")
async def emojigames(e):
    if e.fwd_from:
        return
    here = e.chat_id
    emoticon = e.pattern_match.group(1)
    input_str = e.pattern_match.group(2)
    try:
        await e.delete()
    except Exception:
        pass
    if emoticon == "ball":
        emoticon = "🏀"
    r = await e.client.send_file(here, InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await e.client.send_file(here, InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass


@ultroid_cmd(pattern=f"({FOOT_E_MOJI}|football)( ([1-5])|$)")
async def emojigames(e):
    if e.fwd_from:
        return
    here = e.chat_id
    emoticon = e.pattern_match.group(1)
    input_str = e.pattern_match.group(2)
    try:
        await e.delete()
    except Exception:
        pass
    if emoticon == "football":
        emoticon = "⚽️"
    r = await e.client.send_file(here, InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await e.client.send_file(here, InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass


@ultroid_cmd(pattern=f"({SLOT_E_MOJI}|slot)")
async def emojigames(e):
    if e.fwd_from:
        return
    here = e.chat_id
    emoticon = e.pattern_match.group(1)
    try:
        await e.delete()
    except Exception:
        pass
    if emoticon == "slot":
        emoticon = "🎰"
    await e.client.send_file(here, InputMediaDice(emoticon=emoticon))


@ultroid_cmd(pattern=f"({BOWL_E_MOJI}|bowl)( ([1-6])|$)")
async def emojigames(e):
    if e.fwd_from:
        return
    here = e.chat_id
    emoticon = e.pattern_match.group(1)
    input_str = e.pattern_match.group(2)
    try:
        await e.delete()
    except Exception:
        pass
    if emoticon == "bowl":
        emoticon = "🎳"
    r = await e.client.send_file(here, InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await e.client.send_file(here, InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass
