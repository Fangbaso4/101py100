import requests
import re, json

url1 = 'https://i.tq121.com.cn/j/wap2016/news/city_data.js?2016'
content1 = requests.get(url1).text
# print(content1)

content = re.search('city_data=({.*});', content1)

c_group1 = content.group(1)
c_json = c_group1.replace('AREAID', '"AREAID"').replace('NAMECN', '"NAMECN"')
# print(c_json)

content_dic = json.dumps(c_json)
print('type(content_dic): ', type(content_dic))

result = 'city = {\n'

for p in content_dic:
    cities = content_dic[p]

    for c in cities:
        districts = cities[c]

        for d in districts:
            d_data = districts[d]
            line = "    '%s': '%s',\n" % (d_data['NAMECN'], d_data['AREAID'])
            result += line

result += '}'

f = open('city.py', 'w', encoding='utf-8')
f.write(result)
f.close()

