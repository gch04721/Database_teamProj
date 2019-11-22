import xml.etree.ElementTree as elemTree

# parser example & tester

# 해당 파일의 파싱을 수행
tree = elemTree.parse('Consume/String.Consume.img.xml')

# 'dir'태그를 모두 탐색
rootList = tree.findall('dir')

# 모든 dir 태그의 하위 태그를 탐색
for root in rootList[:10]:
    print(root.attrib['name'])
    for child in root.iter('string'):
        print(child.attrib['value'])
        print('test: ',  child.findtext('빨간 포션'))