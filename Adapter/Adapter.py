import json
import xml.etree.ElementTree as ET


class Adapter:
    def __init__(self, cls) -> None:
        self.cls = cls

    def getData(self):
        """
        Enter a instance DataJson or DataXML
        The output is the information
        """
        str_class = str(self.cls).lower()
        
        if "json" in str_class:
            data = json.loads(self.cls.getData())
            data = data["data"]["information"]
            return data
        elif "xml" in str_class:
            data = ET.fromstring(self.cls.getData())
            return data.find('information').text
