from hashlib import md5
import time

class Strap:
    def __init__(self):
        pass
    @staticmethod
    def uid( email, pwd ):
        return md5( f"{email}-{pwd}".encode() ).hexdigest()

    @staticmethod
    def pid( uid, caption ):
        return md5( f"{uid}-{caption}-{time.time()}".encode() ).hexdigest()
