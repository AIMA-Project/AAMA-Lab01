import lief
from hashlib import sha256
from sys import argv

class FeatureExtract (object):
    def __init__ (self) -> None:
        self.sha256_hash:str = ""
        self.header_size:int = 0
        self.virtual_size:int = 0
        self.target_machine:str = "UNKNOWN"
        self.section_count:int = 0
        self.section_info:dict = {}
        
        self.encoded_sec_info: dict = {}

# === Paste Lab 1a Methods Below This Line =========================================================


# === Lab 1b Methods Start Here ====================================================================
# Encoding Schemes:
#
# Target Machine
#   UNKNOWN = 0x01 (0b00000001)
#   I386    = 0x02 (0b00000010)
#   AMD64   = 0x04 (0b00000100)
#   ARM64   = 0x08 (0b00001000)
#
# Section Names
#   .text     = 0x000001
#   .rdata    = 0x000002
#   .data     = 0x000004
#   .ndata    = 0x000008
#   .rsrc     = 0x000010
#   .itext    = 0x000020
#   .bss      = 0x000040
#   .idata    = 0x000080
#   .didata   = 0x000100
#   .edata    = 0x000200
#   .tls      = 0x000400
#   .buildid  = 0x000800
#   .reloc    = 0x001000
#   .UPX0     = 0x002000
#   .UPX1     = 0x004000
#   .qtmetad  = 0x008000
#   .qtmimed4 = 0x010000
#   .pdata    = 0x020000
#   .xdata    = 0x040000
#   .CRT      = 0x080000
#   .debug    = 0x100000
#


    def encode_target_machine (self) -> None:
        # Encode target machine using one-hot encoding schema
        pass
    
    def encode_section_info (self) -> None:
        # Encode section names using one-hot encoding schema
        pass
    
    def decode_target_machine (self) -> None:
        # Decode one-hot target machine back to string
        pass
    
    def decode_section_info (self) -> None:
        # Decode one-hot section names back to strings
        pass


# === Do not edit anything below this line =========================================================
def main (input_name: str = ""):
    extraction: FeatureExtract = FeatureExtract()
    extraction.extract_features (input_name)
    extraction.print_data()

if __name__ == "__main__":
    main (argv[1])
