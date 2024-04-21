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

# === Paste Lab 1a Methods Above This Line =========================================================

# === Lab 1b Methods Start Here ====================================================================
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
