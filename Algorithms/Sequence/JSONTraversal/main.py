import json
from unicodedata import numeric

def main():

    # byte literal embedding a json document
    # https://docs.python.org/3/library/stdtypes.html#bytes
    
    json_blob = json.loads(    '''
{
  "kind": "Pod",
  "apiVersion": "v1",
  "metadata": {
    "name": "mongo",
    "labels": {
      "name": "mongo",
      "role": "mongo"
    }
  },
  "spec": {
    "volumes": [
      {
        "name": "mongo-disk",
        "gcePersistentDisk": {
          "pdName": "mongo-disk",
          "fsType": "ext4"
        }
      }
    ],
    "containers": [
      {
        "name": "mongo",
        "image": "mongo:latest",
        "ports": [
          {
            "name": "mongo",
            "containerPort": 27017
          }
        ],
        "volumeMounts": [
          {
            "name": "mongo-disk",
            "mountPath": "/data/db"
          }
        ]
      }
    ]
  }
}    
    ''')

    def recurse(blob):
        for key, val in blob.items():
            if isinstance(val, dict):
                recurse(val)
            elif isinstance(val, list):
                print(val)
            elif isinstance(val, str):
                print(val)
            elif isinstance(val, bool):
                print(val)
            elif isinstance(val, int) or isinstance(val, float):
                print(val)
    
    recurse(json_blob)



if __name__ == '__main__':
    main()
