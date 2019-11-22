import csv, os
import xml.etree.ElementTree as ET

path = './Mob/'
file_list = os.listdir(path)
file_list = [file for file in file_list if file.endswith('.xml')]

for file in file_list:
    tree = ET.parse(path + file)

    rootList = tree.findall('dir')
    MobList = []
    for root in rootList:
        Mob_detail = {'key': int(), 'name' : str(), 'lv' : int(), 'att': int(), 'exp':int()}
        Mob_key = int(root.attrib['name'])
        for child in root.iter('string'):
            Mob_name = child.attrib['value']

        Mob_detail['key'] = Mob_key
        Mob_detail['name'] = Mob_name

        MobList.append(Mob_detail)

    with open(path + 'Mob.csv', 'w', newline = '', encoding='utf-8') as csvFile:
        fieldNames = ['key', 'name', 'lv','att','exp']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)

        writer.writeheader()
        for Mob in MobList:
            writer.writerow(Mob)