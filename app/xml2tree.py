import xml.etree.ElementTree as ET
from collections import Counter
import re 

#find paths of elements 
def etree_iter_path(node, tag=None, path='.'):
    if tag == "*":
        tag = None
    if tag is None or node.tag == tag:
        yield node, path
    for child in node:
        _child_path = '%s/%s' % (path, child.tag)
        for child, child_path in etree_iter_path(child, tag, path=_child_path):
            yield child, child_path

#convert xml to tree
def makeTree(xmlfile):
    root = ET.fromstring(xmlfile)
    str_tree = ''
    for elem, path in etree_iter_path(root):
        path = str(path)
        path = path.replace('.', str(root.tag)+'    ')
        path = path.replace('/', '    ')
        spaces = Counter(path)
        tag_name = path.split()[-1].split('[')[0]
        tag_name = ' ' * (spaces[' '] - 4) + tag_name
        txt = str(elem.text)
        atr = str(elem.attrib)
        txt = txt.replace('\n', '')    
        txt = txt.replace('None', '')
        txt = txt.lstrip()
        if re.search('\w', txt):
            txt = ' \\' + txt
        if not (atr == '{}'):
            atr = '\n' + ' ' * spaces[' '] + '@ ' + atr
        atr = atr.replace('\'', '')
        atr = atr.replace('{', '')
        atr = atr.replace('}', '')
        atr = atr.replace(': ', ' \\')
        atr = atr.replace(',', '\n' + ' ' * (spaces[' ']) + '@')
        str_tree = str_tree + tag_name + txt + atr + '\n'
    return str_tree

