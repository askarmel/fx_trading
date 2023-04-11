import json
from models.instruments import Instrument

class InstrumentCollection:
    FILENAME = "instruments.json"
    API_KEYS = ['name', 'type', 'displayName', 'pipLocation', 
         'displayPrecision', 'tradeUnitsPrecision', 'marginRate']
    
    def __init__(self):
        self.instruments_dict = {}

    def load_instruments(self, path):
        self.instruments_dict = {}
        filename =f"{path}/{self.FILENAME}"
        with open(filename, "r") as f:
            data = json.loads(f.read())
            for k, v in data.items():
                self.instruments_dict[k] = Instrument.FromApiObject(v)

    def create_file(self, data, path):
        if data is None:
            print("Instruments file creation failed")
            return
        
        instruments_dict = {}
        for i in data:
            key = i['name']
            instruments_dict[key] = {k: i[k] for k in self.API_KEYS}
        
        filename = f"{path}/{self.FILENAME}"
        with open(filename, "w") as f:
            f.write(json.dumps(instruments_dict, indent=2))
            


    def print_instrument(self):
        [print(k,v) for k, v in self.instruments_dict.items()]
        print(len(self.instruments_dict.keys()), "instruments")

InstrumentCollection = InstrumentCollection()

    