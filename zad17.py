from xml.dom import minidom

doc = minidom.parse('zad17.xml')
films = doc.getElementsByTagName('film')
for film in films:
    if film.getElementsByTagName('title')[0].firstChild.data == 'Złap mnie jeśli potrafisz':
        film.getElementsByTagName('title')[0].firstChild.data = 'Szczęki'

with open('zad17_new.xml', 'w', encoding='utf-8') as fd:
    doc.writexml(fd)
