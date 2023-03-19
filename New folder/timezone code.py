from datetime import datetime
import pytz
import pycountry_convert as pc
for tz in pytz.all_timezones:
    target_word=tz
    split_word = '/'
    city_in_data = target_word.partition(split_word)[2]
    print (city_in_data)
    if city_in_data=='Karachi':
        print(city_in_data)

##UTC = pytz.utc
##
##datetime_utc = datetime.now(UTC)
##print("Date & Time in UTC : ",
##      datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
##
##country_code = pc.country_name_to_country_alpha2("USA", cn_name_format="default")
##print(country_code)
##continent_name = pc.country_alpha2_to_continent_code(country_code)
##print(continent_name)
##pc.convert_continent_code_to_continent_name(continent_name)

##text="Africa/Abidjan"
##spl_word = '/'
##res = text.partition(spl_word)[2]
##print(res)
