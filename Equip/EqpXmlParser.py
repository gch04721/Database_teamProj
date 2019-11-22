import csv, os
import xml.etree.ElementTree as ET

path = './Equip/'

file_list = os.listdir(path)
file_list = [file for file in file_list if file.endswith('.xml')]

Category = []

for file in file_list:
    tree = ET.parse(path + file)

    rootList = tree.findall('dir')
    
    for root in rootList:
        pass