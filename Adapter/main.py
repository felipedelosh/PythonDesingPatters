from DataJson import *
from DataXML import *


d1 = DataJson()
d2 = DataXML()

#print(d1.getData())
#print(d2.getData())

#Use adapter
from Adapter import *

adapter = Adapter(d2)

information = adapter.getData()

print(information)
