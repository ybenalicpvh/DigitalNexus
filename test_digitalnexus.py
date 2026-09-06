# test_digitalnexus.py
"""
Tests for DigitalNexus module.
"""

import unittest
from digitalnexus import DigitalNexus

class TestDigitalNexus(unittest.TestCase):
    """Test cases for DigitalNexus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DigitalNexus()
        self.assertIsInstance(instance, DigitalNexus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DigitalNexus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
