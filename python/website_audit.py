#!/usr/bin/env python3
"""
Website Performance Audit Tool

This script performs a comprehensive technical assessment of a website including:
- Performance metrics (via PageSpeed Insights API)
- Accessibility score
- SEO score
- Best practices
- Tech stack detection

Usage:
    python website_audit.py <url> [--api-key YOUR_API_KEY]
"""

import argparse
import json
import sys
import requests
from typing import Dict, Any, Optional
from datetime import datetime


class WebsiteAuditor:
    """Performs technical audits on websites using PageSpeed Insights API."""
    
    PAGESPEED_API_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the auditor.
        
        Args:
            api_key: Optional Google PageSpeed Insights API key for higher rate limits
        """
        self.api_key = api_key
    
    def audit_url(self, url: str, strategy: str = "mobile") -> Dict[str, Any]:
        """
        Audit a website URL.
        
        Args:
            url: The URL to audit
            strategy: "mobile" or "desktop"
            
        Returns:
            Dict containing audit results
        """
        print(f"🔍 Auditing {url} ({strategy} view)...")
        
        params = {
            "url": url,
            "strategy": strategy,
            "category": ["performance", "accessibility", "best-practices", "seo"]
        }
        
        if self.api_key:
            params["key"] = self.api_key
        
        try:
            response = requests.get(self.PAGESPEED_API_URL, params=params, timeout=60)
            response.raise_for_status()
            data = response.json()
            
            return self._parse_results(data, url, strategy)
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching data: {e}")
            sys.exit(1)
    
    def _parse_results(self, data: Dict[str, Any], url: str, strategy: str) -> Dict[str, Any]:
        """Parse the PageSpeed Insights API response."""
        
        lighthouse_result = data.get("lighthouseResult", {})
        categories = lighthouse_result.get("categories", {})
        audits = lighthouse_result.get("audits", {})
        
        # Extract scores
        scores = {
            "performance": categories.get("performance", {}).get("score", 0) * 100,
            "accessibility": categories.get("accessibility", {}).get("score", 0) * 100,
            "best_practices": categories.get("best-practices", {}).get("score", 0) * 100,
            "seo": categories.get("seo", {}).get("score", 0) * 100,
        }
        
        # Extract key metrics
        metrics = {}
        metric_keys = [
            "first-contentful-paint",
            "largest-contentful-paint",
            "total-blocking-time",
            "cumulative-layout-shift",
            "speed-index"
        ]
        
        for key in metric_keys:
            if key in audits:
                audit = audits[key]
                metrics[key] = {
                    "value": audit.get("numericValue"),
                    "displayValue": audit.get("displayValue"),
                    "score": audit.get("score")
                }
        
        # Tech stack detection
        tech_stack = self._detect_tech_stack(audits)
        
        return {
            "url": url,
            "strategy": strategy,
            "timestamp": datetime.now().isoformat(),
            "scores": scores,
            "metrics": metrics,
            "tech_stack": tech_stack,
            "final_url": lighthouse_result.get("finalUrl", url),
            "fetch_time": lighthouse_result.get("fetchTime")
        }
    
    def _detect_tech_stack(self, audits: Dict[str, Any]) -> Dict[str, Any]:
        """Detect technologies used on the website."""
        
        tech_stack = {
            "frameworks": [],
            "libraries": [],
            "server": None,
            "cms": None
        }
        
        # Check for common frameworks/libraries in diagnostics
        if "diagnostics" in audits:
            diagnostics = audits["diagnostics"].get("details", {})
            items = diagnostics.get("items", [])
            if items:
                item = items[0]
                # Server information
                tech_stack["server"] = item.get("serverResponseTime")
        
        # Check network requests for tech detection
        if "network-requests" in audits:
            requests_data = audits["network-requests"].get("details", {})
            items = requests_data.get("items", [])
            
            for req in items:
                url = req.get("url", "").lower()
                # Detect common libraries
                if "jquery" in url:
                    tech_stack["libraries"].append("jQuery")
                elif "react" in url:
                    tech_stack["frameworks"].append("React")
                elif "angular" in url:
                    tech_stack["frameworks"].append("Angular")
                elif "vue" in url:
                    tech_stack["frameworks"].append("Vue.js")
                elif "bootstrap" in url:
                    tech_stack["libraries"].append("Bootstrap")
        
        # Remove duplicates
        tech_stack["frameworks"] = list(set(tech_stack["frameworks"]))
        tech_stack["libraries"] = list(set(tech_stack["libraries"]))
        
        return tech_stack
    
    def print_report(self, results: Dict[str, Any]):
        """Print a formatted report to console."""
        
        print("\n" + "=" * 80)
        print(f"📊 WEBSITE AUDIT REPORT")
        print("=" * 80)
        print(f"\n🌐 URL: {results['url']}")
        print(f"📱 Strategy: {results['strategy']}")
        print(f"🕐 Timestamp: {results['timestamp']}")
        print(f"🔗 Final URL: {results['final_url']}")
        
        print("\n" + "-" * 80)
        print("📈 SCORES")
        print("-" * 80)
        
        scores = results['scores']
        for category, score in scores.items():
            emoji = self._get_score_emoji(score)
            category_name = category.replace("_", " ").title()
            print(f"{emoji} {category_name:20} {score:5.1f}/100")
        
        print("\n" + "-" * 80)
        print("⚡ PERFORMANCE METRICS")
        print("-" * 80)
        
        metrics = results['metrics']
        for metric_name, metric_data in metrics.items():
            if metric_data.get("displayValue"):
                name = metric_name.replace("-", " ").title()
                value = metric_data["displayValue"]
                score = metric_data.get("score", 0)
                emoji = self._get_score_emoji(score * 100) if score else "📊"
                print(f"{emoji} {name:30} {value}")
        
        print("\n" + "-" * 80)
        print("🔧 DETECTED TECHNOLOGIES")
        print("-" * 80)
        
        tech = results['tech_stack']
        if tech['frameworks']:
            print(f"⚛️  Frameworks: {', '.join(tech['frameworks'])}")
        if tech['libraries']:
            print(f"📚 Libraries: {', '.join(tech['libraries'])}")
        if tech['cms']:
            print(f"📝 CMS: {tech['cms']}")
        if not any([tech['frameworks'], tech['libraries'], tech['cms']]):
            print("ℹ️  No major frameworks or libraries detected")
        
        print("\n" + "=" * 80)
    
    def _get_score_emoji(self, score: float) -> str:
        """Get an emoji based on the score."""
        if score >= 90:
            return "🟢"
        elif score >= 50:
            return "🟡"
        else:
            return "🔴"
    
    def save_results(self, results: Dict[str, Any], output_file: str):
        """Save results to a JSON file."""
        
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n💾 Results saved to: {output_file}")


def main():
    """Main entry point for the CLI."""
    
    parser = argparse.ArgumentParser(
        description="Perform a comprehensive technical audit of a website",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python website_audit.py https://example.com
  python website_audit.py https://example.com --strategy desktop
  python website_audit.py https://example.com --api-key YOUR_KEY --output results.json
        """
    )
    
    parser.add_argument(
        "url",
        help="URL of the website to audit"
    )
    
    parser.add_argument(
        "--api-key",
        help="Google PageSpeed Insights API key (optional, for higher rate limits)",
        default=None
    )
    
    parser.add_argument(
        "--strategy",
        choices=["mobile", "desktop"],
        default="mobile",
        help="Audit strategy: mobile or desktop (default: mobile)"
    )
    
    parser.add_argument(
        "--output",
        help="Output JSON file path (optional)",
        default=None
    )
    
    parser.add_argument(
        "--both",
        action="store_true",
        help="Run audit for both mobile and desktop"
    )
    
    args = parser.parse_args()
    
    # Ensure URL has a scheme
    url = args.url
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    
    auditor = WebsiteAuditor(api_key=args.api_key)
    
    if args.both:
        # Run both mobile and desktop audits
        results_mobile = auditor.audit_url(url, "mobile")
        auditor.print_report(results_mobile)
        
        print("\n\n")
        
        results_desktop = auditor.audit_url(url, "desktop")
        auditor.print_report(results_desktop)
        
        if args.output:
            combined_results = {
                "mobile": results_mobile,
                "desktop": results_desktop
            }
            auditor.save_results(combined_results, args.output)
        
    else:
        # Run single audit
        results = auditor.audit_url(url, args.strategy)
        auditor.print_report(results)
        
        if args.output:
            auditor.save_results(results, args.output)


if __name__ == "__main__":
    main()
