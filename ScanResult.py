#  Copyright (c) 2024. Yoppy Yunhasnawa, Politeknik Negeri Malang.
#  This software is available under the MIT License.
#  Contact me at: yunhasnawa@polinema.ac.id.

class ScanResult:

    def __init__(self, id_scan: str, boardcomputer_name: str, mac_address_scan: list, ip_address_scan: str, timetaken: str):
        self.id_scan = id_scan
        self.boardcomputer_name = boardcomputer_name
        self.mac_address_scan = mac_address_scan
        self.ip_address_scan = ip_address_scan
        self.timetaken = timetaken

    def to_json(self) -> str:
        return ('{'
                '"id_scan":"' + self.id_scan + '", '
                '"boardcomputer_name": "' + self.boardcomputer_name + '", '
                '"ip_address_scan": "' + self.ip_address_scan + '", '
                '"timetaken": "' + self.timetaken + '", '
                '"mac_address_scan": ' + self.serialized_mac_address_scan() + '}')

    def serialized_mac_address_scan(self) -> str:
        serialized = '['
        for count, addr in enumerate(self.mac_address_scan):
            serialized += '"' + addr + '"'
            if count < len(self.mac_address_scan) - 1:
                serialized += ', '
        serialized += ']'
        return serialized
