'''
File: GradeScript1b.py
Author: Drew Wheeler
Last Edit: 2024-08-23


This file was written for lab 1b of the AI-Assisted Malware Analysis project funded by the NSF (Grant #2025682).


Script Usage: python3 -m unittest GradeScript1b.py

This file is intended to act as a grading script for the lab assignment associated with section 1b. It has been
configured such that the test cases utilize the same file as the lab assignment. However, given a sufficient
understanding of the code, the lab could be modified to acommodate any executable file.
'''

from unittest import TestCase
from FeatureExtraction1b import FeatureExtract


TEST_FILE = "ExamplePE.exe"


class TestFeatureExtract (TestCase):
    def setUp (self) -> None:
        self.sha256_hash:               str = "1df56772594a5ec2f550c7727a4879142736106da68b5d185c4391e08b48ec5e"
        self.target_machine:            str = "I386"
        self.sections:     dict[str, float] = {".text": 6.4723,
                                            ".rdata": 5.2098,
                                            ".data": 4.1106,
                                            ".ndata": 0.0000,
                                            ".rsrc": 5.7320}
        self.enc_target_machine:        int = 0x02
        self.enc_sections: dict[str, dict] = {".text": {"encoded": 0x000001, "entropy": 6.4723},
                                            ".rdata": {"encoded": 0x000002, "entropy": 5.2098},
                                            ".data": {"encoded": 0x000004, "entropy": 4.1106},
                                            ".ndata": {"encoded": 0x000008, "entropy": 0.0000},
                                            ".rsrc": {"encoded": 0x000010, "entropy": 5.7320}}
        self.features: FeatureExtract = FeatureExtract()
        self.features.extract_features (TEST_FILE)

    def test_sha256_hash (self) -> None:
        self.assertEqual (self.sha256_hash, self.features.sha256_hash)

    def test_sections (self) -> None:
        self.assertEqual (self.sections, self.features.section_info)

    def test_encode_machine (self) -> None:
        self.features.encode_target_machine()
        self.assertEqual (self.enc_target_machine, self.features.encoded_target_machine)
        self.features.decode_target_machine()

    def test_encode_sections (self) -> None:
        self.features.encode_section_info()
        self.assertEqual (self.enc_sections, self.features.encoded_sec_info)
        self.features.decode_section_info()

    def test_decode_machine (self) -> None:
        self.features.encode_target_machine()
        self.features.decode_target_machine()
        self.assertEqual (self.target_machine, self.features.target_machine)

    def test_decode_sections (self) -> None:
        self.features.encode_section_info()
        self.features.decode_section_info()
        self.assertEqual (self.sections, self.features.section_info)
