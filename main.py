from api.oanda_api import OandaApi
from infrastructure.instrument_collection import InstrumentCollection

if __name__ == '__main__':
    api = OandaApi()

    #data = api.get_instruments()
    #print([x['name'] for x in data])
    InstrumentCollection.create_file(api.get_account_instruments(), "./data")
    InstrumentCollection.load_instruments("./data")
    InstrumentCollection.print_instrument()
