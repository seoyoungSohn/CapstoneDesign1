import pandas as pd
import folium
import json

# df = pd.read_csv("old_people.csv", encoding="utf8")
# print(df)
#
# m = folium.Map(location = [37.65146111, 127.0583889], zoon_start = 3)

people_list = [("월계1동", 4209), ("월계2동", 5848), ("월계3동",6080), ("공릉1동",6509),
               ("공릉2동",5325), ("하계1동",4470), ("하계2동",3229), ("중계본동",2523),
               ("중계1동",2373), ("중계2.3동",7399), ("중계4동",4007), ("상계1동",6973),
               ("상계2동",3354), ("상계3.4동",6109), ("상계5동",5005), ("상계6.7동",5031),
               ("상계8동",2884), ("상계9동",3441), ("상계10동",2693)]
df = pd.DataFrame(people_list, columns=["동", "인구수"])
print(df)


