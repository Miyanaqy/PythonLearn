from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('SR<%s>' % tag)
        
    def handle_endtag(self, tag):
        print('EN</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('SD<%s/>' % tag)

    def handle_data(self, data):
        print('D'+data)

    def handle_comment(self,data):
        print('C<!--', data, '-->')

    def handle_entityref(self, name):
        print('E &%s;' % name)

    def handle_charref(self, name):
        print('CF &#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
