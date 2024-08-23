'''
File: FeatureExtraction1b.py
Author: Drew Wheeler
Last Edit: 2024-08-23


This file was written for Lab 1a of the AI-Assisted Malware Analysis Project,
funded by the NSF (grant #2025682).

This lab is intended to introduce the concept of feature extraction and how it
can be applied to the portable executable (PE) file format.

Script Usage: python3 FeatureExtraction1b.py [.exe File]


The details of the PE file originally used as part of this assignment are as
follows:
    File Name: npp.8.5.4.Installer.x64.exe
         Size: 4662072 bytes
      SHA-256: 1df56772594a5ec2f550c7727a4879142736106da68b5d185c4391e08b48ec5e
          URL: https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.5.4/npp.8.5.4.Installer.x64.exe

Instructions for completing the lab are as follows:
    1. Copy the class methods developed as part of Lab 1a into the FeatureExtract class definition.
    2. Implement the encoding functions the class contains using the provided encoding schema.
    3. Implement the decoding functions the class contains using the provided decoding schema.
    4. Run the script and ensure all data is encoded and decoded as expected.

Hint: The type hints for the variables declared in the __init__ method can help with determining the data type that
should be used for a given piece of data.

LIEF Documentation: https://lief-project.github.io/doc/stable/api/python/index.html#python-api-ref
Microsoft PE Documentation: https://learn.microsoft.com/en-us/windows/win32/debug/pe-format
'''

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

    def extract_features (self, file_name: str = "") -> None:
        binary: lief.PE.Binary = lief.parse (file_name)
        self.extract_sha256 (file_name)
        self.extract_header_s (binary)
        self.extract_virtual_s (binary)
        self.extract_machine (binary)
        self.extract_sec_count (binary)
        self.extract_sec_data (binary)
    
    def extract_sha256 (self, file_name: str = "") -> None:
        with open (file_name, "rb") as hasher:
            byte_stream = hasher.read()
            self.sha256_hash = sha256 (byte_stream).hexdigest()

    def print_data (self) -> None:
        print (self.sha256_hash)
        print (self.header_size)
        print (self.virtual_size)
        print (self.target_machine)
        print (self.section_count)
        print (self.section_info)
    

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
