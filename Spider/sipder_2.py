# -*- coding: utf-8 -*-
import urllib
import urllib2
import gzip, StringIO
import zlib

request = urllib2.Request('http://www.google.cn')
request.add_header('Accept-encoding', 'gzip')

proxy_handler = urllib2.ProxyHandler({'http': 'xxx.xxx.xxx.xxx:xxxx'})
opener = urllib2.build_opener(proxy_handler)

response = opener.open(request)
html = response.read()

gzipped = response.headers.get('Content-Encoding')
if gzipped:
    html = StringIO.StringIO(html)
    #html = zlib.decompress(html, 16 + zlib.MAX_WBITS)
    gzipper = gzip.GzipFile(fileobj=html)
    html = gzipper.read()
else:
    html = html.decode('utf-8').encode('gdk')
    typeEncode = sys.getfilesystemencoding()##系统默认编码
    infoencode = chardet.detect(html).get('encoding','utf-8')##通过第3方模块来自动提取网页的编码
    html = content.decode(infoencode,'ignore').encode(typeEncode)##先转换成unicode编码，然后转换系统编码输出

print html


