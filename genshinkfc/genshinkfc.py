import os
from nonebot.exceptions import CQHttpError
from nonebot import MessageSegment
from hoshino import R, Service, priv

sv = Service('genshinkfc', enable_on_default=True, visible=False)


@sv.on_fullmatch(('KFC', 'kfc', '原神KFC', '原神kfc', '二次元KFC', '二次元kfc'))
async def kfc(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/genshinkfc.mp3')
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")
