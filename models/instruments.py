class Instrument:

    def __init__(self, name, ins_type, display_name, pip_location,
                 trade_unit_precision, margin_rate):
        
        self.name = name
        self.ins_type = ins_type
        self.display_name = display_name
        self.pip_location = pow(10, pip_location)
        self.trade_unit_precision = trade_unit_precision
        self.margin_rate = float(margin_rate)

    def __repr__(self):
        return str(vars(self))
    
    @classmethod
    def FromApiObject(cls, ob):
        return Instrument(
            ob['name'],
            ob['type'],
            ob['displayName'],
            ob['pipLocation'],
            ob['tradeUnitsPrecision'],
            ob['marginRate']
        )
    