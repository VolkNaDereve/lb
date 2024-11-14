import json
import xml.etree.ElementTree as ET

# Функция для конвертации JSON в XML
def json_to_xml(json_data):
    root = ET.Element("People")
    
    for person in json_data:
        person_element = ET.SubElement(root, "Person")
        for key, value in person.items():
            ET.SubElement(person_element, key).text = str(value)

    return ET.tostring(root, encoding='unicode')

# Чтение JSON-данных из файла
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Конвертация и запись в XML-файл
with open('data.xml', 'w', encoding='utf-8') as xml_file:
    xml_file.write(json_to_xml(data))

print("Конвертация из JSON в XML завершена.")
