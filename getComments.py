import sys
import xml.dom.minidom


def agregarComentario(nodo, comentarios):
    metodo = nodo.getAttribute('name')
    ix = 0
    for (i, c) in enumerate(comentarios):
        if metodo in c:
            ix = i
            break
    comentario = ""
    for (i, c) in enumerate(reversed(comentarios[:ix])):
        c = c.replace('\n', '\\n').strip()
        if i == 0:
            if "'/" not in c:
                break
            else:
                continue
        if "/'" in c:
            break
        comentario = c + comentario
        
    comentario = comentario.strip().replace("'/" , '').replace("/'", '')
    nodo.setAttribute('label', comentario)


def main(filepath):
    lineas = []
    with open(filepath, 'r') as clase:
        lineas = clase.readlines()
    filepath = filepath.replace('.wsd', '.xmi').replace('.puml', '.xmi')
    doc = xml.dom.minidom.parse(filepath)
    uml = doc.childNodes[0].childNodes[3]
    for i in range(4):
        uml = uml.childNodes[1]
    for n in uml.childNodes:
        if n.nodeName == 'UML:Operation':
            agregarComentario(n, lineas)
    
    with open(filepath, 'w') as xmi:
        doc.writexml(xmi)


if __name__ == '__main__':
    main(sys.argv[1])
