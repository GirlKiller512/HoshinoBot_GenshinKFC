import os
import random
from nonebot.exceptions import CQHttpError
from nonebot import MessageSegment
from hoshino import Service

sv = Service('genshinkfc', enable_on_default=True, visible=False)


def get_kfc():
    files = os.listdir(os.path.dirname(__file__) + '/record')
    rec = random.choice(files)
    return rec


@sv.on_fullmatch(('KFC', 'kfc', '原神KFC', '原神kfc', '二次元KFC', '二次元kfc', '异世相遇尽享美味'))
async def kfc(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/{get_kfc()}')
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")
