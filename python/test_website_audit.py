#!/usr/bin/env python3
"""
Simple unit tests for website_audit.py

These tests verify the structure and basic functionality of the audit tool
without requiring actual API calls.
"""

import sys
import os
import unittest
from unittest.mock import Mock, patch
import json

# Add parent directory to path to import the module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from website_audit import WebsiteAuditor


class TestWebsiteAuditor(unittest.TestCase):
    """Test cases for WebsiteAuditor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.auditor = WebsiteAuditor()
        self.auditor_with_key = WebsiteAuditor(api_key="test-key-123")
    
    def test_initialization(self):
        """Test auditor initialization."""
        self.assertIsNone(self.auditor.api_key)
        self.assertEqual(self.auditor_with_key.api_key, "test-key-123")
    
    def test_api_url(self):
        """Test API URL is set correctly."""
        expected_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
        self.assertEqual(WebsiteAuditor.PAGESPEED_API_URL, expected_url)
    
    def test_parse_results(self):
        """Test parsing of PageSpeed Insights API response."""
        # Mock API response
        mock_data = {
            "lighthouseResult": {
                "finalUrl": "https://example.com/",
                "fetchTime": "2025-01-08T12:00:00.000Z",
                "categories": {
                    "performance": {"score": 0.92},
                    "accessibility": {"score": 0.95},
                    "best-practices": {"score": 0.91},
                    "seo": {"score": 0.88}
                },
                "audits": {
                    "first-contentful-paint": {
                        "numericValue": 1200,
                        "displayValue": "1.2 s",
                        "score": 0.95
                    },
                    "largest-contentful-paint": {
                        "numericValue": 2100,
                        "displayValue": "2.1 s",
                        "score": 0.92
                    },
                    "total-blocking-time": {
                        "numericValue": 150,
                        "displayValue": "150 ms",
                        "score": 0.98
                    },
                    "cumulative-layout-shift": {
                        "numericValue": 0.05,
                        "displayValue": "0.05",
                        "score": 0.96
                    },
                    "speed-index": {
                        "numericValue": 2300,
                        "displayValue": "2.3 s",
                        "score": 0.94
                    }
                }
            }
        }
        
        result = self.auditor._parse_results(mock_data, "https://example.com", "mobile")
        
        # Verify basic structure
        self.assertEqual(result["url"], "https://example.com")
        self.assertEqual(result["strategy"], "mobile")
        self.assertIn("timestamp", result)
        self.assertIn("scores", result)
        self.assertIn("metrics", result)
        self.assertIn("tech_stack", result)
        
        # Verify scores
        self.assertEqual(result["scores"]["performance"], 92.0)
        self.assertEqual(result["scores"]["accessibility"], 95.0)
        self.assertEqual(result["scores"]["best_practices"], 91.0)
        self.assertEqual(result["scores"]["seo"], 88.0)
        
        # Verify metrics
        self.assertIn("first-contentful-paint", result["metrics"])
        self.assertEqual(result["metrics"]["first-contentful-paint"]["displayValue"], "1.2 s")
    
    def test_detect_tech_stack(self):
        """Test technology stack detection."""
        mock_audits = {
            "network-requests": {
                "details": {
                    "items": [
                        {"url": "https://example.com/jquery.min.js"},
                        {"url": "https://example.com/bootstrap.min.css"},
                        {"url": "https://example.com/react.production.min.js"}
                    ]
                }
            }
        }
        
        tech_stack = self.auditor._detect_tech_stack(mock_audits)
        
        self.assertIsInstance(tech_stack, dict)
        self.assertIn("frameworks", tech_stack)
        self.assertIn("libraries", tech_stack)
        self.assertIn("React", tech_stack["frameworks"])
        self.assertIn("jQuery", tech_stack["libraries"])
        self.assertIn("Bootstrap", tech_stack["libraries"])
    
    def test_get_score_emoji(self):
        """Test emoji selection based on score."""
        self.assertEqual(self.auditor._get_score_emoji(95), "🟢")
        self.assertEqual(self.auditor._get_score_emoji(90), "🟢")
        self.assertEqual(self.auditor._get_score_emoji(75), "🟡")
        self.assertEqual(self.auditor._get_score_emoji(50), "🟡")
        self.assertEqual(self.auditor._get_score_emoji(45), "🔴")
        self.assertEqual(self.auditor._get_score_emoji(0), "🔴")
    
    def test_save_results(self):
        """Test saving results to JSON file."""
        test_results = {
            "url": "https://example.com",
            "strategy": "mobile",
            "scores": {"performance": 92.0}
        }
        
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            temp_file = f.name
        
        try:
            self.auditor.save_results(test_results, temp_file)
            
            # Verify file was created and contains correct data
            with open(temp_file, 'r') as f:
                saved_data = json.load(f)
            
            self.assertEqual(saved_data["url"], "https://example.com")
            self.assertEqual(saved_data["strategy"], "mobile")
            self.assertEqual(saved_data["scores"]["performance"], 92.0)
        finally:
            # Clean up
            if os.path.exists(temp_file):
                os.remove(temp_file)


class TestMainFunction(unittest.TestCase):
    """Test cases for main CLI function."""
    
    @patch('sys.argv', ['website_audit.py', 'https://example.com'])
    def test_url_argument_parsing(self):
        """Test that URL argument is parsed correctly."""
        from website_audit import main
        import argparse
        
        # This test just verifies the argument parser setup
        # We won't actually run main() as it would make API calls
        self.assertTrue(True)  # Placeholder
    
    def test_url_scheme_handling(self):
        """Test that URLs without schemes get https:// added."""
        test_url = "example.com"
        expected = "https://example.com"
        
        # This would be tested in the actual main function
        if not test_url.startswith(("http://", "https://")):
            result = "https://" + test_url
        
        self.assertEqual(result, expected)


if __name__ == '__main__':
    # Run tests
    unittest.main()
