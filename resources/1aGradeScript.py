'''
File: UnitTestGradeScript.py
Author: Drew Wheeler
Last Edit: 2023-07-29_15:09-UTC


This file was written for Lab 1a of the AI-Assisted Malware Analysis Project,
funded by the NSF (grant #2025682).


Script Usage: python3 -m unittest UnitTestGradeScript.py


This file is intended to act as a grading script for the lab 1a assignment. It
has been configured such that the test cases use the same file as the lab, but
could also be set up to use other PE-format files.


Instructions for configuring grade script for other PE file:
    1. Obtain the desired executable file that is in the PE format.
    2. Run the completed version of the lab script that is included with the
       instructor content. If the extraction script fails, most likely it is
       due to the input file not being in the PE format.
    3. Copy over the data printed out by that script to the TestFeatureExtract
       class below.

'''

# Use unittest as the actual grader, which prints out pass, fail, or error for
# each test case.
from unittest import TestCase

# Import the FeatureExtract class the student wrote as part of the lab. Its
# extraction methods will be tested and compared against known good data.
from FeatureExtraction import FeatureExtract


TEST_FILE = "ExamplePE.exe"


class TestFeatureExtract (TestCase):
    def setUp (self) -> None:
        # Orignal file is the x64 installer for Notepad++ v.8.5.4 (npp.8.5.4.Installer.x64.exe)
        self.sha256_hash:    str = "1df56772594a5ec2f550c7727a4879142736106da68b5d185c4391e08b48ec5e"
        self.header_size:    int = 446464
        self.virtual_size:   int = 446464
        self.target_machine: str = "I386"
        self.section_count:  int = 5
        self.sections:    dict() = {".text": 6.4723,
                                    ".rdata": 5.2098,
                                    ".data": 4.1106,
                                    ".ndata": 0.0000,
                                    ".rsrc": 5.7320}
        self.features: FeatureExtract = FeatureExtract()
        self.features.extract_features (TEST_FILE)

    def test_sha256_hash (self) -> None:
        self.assertEqual (self.sha256_hash, self.features.sha256_hash)
    
    def test_header_s (self) -> None:
        self.assertEqual (self.header_size, self.features.header_size)
    
    def test_virtual_s (self) -> None:
        self.assertEqual (self.virtual_size, self.features.virtual_size)
    
    def test_machine (self) -> None:
        self.assertEqual (self.target_machine, self.features.target_machine)
    
    def test_section_count (self) -> None:
        self.assertEqual (self.section_count, self.features.section_count)
    
    def test_sections (self) -> None:
        self.assertEqual (self.sections, self.features.section_info)

