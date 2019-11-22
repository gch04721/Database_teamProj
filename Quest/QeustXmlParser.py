import csv
import xml.etree.ElementTree as ET
import os

path = './Quest/'

file_list = os.listdir(path)
file_list = [file for file in file_list if file.endswith('.xml')]

tree = {}
for file in file_list:
    tmp = file.split('.')

    tree[tmp[1]] = ET.parse(path + file)


QuestList = []
QuestKeyIdx = {}
tmp_idx = 0
rootList_QuestInfo = tree['QuestInfo'].findall('dir') 
# find id, name, parent
Quest_key = 0
Quest_name = ''
for root_QuestInfo in rootList_QuestInfo:
    Quest_parent = ' ' # 있을수도 없을수도 있음
    Quest_detail = {'key': int(), 'name':str(), 'npc':int(),'lvmin':int(), 'exp':int(), 'parent':str(), 'job':[]}
    Quest_key = int(root_QuestInfo.attrib['name'])
    for child_QuestInfo in root_QuestInfo.iter('string'):
        tmp_name = child_QuestInfo.attrib['name']
        tmp_value = child_QuestInfo.attrib['value']
        if tmp_name == 'name':
            if tmp_value.find('–') != -1:
                print(tmp_value.find('–'))
                print(tmp_value)
            tmp_value.replace('–', '')
            
            Quest_name = tmp_value

        if tmp_name == 'parent':
            Quest_parent = tmp_value
    Quest_detail['key'] = Quest_key
    Quest_detail['name'] = Quest_name
    Quest_detail['parent'] = Quest_parent
    QuestList.append(Quest_detail)
    QuestKeyIdx[Quest_key] = tmp_idx
    tmp_idx += 1

# find exp
Quest_exp = 0 
rootList_Act = tree['Act'].findall('dir')
for root_Act in rootList_Act:
    Quest_job = []
    Quest_key = int(root_Act.attrib['name'])
    for child_Act in root_Act.iter('int32'):
        tmp_name = child_Act.attrib['name']
        tmp_value = int(child_Act.attrib['value'])
        if tmp_name == 'exp':
            Quest_exp = tmp_value

    idx = QuestKeyIdx[Quest_key]
    QuestList[idx]['exp'] = Quest_exp

# find #npc, lvmin, job
Quest_npc = 0
Quest_lvmin = 0
rootList_Check = tree['Check'].findall('dir')
for root_Check in rootList_Check:
    Quest_job = []
    Quest_key = int(root_Check.attrib['name'])
    idx = QuestKeyIdx[Quest_key]
    for child_dir in root_Check.iter('dir'):
        dir_num = child_dir.attrib['name']

        if dir_num == '0':
            for child_npc in child_dir.iter('int32'):
                tmp_name = child_npc.attrib['name']
                tmp_value = child_npc.attrib['value']
                if tmp_name == 'npc':
                    Quest_npc = int(tmp_value)
                    QuestList[idx]['npc'] = Quest_npc
                if tmp_name == 'lvmin':
                    Quest_lvmin = int(tmp_value)
                    QuestList[idx]['lvmin'] = Quest_lvmin

            for child_job in child_dir.iter('dir'):
                tmp_name = child_job.attrib['name']
                if tmp_name == 'job':
                    for child_job_num in child_job.iter('int32'):
                        Quest_job.append(int(child_job_num.attrib['value']))
                    QuestList[idx]['job'] = Quest_job    
    
with open(path + "Quest.csv", 'w', newline = '', encoding='utf-8') as csvFile:
    fieldNames = ['key', 'name', 'npc', 'lvmin', 'exp', 'parent', 'job']
    writer = csv.DictWriter(csvFile, fieldnames = fieldNames)

    writer.writeheader()
    for Quest in QuestList:
        
        writer.writerow(Quest)