from borax.calendars import LunarDate
from borax.calendars.festivals import get_festival, LunarSchema, DayLunarSchema

today = LunarDate.today()
print(today.strftime('%Y年%L%M月%D'))  # '二〇一八年六月廿六'
print(today.strftime('今天的干支表示法为：%G'))  # '今天的干支表示法为：戊戌年庚申月辛未日'


festival = get_festival('春节')
print(festival.countdown())  # 7

dls = DayLunarSchema(month=12, day=1, reverse=1)
print(dls.countdown())  # 344
