{"changed":true,"filter":false,"title":"jsonFileHandler.py","tooltip":"/files/jsonFileHandler.py","value":"import json\n\ndef readJsonFile(fileName):\n    data=\"\"\n    try:\n        with open('files/insulin.json') as json_files:\n            data =json.load(json_file)\n    except IoError:\n        print(\"Could not read file\")\n    return data\n    \n    \n    ","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"remove","lines":[" "],"id":68},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"remove","lines":["b"]}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["b"],"id":69}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"remove","lines":["b"],"id":70}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["n"],"id":71}],[{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":[" "],"id":72},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["d"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["a"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["t"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":["a"]}],[{"start":{"row":9,"column":15},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":73},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":4},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":74},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":11,"column":4},"end":{"row":20,"column":15},"action":"insert","lines":["import json","","def readJsonFile(fileName):","    data = \"\"","    try:","        with open(fileName) as json_file:","            data = json.load(json_file)","    except IOError:","        print(\"Could not read file\")","    return data"],"id":75}],[{"start":{"row":20,"column":15},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":76},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]},{"start":{"row":21,"column":4},"end":{"row":22,"column":0},"action":"insert","lines":["",""]},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"insert","lines":["i"],"id":77},{"start":{"row":22,"column":5},"end":{"row":22,"column":6},"action":"insert","lines":["m"]},{"start":{"row":22,"column":6},"end":{"row":22,"column":7},"action":"insert","lines":["p"]},{"start":{"row":22,"column":7},"end":{"row":22,"column":8},"action":"insert","lines":["o"]},{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["r"]},{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":[" "],"id":78},{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["j"]},{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["s"]},{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["o"]},{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["n"]}],[{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["F"],"id":79},{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["i"]},{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["l"]},{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"insert","lines":["e"]},{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["H"]},{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":["a"]},{"start":{"row":22,"column":21},"end":{"row":22,"column":22},"action":"insert","lines":["n"]}],[{"start":{"row":22,"column":22},"end":{"row":22,"column":23},"action":"insert","lines":["d"],"id":80},{"start":{"row":22,"column":23},"end":{"row":22,"column":24},"action":"insert","lines":["l"]},{"start":{"row":22,"column":24},"end":{"row":22,"column":25},"action":"insert","lines":["e"]},{"start":{"row":22,"column":25},"end":{"row":22,"column":26},"action":"insert","lines":["r"]}],[{"start":{"row":22,"column":26},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":81},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":23,"column":4},"end":{"row":23,"column":5},"action":"insert","lines":["d"],"id":82},{"start":{"row":23,"column":5},"end":{"row":23,"column":6},"action":"insert","lines":["a"]},{"start":{"row":23,"column":6},"end":{"row":23,"column":7},"action":"insert","lines":["t"]},{"start":{"row":23,"column":7},"end":{"row":23,"column":8},"action":"insert","lines":["a"]},{"start":{"row":23,"column":8},"end":{"row":23,"column":9},"action":"insert","lines":["="]}],[{"start":{"row":23,"column":9},"end":{"row":23,"column":10},"action":"insert","lines":[" "],"id":83},{"start":{"row":23,"column":10},"end":{"row":23,"column":11},"action":"insert","lines":["j"]},{"start":{"row":23,"column":11},"end":{"row":23,"column":12},"action":"insert","lines":["s"]},{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"insert","lines":["o"]},{"start":{"row":23,"column":13},"end":{"row":23,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":23,"column":14},"end":{"row":23,"column":15},"action":"insert","lines":["F"],"id":84},{"start":{"row":23,"column":15},"end":{"row":23,"column":16},"action":"insert","lines":["i"]},{"start":{"row":23,"column":16},"end":{"row":23,"column":17},"action":"insert","lines":["l"]},{"start":{"row":23,"column":17},"end":{"row":23,"column":18},"action":"insert","lines":["e"]},{"start":{"row":23,"column":18},"end":{"row":23,"column":19},"action":"insert","lines":["H"]},{"start":{"row":23,"column":19},"end":{"row":23,"column":20},"action":"insert","lines":["a"]},{"start":{"row":23,"column":20},"end":{"row":23,"column":21},"action":"insert","lines":["n"]},{"start":{"row":23,"column":21},"end":{"row":23,"column":22},"action":"insert","lines":["d"]}],[{"start":{"row":23,"column":22},"end":{"row":23,"column":23},"action":"insert","lines":["l"],"id":85},{"start":{"row":23,"column":23},"end":{"row":23,"column":24},"action":"insert","lines":["e"]},{"start":{"row":23,"column":24},"end":{"row":23,"column":25},"action":"insert","lines":["r"]}],[{"start":{"row":23,"column":25},"end":{"row":23,"column":26},"action":"insert","lines":["."],"id":86},{"start":{"row":23,"column":26},"end":{"row":23,"column":27},"action":"insert","lines":["r"]},{"start":{"row":23,"column":27},"end":{"row":23,"column":28},"action":"insert","lines":["e"]},{"start":{"row":23,"column":28},"end":{"row":23,"column":29},"action":"insert","lines":["a"]},{"start":{"row":23,"column":29},"end":{"row":23,"column":30},"action":"insert","lines":["d"]}],[{"start":{"row":23,"column":30},"end":{"row":23,"column":31},"action":"insert","lines":["j"],"id":87}],[{"start":{"row":23,"column":30},"end":{"row":23,"column":31},"action":"remove","lines":["j"],"id":88}],[{"start":{"row":23,"column":30},"end":{"row":23,"column":31},"action":"insert","lines":["J"],"id":89},{"start":{"row":23,"column":31},"end":{"row":23,"column":32},"action":"insert","lines":["s"]},{"start":{"row":23,"column":32},"end":{"row":23,"column":33},"action":"insert","lines":["o"]},{"start":{"row":23,"column":33},"end":{"row":23,"column":34},"action":"insert","lines":["n"]}],[{"start":{"row":23,"column":34},"end":{"row":23,"column":35},"action":"insert","lines":["F"],"id":90},{"start":{"row":23,"column":35},"end":{"row":23,"column":36},"action":"insert","lines":["i"]},{"start":{"row":23,"column":36},"end":{"row":23,"column":37},"action":"insert","lines":["l"]},{"start":{"row":23,"column":37},"end":{"row":23,"column":38},"action":"insert","lines":["e"]}],[{"start":{"row":23,"column":38},"end":{"row":23,"column":40},"action":"insert","lines":["()"],"id":91}],[{"start":{"row":23,"column":39},"end":{"row":23,"column":41},"action":"insert","lines":["''"],"id":92}],[{"start":{"row":23,"column":40},"end":{"row":23,"column":41},"action":"insert","lines":["f"],"id":93},{"start":{"row":23,"column":41},"end":{"row":23,"column":42},"action":"insert","lines":["i"]},{"start":{"row":23,"column":42},"end":{"row":23,"column":43},"action":"insert","lines":["l"]},{"start":{"row":23,"column":43},"end":{"row":23,"column":44},"action":"insert","lines":["e"]},{"start":{"row":23,"column":44},"end":{"row":23,"column":45},"action":"insert","lines":["s"]}],[{"start":{"row":23,"column":45},"end":{"row":23,"column":46},"action":"insert","lines":["/"],"id":94},{"start":{"row":23,"column":46},"end":{"row":23,"column":47},"action":"insert","lines":["i"]},{"start":{"row":23,"column":47},"end":{"row":23,"column":48},"action":"insert","lines":["n"]},{"start":{"row":23,"column":48},"end":{"row":23,"column":49},"action":"insert","lines":["s"]},{"start":{"row":23,"column":49},"end":{"row":23,"column":50},"action":"insert","lines":["u"]},{"start":{"row":23,"column":50},"end":{"row":23,"column":51},"action":"insert","lines":["l"]},{"start":{"row":23,"column":51},"end":{"row":23,"column":52},"action":"insert","lines":["i"]},{"start":{"row":23,"column":52},"end":{"row":23,"column":53},"action":"insert","lines":["n"]}],[{"start":{"row":23,"column":53},"end":{"row":23,"column":54},"action":"insert","lines":["."],"id":95},{"start":{"row":23,"column":54},"end":{"row":23,"column":55},"action":"insert","lines":["j"]},{"start":{"row":23,"column":55},"end":{"row":23,"column":56},"action":"insert","lines":["s"]},{"start":{"row":23,"column":56},"end":{"row":23,"column":57},"action":"insert","lines":["o"]},{"start":{"row":23,"column":57},"end":{"row":23,"column":58},"action":"insert","lines":["n"]}],[{"start":{"row":23,"column":60},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":96},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":4},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":97},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":25,"column":4},"end":{"row":34,"column":35},"action":"insert","lines":["if data != \"\" :","    bInsulin = data['molecules']['bInsulin']","    aInsulin = data['molecules']['aInsulin']","    insulin = bInsulin + aInsulin","    molecularWeightInsulinActual = data['molecularWeightInsulinActual']","    print('bInsulin: ' + bInsulin)","    print('aInsulin: ' + aInsulin)","    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))","else:","    print(\"Error. Exiting program\")"],"id":98}],[{"start":{"row":34,"column":35},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":99},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]},{"start":{"row":35,"column":4},"end":{"row":36,"column":0},"action":"insert","lines":["",""]},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":36,"column":4},"end":{"row":38,"column":37},"action":"insert","lines":["bInsulin: fvnqhlcgshlvealylvcgergffytpkt","aInsulin: giveqcctsicslyqlenycn","molecularWeightInsulinActual: 5807.63"],"id":100}],[{"start":{"row":38,"column":37},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":101},{"start":{"row":39,"column":0},"end":{"row":40,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":40,"column":0},"end":{"row":41,"column":22},"action":"insert","lines":["Could not read file","Error. Exiting program"],"id":102}],[{"start":{"row":41,"column":22},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":103},{"start":{"row":42,"column":0},"end":{"row":43,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":22,"column":4},"end":{"row":43,"column":0},"action":"remove","lines":["import jsonFileHandler","    data= jsonFileHandler.readJsonFile('files/insulin.json')","    ","    if data != \"\" :","    bInsulin = data['molecules']['bInsulin']","    aInsulin = data['molecules']['aInsulin']","    insulin = bInsulin + aInsulin","    molecularWeightInsulinActual = data['molecularWeightInsulinActual']","    print('bInsulin: ' + bInsulin)","    print('aInsulin: ' + aInsulin)","    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))","else:","    print(\"Error. Exiting program\")","    ","    bInsulin: fvnqhlcgshlvealylvcgergffytpkt","aInsulin: giveqcctsicslyqlenycn","molecularWeightInsulinActual: 5807.63","","Could not read file","Error. Exiting program","",""],"id":104}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":8},"action":"remove","lines":["    "],"id":105}],[{"start":{"row":17,"column":8},"end":{"row":17,"column":12},"action":"remove","lines":["    "],"id":106}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"remove","lines":["    "],"id":107}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"insert","lines":["    "],"id":108}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"remove","lines":["    "],"id":109}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":8},"action":"remove","lines":["    "],"id":110}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":[" "],"id":111}],[{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":[" "],"id":112}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":8},"action":"remove","lines":["data"],"id":113},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":[" "]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":[" "]}],[{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"remove","lines":[" "],"id":114},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"remove","lines":[" "]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":[" "],"id":115}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"remove","lines":[" "],"id":116}],[{"start":{"row":7,"column":36},"end":{"row":7,"column":49},"action":"remove","lines":["as json_file:"],"id":117}],[{"start":{"row":8,"column":3},"end":{"row":8,"column":16},"action":"insert","lines":["as json_file:"],"id":118}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":119},{"start":{"row":6,"column":11},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":[" "],"id":120}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"remove","lines":[" "],"id":121}],[{"start":{"row":6,"column":11},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":122},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["a"],"id":124},{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":[" "],"id":125},{"start":{"row":7,"column":39},"end":{"row":7,"column":40},"action":"insert","lines":["j"]},{"start":{"row":7,"column":40},"end":{"row":7,"column":41},"action":"insert","lines":["s"]},{"start":{"row":7,"column":41},"end":{"row":7,"column":42},"action":"insert","lines":["o"]},{"start":{"row":7,"column":42},"end":{"row":7,"column":43},"action":"insert","lines":["n"]}],[{"start":{"row":7,"column":43},"end":{"row":7,"column":44},"action":"insert","lines":["_"],"id":126},{"start":{"row":7,"column":44},"end":{"row":7,"column":45},"action":"insert","lines":["f"]},{"start":{"row":7,"column":45},"end":{"row":7,"column":46},"action":"insert","lines":["i"]},{"start":{"row":7,"column":46},"end":{"row":7,"column":47},"action":"insert","lines":["l"]},{"start":{"row":7,"column":47},"end":{"row":7,"column":48},"action":"insert","lines":["e"]},{"start":{"row":7,"column":48},"end":{"row":7,"column":49},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":49},"end":{"row":7,"column":50},"action":"insert","lines":[":"],"id":127}],[{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"remove","lines":[":"],"id":128},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"remove","lines":["e"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"remove","lines":["l"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"remove","lines":["i"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["f"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["_"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["n"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":["o"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"remove","lines":["s"]}],[{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"remove","lines":["j"],"id":129},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"remove","lines":[" "]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"remove","lines":["s"]},{"start":{"row":8,"column":3},"end":{"row":8,"column":4},"action":"remove","lines":["a"]}],[{"start":{"row":8,"column":3},"end":{"row":8,"column":4},"action":"insert","lines":["d"],"id":130},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["a"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["t"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["a"]}],[{"start":{"row":6,"column":11},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":131},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["t"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["r"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["y"]}],[{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":[":"],"id":132}],[{"start":{"row":8,"column":3},"end":{"row":8,"column":4},"action":"insert","lines":[" "],"id":133}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":8},"action":"insert","lines":["    "],"id":134}],[{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"insert","lines":[" "],"id":135}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":8},"action":"insert","lines":["    "],"id":136}],[{"start":{"row":9,"column":8},"end":{"row":9,"column":12},"action":"insert","lines":["    "],"id":137}],[{"start":{"row":9,"column":8},"end":{"row":9,"column":12},"action":"remove","lines":["    "],"id":138}],[{"start":{"row":9,"column":8},"end":{"row":9,"column":12},"action":"insert","lines":["    "],"id":139}],[{"start":{"row":9,"column":38},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":140},{"start":{"row":10,"column":0},"end":{"row":10,"column":12},"action":"insert","lines":["            "]},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["x"],"id":141},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["c"]},{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["e"]},{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["p"]},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["I"],"id":142},{"start":{"row":10,"column":19},"end":{"row":10,"column":20},"action":"insert","lines":["o"]},{"start":{"row":10,"column":20},"end":{"row":10,"column":21},"action":"insert","lines":["e"]}],[{"start":{"row":10,"column":20},"end":{"row":10,"column":21},"action":"remove","lines":["e"],"id":143}],[{"start":{"row":10,"column":20},"end":{"row":10,"column":21},"action":"insert","lines":["E"],"id":144},{"start":{"row":10,"column":21},"end":{"row":10,"column":22},"action":"insert","lines":["r"]},{"start":{"row":10,"column":22},"end":{"row":10,"column":23},"action":"insert","lines":["r"]},{"start":{"row":10,"column":23},"end":{"row":10,"column":24},"action":"insert","lines":["o"]},{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"remove","lines":["e"],"id":145}],[{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"insert","lines":["r"],"id":146}],[{"start":{"row":10,"column":8},"end":{"row":10,"column":12},"action":"remove","lines":["    "],"id":147},{"start":{"row":10,"column":4},"end":{"row":10,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":[" "],"id":148}],[{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":[":"],"id":149}],[{"start":{"row":10,"column":19},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":150},{"start":{"row":11,"column":0},"end":{"row":11,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["p"],"id":151},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["r"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["i"]},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["n"]},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":11,"column":13},"end":{"row":11,"column":15},"action":"insert","lines":["()"],"id":152}],[{"start":{"row":11,"column":14},"end":{"row":11,"column":16},"action":"insert","lines":["\"\""],"id":153}],[{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"insert","lines":["C"],"id":154},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":["o"]},{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"insert","lines":["u"]},{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"insert","lines":["l"]},{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"insert","lines":["d"]}],[{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"insert","lines":[" "],"id":155},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"insert","lines":["n"]},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"insert","lines":["o"]},{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"insert","lines":["t"]}],[{"start":{"row":11,"column":24},"end":{"row":11,"column":25},"action":"insert","lines":[" "],"id":156},{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"insert","lines":["r"]},{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"insert","lines":["e"]},{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"insert","lines":["a"]},{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"insert","lines":["d"]}],[{"start":{"row":11,"column":29},"end":{"row":11,"column":30},"action":"insert","lines":[" "],"id":157},{"start":{"row":11,"column":30},"end":{"row":11,"column":31},"action":"insert","lines":["f"]},{"start":{"row":11,"column":31},"end":{"row":11,"column":32},"action":"insert","lines":["i"]},{"start":{"row":11,"column":32},"end":{"row":11,"column":33},"action":"insert","lines":["l"]},{"start":{"row":11,"column":33},"end":{"row":11,"column":34},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":8},"action":"insert","lines":["    "],"id":158}],[{"start":{"row":20,"column":3},"end":{"row":20,"column":4},"action":"insert","lines":[" "],"id":159}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":8},"action":"insert","lines":["    "],"id":160}],[{"start":{"row":20,"column":8},"end":{"row":20,"column":12},"action":"insert","lines":["    "],"id":161}],[{"start":{"row":22,"column":3},"end":{"row":22,"column":4},"action":"insert","lines":[" "],"id":162}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":8},"action":"insert","lines":["    "],"id":163}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":12},"action":"insert","lines":["    "],"id":164}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":12},"action":"remove","lines":["    "],"id":165}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":11},"action":"remove","lines":["def readJsonFile(fileName) :","    data=\"\""],"id":166}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["",""],"id":167},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":11,"column":4},"end":{"row":21,"column":4},"action":"remove","lines":["import json","","def readJsonFile(fileName):","    data = \"\"","    try:","        with open(fileName) as json_file:","             data = json.load(json_file)","    except IOError:","         print(\"Could not read file\")","    return data","    "],"id":168}],[{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"remove","lines":[" "],"id":169}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":27},"action":"remove","lines":["files/in"],"id":174},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["z"]}],[{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"remove","lines":["'"],"id":174},{"start":{"row":5,"column":36},"end":{"row":5,"column":37},"action":"remove","lines":["n"]},{"start":{"row":5,"column":35},"end":{"row":5,"column":36},"action":"remove","lines":["o"]},{"start":{"row":5,"column":34},"end":{"row":5,"column":35},"action":"remove","lines":["s"]},{"start":{"row":5,"column":33},"end":{"row":5,"column":34},"action":"remove","lines":["j"]},{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"remove","lines":["."]},{"start":{"row":5,"column":31},"end":{"row":5,"column":32},"action":"remove","lines":["n"]},{"start":{"row":5,"column":30},"end":{"row":5,"column":31},"action":"remove","lines":["i"]},{"start":{"row":5,"column":29},"end":{"row":5,"column":30},"action":"remove","lines":["l"]},{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"remove","lines":["u"]},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"remove","lines":["s"]}]]},"ace":{"folds":[],"scrolltop":19,"scrollleft":0,"selection":{"start":{"row":6,"column":12},"end":{"row":6,"column":12},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":0,"state":"start","mode":"ace/mode/python"}},"timestamp":1678737296231}