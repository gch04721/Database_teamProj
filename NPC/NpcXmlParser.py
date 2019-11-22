import csv, os
import xml.etree.ElementTree as ET

path = './NPC/'

file_list = os.listdir(path)
file_list = [file for file in file_list if file.endswith('.xml')]

NPCList = []

for file in file_list:
    tree = ET.parse(path + file)
    rootList = tree.findall('dir')

    for root in rootList:
        NPC_detail = {'key': int(), 'name': str(), 'loc' : int()}
        NPC_key = int(root.attrib['name'])
        NPC_name = None
        for child in root.iter('string'):
            if child.attrib['name'] == 'name':
                NPC_name = child.attrib['value']
        if NPC_name == None:
            continue
        NPC_detail['key'] = NPC_key
        NPC_detail['name'] = NPC_name

        NPCList.append(NPC_detail)


with open(path + 'NPC.csv', 'w', newline = '', encoding='utf-8') as csvFile:
    fileNames = ['key', 'name', 'loc']
    writer = csv.DictWriter(csvFile, fieldnames= fileNames)
    writer.writeheader()
    for NPC in NPCList:
        writer.writerow(NPC)
