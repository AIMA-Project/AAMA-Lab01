'''
File: FeatureExtraction.py
Author: Drew Wheeler
Last Edit: 2023-07-29_14:00-UTC


This file was written for Lab 1a of the AI-Assisted Malware Analysis Project,
funded by the NSF (grant #2025682).

This lab is intended to introduce the concept of feature extraction and how it
can be applied to the portable executable (PE) file format.


Script Usage: python3 FeatureExtraction.py [.exe file]


The details of the PE file originally used as part of this assignment are as
follows:
    File Name: npp.8.5.4.Installer.x64.exe
         Size: 4662072 bytes
      SHA-256: 1df56772594a5ec2f550c7727a4879142736106da68b5d185c4391e08b48ec5e
          URL: https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.5.4/npp.8.5.4.Installer.x64.exe


Instructions for completing the lab are as follows:
    1. Run the script without any modification, using the path of the .exe file
       as the [.exe file] argument.
    2. Take note of the missing features when the script prints to the terminal.
    3. Use the LIEF Python library to extract the features specified in each of
       the extraction methods below.
    4. Run the script one final time and ensure that each feature is extracted
       as expected.
    
Hint: The type hints for the variables declared in the __init__ method can help
      determine which feature should be extracted.


LIEF Documentation: https://lief-project.github.io/doc/stable/api/python/index.html#python-api-ref
Microsoft PE Documentation: https://learn.microsoft.com/en-us/windows/win32/debug/pe-format
'''


import lief
from hashlib import sha256
from sys import argv
from typing import Dict


class FeatureExtract (object):
    def __init__ (self) -> None:
        self.sha256_hash:    str = ""
        self.header_size:    int = 0
        self.virtual_size:   int = 0
        self.target_machine: str = "UNKNOWN"
        self.section_count:  int = 0
        self.section_info:   Dict[str, float] = {}
    
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
    
    def extract_header_s (self, binary: lief.PE.Binary = None) -> None:
        # Extract optional header size
        self.header_size = 0
    
    def extract_virtual_s (self, binary: lief.PE.Binary = None) -> None:
        # Extract virtual header size
        self.virtual_size = 0
    
    def extract_machine (self, binary: lief.PE.Binary = None) -> None:
        # Extract COFF header's target machine
        self.target_machine = ""
    
    def extract_sec_count (self, binary: lief.PE.Binary = None) -> None:
        # Extract COFF header's section count
        self.section_count = 0
    
    def extract_sec_data (self, binary: lief.PE.Binary = None) -> None:
        # Extract section names and their entropy
        for section in binary.sections:
            name: str = ""
            entropy: float = 0.0
            # name = section name (NOT the fullname)
            # entropy = section entropy
            self.section_info[name] = float (format (entropy, ".4f"))
    
    def print_data (self) -> None:
        print (self.sha256_hash)
        print (self.header_size)
        print (self.virtual_size)
        print (self.target_machine)
        print (self.section_count)
        print (self.section_info)


# === Do not edit anything below this line =========================================================
def main (input_name: str = ""):
    extraction: FeatureExtract = FeatureExtract()
    extraction.extract_features (input_name)
    extraction.print_data()

if __name__ == "__main__":
    main (argv[1])
