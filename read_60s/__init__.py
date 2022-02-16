import requests
from .config import Config
from nonebot import require
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import json
import nonebot
from nonebot.adapters.onebot.v11 import (
    GROUP,
    PRIVATE_FRIEND,
    Bot,
    Message,
    MessageEvent,
    PrivateMessageEvent,
)

global_config = nonebot.get_driver().config
nonebot.logger.info("global_config:{}".format(global_config))
plugin_config = Config(**global_config.dict())
nonebot.logger.info("plugin_config:{}".format(plugin_config))
scheduler = require("nonebot_plugin_apscheduler").scheduler  # type:AsyncIOScheduler

def remove_upprintable_chars(s):
    return ''.join(x for x in s if x.isprintable())#去除imageUrl可能存在的不可见字符

async def read60s():
    #global msg  # msg改成全局，方便在另一个函数中使用
    msg = await suijitu()
    for qq in plugin_config.leetcode_qq_friends:
        await nonebot.get_bot().send_private_msg(user_id=qq, message=Message(msg))
    for qq_group in plugin_config.leetcode_qq_groups:
        await nonebot.get_bot().send_group_msg(group_id=qq_group, message=Message(msg))  # MessageEvent可以使用CQ发图片

async def suijitu():
    url="https://api.iyk0.com/60s"
    resp = requests.get(url)
    resp = resp.text
    resp = remove_upprintable_chars(resp)
    retdata = json.loads(resp)
    lst = retdata['imageUrl']
    pic_ti = f"[CQ:image,file={lst}]"
    return pic_ti

for index, time in enumerate(plugin_config.leetcode_inform_time):
    nonebot.logger.info("id:{},time:{}".format(index, time))
    scheduler.add_job(read60s, "cron", hour=time.hour, minute=time.minute, id=str(index))