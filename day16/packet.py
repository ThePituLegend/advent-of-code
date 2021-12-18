class Packet:
    def __init__(self, version=None, packet_type=None):
        self.version = version
        self.packet_type = packet_type
        self.value = None
        self.operands = list()
        self.length_type = None
        self.length = None
    
    def __repr__(self):
        rep = f"Packet(\n\tv{self.version}"

        if self.packet_type:
            rep += f"\n\tType {self.packet_type}"

        if self.value:
            rep += f"\n\tValue => {self.value}"
        elif self.operands:
            rep += f"\n\tOperands => {self.operands}"
        
        rep += "\n)"

        return rep
    