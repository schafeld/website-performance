# Python Website Audit Tool

A comprehensive Python script to perform technical assessments of websites, including performance, accessibility, SEO, code quality, and technology stack detection.

## Features

- **Performance Analysis**: Measures key metrics like First Contentful Paint (FCP), Largest Contentful Paint (LCP), Total Blocking Time (TBT), Cumulative Layout Shift (CLS), and Speed Index
- **Accessibility Score**: Evaluates website accessibility based on WCAG guidelines
- **SEO Analysis**: Checks search engine optimization best practices
- **Best Practices Score**: Assesses overall code quality and web development standards
- **Tech Stack Detection**: Identifies frameworks, libraries, and technologies used
- **Mobile & Desktop Testing**: Supports auditing from both mobile and desktop perspectives
- **JSON Export**: Save detailed results to JSON files for further analysis

## Prerequisites

- Python 3.7 or higher
- Internet connection (to access Google PageSpeed Insights API)

## Installation

1. Navigate to the `python/` directory:
   ```bash
   cd python/
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Audit a website (mobile view by default):
```bash
python website_audit.py https://example.com
```

### Advanced Options

Audit with desktop view:
```bash
python website_audit.py https://example.com --strategy desktop
```

Audit both mobile and desktop:
```bash
python website_audit.py https://example.com --both
```

Save results to a JSON file:
```bash
python website_audit.py https://example.com --output results.json
```

Use with API key (for higher rate limits):
```bash
python website_audit.py https://example.com --api-key YOUR_GOOGLE_API_KEY
```

### Complete Example

```bash
python website_audit.py https://example.com \
  --strategy mobile \
  --output example_audit.json \
  --api-key YOUR_API_KEY
```

## Command-Line Arguments

- `url` (required): The URL of the website to audit
- `--strategy`: Choose `mobile` or `desktop` (default: `mobile`)
- `--both`: Run audits for both mobile and desktop
- `--output`: Specify a file path to save JSON results
- `--api-key`: Optional Google PageSpeed Insights API key for higher rate limits

## Getting a PageSpeed Insights API Key

While the tool works without an API key, using one provides higher rate limits:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the PageSpeed Insights API
4. Create credentials (API key)
5. Use the API key with the `--api-key` parameter

## Output

The tool provides:

### Console Output

A formatted report with:
- Overall scores (0-100) for Performance, Accessibility, Best Practices, and SEO
- Key performance metrics with visual indicators
- Detected technologies and frameworks
- Color-coded emoji indicators (🟢 good, 🟡 needs improvement, 🔴 poor)

### JSON Output (Optional)

Detailed JSON file containing:
- All scores and metrics
- Raw metric values
- Technology stack information
- Timestamps and URLs
- Full audit metadata

## Example Output

```
================================================================================
📊 WEBSITE AUDIT REPORT
================================================================================

🌐 URL: https://example.com
📱 Strategy: mobile
🕐 Timestamp: 2025-01-08T12:00:00
🔗 Final URL: https://example.com/

--------------------------------------------------------------------------------
📈 SCORES
--------------------------------------------------------------------------------
🟢 Performance            92.0/100
🟢 Accessibility          95.0/100
🟢 Best Practices         91.0/100
🟡 Seo                    88.0/100

--------------------------------------------------------------------------------
⚡ PERFORMANCE METRICS
--------------------------------------------------------------------------------
🟢 First Contentful Paint         1.2 s
🟢 Largest Contentful Paint       2.1 s
🟢 Total Blocking Time            150 ms
🟢 Cumulative Layout Shift        0.05
🟢 Speed Index                    2.3 s

--------------------------------------------------------------------------------
🔧 DETECTED TECHNOLOGIES
--------------------------------------------------------------------------------
⚛️  Frameworks: React
📚 Libraries: jQuery, Bootstrap

================================================================================
```

## Troubleshooting

### Rate Limiting

If you encounter rate limiting errors:
- Wait a few minutes before trying again
- Use a Google PageSpeed Insights API key (see above)
- Reduce the frequency of requests

### Connection Errors

If you get connection errors:
- Check your internet connection
- Verify the URL is accessible
- Ensure the URL includes `http://` or `https://` (or the tool will add `https://` automatically)

### Invalid URL

Make sure the URL:
- Is publicly accessible
- Uses a valid domain name
- Includes the protocol (http:// or https://) or let the tool add it

## Technical Details

The tool uses:
- **Google PageSpeed Insights API v5**: For comprehensive web performance analysis
- **Lighthouse**: Google's automated tool for auditing web pages (via PageSpeed API)
- **Python Requests**: For HTTP communications

## Limitations

- Requires internet connectivity
- Subject to Google PageSpeed Insights API rate limits (higher limits with API key)
- Can only audit publicly accessible websites
- Tech stack detection is based on URL patterns and may not catch all technologies

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file in the root directory.
