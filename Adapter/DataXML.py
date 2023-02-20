class DataXML:
    def __init__(self) -> None:
        self.information = """
        <data>
            <information id="01">Hola Mundo</information>
        </data>
        """

    def getData(self):
        return self.information
