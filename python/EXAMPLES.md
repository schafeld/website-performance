# Example Usage

## Basic Usage

```bash
# Audit a website (mobile view by default)
python website_audit.py https://example.com
```

## Expected Output

```
🔍 Auditing https://example.com (mobile view)...

================================================================================
📊 WEBSITE AUDIT REPORT
================================================================================

🌐 URL: https://example.com
📱 Strategy: mobile
🕐 Timestamp: 2025-01-08T12:34:56.789012
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
ℹ️  No major frameworks or libraries detected

================================================================================
```

## Advanced Examples

### Desktop Analysis
```bash
python website_audit.py https://example.com --strategy desktop
```

### Both Mobile and Desktop
```bash
python website_audit.py https://example.com --both
```

### Save Results to JSON
```bash
python website_audit.py https://example.com --output results.json
```

### With API Key (Higher Rate Limits)
```bash
python website_audit.py https://example.com --api-key YOUR_GOOGLE_API_KEY
```

### Complete Example
```bash
python website_audit.py https://github.com \
  --both \
  --output github_audit.json \
  --api-key YOUR_GOOGLE_API_KEY
```

## JSON Output Format

When using `--output`, the JSON file contains:

```json
{
  "url": "https://example.com",
  "strategy": "mobile",
  "timestamp": "2025-01-08T12:34:56.789012",
  "scores": {
    "performance": 92.0,
    "accessibility": 95.0,
    "best_practices": 91.0,
    "seo": 88.0
  },
  "metrics": {
    "first-contentful-paint": {
      "value": 1234.5,
      "displayValue": "1.2 s",
      "score": 0.95
    },
    "largest-contentful-paint": {
      "value": 2100.0,
      "displayValue": "2.1 s",
      "score": 0.92
    },
    "total-blocking-time": {
      "value": 150.0,
      "displayValue": "150 ms",
      "score": 0.98
    },
    "cumulative-layout-shift": {
      "value": 0.05,
      "displayValue": "0.05",
      "score": 0.96
    },
    "speed-index": {
      "value": 2300.0,
      "displayValue": "2.3 s",
      "score": 0.94
    }
  },
  "tech_stack": {
    "frameworks": [],
    "libraries": [],
    "server": null,
    "cms": null
  },
  "final_url": "https://example.com/",
  "fetch_time": "2025-01-08T12:34:56.000Z"
}
```

## Interpreting Scores

### Score Ranges
- 🟢 **90-100**: Good - No action needed
- 🟡 **50-89**: Needs Improvement - Optimization recommended
- 🔴 **0-49**: Poor - Immediate attention required

### Key Metrics Thresholds

**First Contentful Paint (FCP)**
- Good: < 1.8s
- Needs Improvement: 1.8s - 3.0s
- Poor: > 3.0s

**Largest Contentful Paint (LCP)**
- Good: < 2.5s
- Needs Improvement: 2.5s - 4.0s
- Poor: > 4.0s

**Total Blocking Time (TBT)**
- Good: < 200ms
- Needs Improvement: 200ms - 600ms
- Poor: > 600ms

**Cumulative Layout Shift (CLS)**
- Good: < 0.1
- Needs Improvement: 0.1 - 0.25
- Poor: > 0.25

**Speed Index**
- Good: < 3.4s
- Needs Improvement: 3.4s - 5.8s
- Poor: > 5.8s
