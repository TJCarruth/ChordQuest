import unittest
from chordquest.engine import ChordEngine

class TestChordEngine(unittest.TestCase):
    def test_major_chord(self):
        engine = ChordEngine(key="C")
        chord = engine.get_chord(1, "maj")
        self.assertIn("Chord 1", chord)

if __name__ == "__main__":
    unittest.main()