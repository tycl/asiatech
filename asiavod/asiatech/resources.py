import uuid
from uuid import getnode

def macnumber():
    mac = getnode()
    return hex(mac)
    

def screenname(macnumber):
    picturename= uuid.uuid1()
    filename = str(picturename)
    return 'user_{0}/{1}'.format(macnumber, filename)
