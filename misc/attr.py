# -*- coding: utf-8 -*-


class SuerParser(object):

    def parser_XML(self, xml):
        print "XML..."

    def parser_HTML(self, html):
        print "HTML..."

    def parser_JSON(self, json):
        print "JSON..."

    def parser(self, **kwargs):
        try:
            func = getattr(self, 'parser_' + kwargs['type'])
            if func:
                func(kwargs['str'])
        except:
            print "Can't parser %s" % type


if __name__ == '__main__':
    parser = SuerParser()
    content = {
        "type": "XML",
        "str": "..."
    }
    parser.parser(**content)
