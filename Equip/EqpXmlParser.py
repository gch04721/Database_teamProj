import csv, os
import xml.etree.ElementTree as ET

path = './Equip/'

file_list = os.listdir(path)
file_list = [file for file in file_list if file.endswith('.xml')]

EquipList = {}
for file in file_list:
    tree = ET.parse(path + file)

    rootList = tree.findall('dir')
    
    cat = str()
    for root in rootList:
        for child in root.iter('dir'):
            name = child.attrib['name']
            Eqp_key = None
            Eqp_name = None
            if name=='Eqp':
                continue
            
            stat_detail = {'str' : int(), 'dex':int(),'int':int(), 'luk':int()}
            Eqp_detail = {'key':int(), 'name':str(), 'lv':int(), 'price':int(), 'job':[], 'stat_need' : stat_detail, 'stat_inc':stat_detail}

            if name.isdigit():
                Eqp_key = int(name)
            else:
                cat = name
                EquipList[cat] = []
                continue

            for _child in child.iter('string'):
                Eqp_name = _child.attrib['value']

            Eqp_detail['key'] = Eqp_key
            Eqp_detail['name'] = Eqp_name

            EquipList[cat].append(Eqp_detail)

for key in EquipList.keys():
    with open(path + key + '.csv', 'w', newline = '', encoding='utf-8') as csvFile:
        fieldNames = EquipList[key][0].keys()
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)

        writer.writeheader()
        for eqp in EquipList[key]:
            writer.writerow(eqp)