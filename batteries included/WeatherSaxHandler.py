from xml.parsers.expat import ParserCreate
class WeatherSaxHandler(object):
    def __init__(self):
        self.weather = {}
        self.today = {}
        self.tomorrow = {}
    def starttag(self, name, attrs):
        if name == 'yweather:location':
            self.weather['city'] = attrs['city']
            self.weather['country'] = attrs['country']
        if name == 'yweather:forecast':
            if attrs['day'] == 'Wed':
                self.today['text'] = attrs['text']
                self.today['low'] = int(attrs['low'])
                self.today['high'] = int(attrs['high'])
                self.weather['today'] = self.today
            if attrs['day'] == 'Thu':
                self.tomorrow['text'] = attrs['text']
                self.tomorrow['low'] = int(attrs['low'])
                self.tomorrow['high'] = int(attrs['high'])
                self.weather['tomorrow'] = self.tomorrow
    def endtag(self,name):
        pass
    def char_data(self, text):
        pass

def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.starttag
    parser.EndElementHandler = handler.endtag
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    return handler.weather

if __name__ == '__main__':
    
