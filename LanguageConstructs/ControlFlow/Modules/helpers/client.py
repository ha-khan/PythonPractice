from urllib import request

# Names defined in this "top-level" scope become the attributes 
# of the module object when imported into another module
# so this module: helpers.client object will have HTTP_CLIENT as an attribute name
class HTTP_Client:
    def __init__(self, url: str) -> None:
        self.url = url
    
    def do(self)->None:
        with request.urlopen(self.url) as f:
            print(f.read(300))
