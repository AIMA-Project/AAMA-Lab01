from unittest import TestCase
from FeatureExtraction1b import FeatureExtract


TEST_FILE = "ExamplePE.exe"


class TestFeatureExtract (TestCase):
    def setUp (self) -> None:
        self.sha256_hash: str = "1df56772594a5ec2f550c7727a4879142736106da68b5d185c4391e08b48ec5e"
        self.target_machine: str = "I386"
        self.sections: dict() = {".text": 6.4723,
                                 ".rdata": 5.2098,
                                 ".data": 4.1106,
                                 ".ndata": 0.0000,
                                 ".rsrc": 5.7320}
        self.enc_target_machine: str = "0x02"
        self.enc_sections: dict() = {"0x000001": 6.4723,
                                     "0x000002": 5.2098,
                                     "0x000004": 4.1106,
                                     "0x000008": 0.0000,
                                     "0x000010": 5.7320}
        self.features: FeatureExtract = FeatureExtract()
        self.features.extract_features (TEST_FILE)

    def test_sha256_hash (self) -> None:
        self.assertEqual (self.sha256_hash, self.features.sha256_hash)

    def test_sections (self) -> None:
        self.assertEqual (self.sections, self.features.section_info)

    def test_encode_machine (self) -> None:
        self.features.encode_target_machine()
        self.assertEqual (self.enc_target_machine, self.features.target_machine)
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
