import json

def main():

    # byte literal embedding a json document
    # https://docs.python.org/3/library/stdtypes.html#bytes
    blob = b'{"key": "value"}'
    
    print(json.loads(blob)["key"])

if __name__ == '__main__':
    main()