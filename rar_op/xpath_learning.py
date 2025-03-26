from lxml import etree


html = etree.parse('C:\\Users\\pc\\leave\\rar_op\\test.html', etree.HTMLParser())
element = html.xpath('//book')
print(element)
