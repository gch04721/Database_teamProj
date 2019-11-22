import xml.etree.ElementTree as ET
import os

path = './'

file_list = os.listdir(path)
file_list = [file for file in file_list if file.endswith('.xml')]

consume_keyName = {int() : str()}
consume_info_list = []

for file in file_list[3:]:
    tree = ET.parse(path + file)
    rootList = tree.findall('dir')

    for root in rootList:
        consume_pk = int(root.attrib['name'])
        for child in root.iter("string"):
            if child.attrib['name'] == 'name':
                consume_keyName[consume_pk] = child.attrib['value']

for file in file_list[:3]:
    print(file)
    tree = ET.parse(path + file)

    rootList = tree.findall('dir')
    
    for root in rootList:
        consume_pk = int()
        name = str()
        price = int()
        hp = int()
        mp = int()
        consume_info = {'pk' : int(), 'name' : str(), 'price' : int(), 'hp' : int(), 'mp' : int()}

        consume_pk = int(root.attrib['name'])

        if consume_keyName.__contains__(consume_pk) == False:
            continue
        
        name = consume_keyName[consume_pk]

        for child in root.iter():
            if child.attrib['name'] == 'price':
                price = int(child.attrib['value'])

            if child.attrib['name'] == 'spec':
                for child in child.iter():
                    # 물약의 능력치에 관한 정보
                    # 이 부분에서 hp, mp에 관한 정보를 추출하면 된다
                    if child.attrib['name'] == 'hp':
                        hp = int(child.attrib['value'])
                    
                    if child.attrib['name'] == 'mp':
                        mp = int(child.attrib['value'])

                    if child.attrib['name'] == 'hpR':
                        hp_max = 99999
                        rate = int(child.attrib['value'])
                        hp = int(hp_max * rate / 100)
                    
                    if child.attrib['name'] == 'mpR':
                        mp_max = 99999
                        rate = int(child.attrib['value'])
                        mp = int(mp_max * rate / 100)
        if hp == 0 and mp == 0:
            continue
        else:
            consume_info['pk'] = consume_pk
            consume_info['name'] = name
            consume_info['price'] = price
            consume_info['hp'] = hp
            consume_info['mp'] = mp

            consume_info_list.append(consume_info)

import csv

with open(path + 'Consume.csv', 'w', newline = '') as csvFile:
    fieldNames = ['pk', 'name', 'price', 'hp', 'mp']
    writer = csv.DictWriter(csvFile, fieldnames = fieldNames)

    writer.writeheader()
    for consumeInfo in consume_info_list:
        writer.writerow(consumeInfo)