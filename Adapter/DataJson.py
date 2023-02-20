class DataJson:
    def __init__(self) -> None:
        self.information = """
        {
            "data" : {
            "information" : "Hola Mundo"
            }
        }
        """

    def getData(self):
        return self.information