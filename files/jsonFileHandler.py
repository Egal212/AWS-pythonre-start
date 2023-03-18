import json

def readJsonFile(fileName):
    data=""
    try:
        with open('files/insulin.json') as json_files:
            data =json.load(json_file)
    except IoError:
        print("Could not read file")
    return data
    
    
    