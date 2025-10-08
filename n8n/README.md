# N8N Website Performance Analysis Workflow

An automated workflow for analyzing and comparing website performance using N8N, Google PageSpeed Insights API, and optional AI analysis.

## Overview

This N8N workflow provides comprehensive website performance analysis including:

- **Performance metrics** from Google PageSpeed Insights
- **Mobile and Desktop** analysis and comparison
- **Accessibility, SEO, and Best Practices** scores
- **Core Web Vitals** metrics (FCP, LCP, TBT, CLS, Speed Index)
- **Automated report generation** in Markdown format
- **Webhook trigger** for easy integration

## Inspiration

This workflow is inspired by the [Automate Website Performance Analysis using PageSpeed Insights](https://n8n.io/workflows/6166-automate-website-performance-analysis-and-comparison-using-gemini-and-pagespeed-insights/) workflow from the N8N community.

## Prerequisites

- N8N installed locally or on a server
- Google PageSpeed Insights API access (free tier available)
- Basic understanding of N8N workflows

## Installation

### 1. Install N8N

If you haven't installed N8N yet:

```bash
npm install n8n -g
```

Or using Docker:

```bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

### 2. Import the Workflow

1. Start N8N:
   ```bash
   n8n start
   ```

2. Open N8N in your browser: `http://localhost:5678`

3. Click on "Workflows" in the left sidebar

4. Click "Import from File" or "Import from URL"

5. Select the `workflow.json` file from this directory

6. The workflow will be imported and ready to configure

### 3. Configure API Credentials

The workflow uses Google PageSpeed Insights API:

#### Option 1: Without API Key (Limited requests)
- No configuration needed
- Subject to rate limiting

#### Option 2: With API Key (Recommended)
1. Get a free API key from [Google Cloud Console](https://console.cloud.google.com/)
2. Enable the PageSpeed Insights API
3. In N8N, configure the HTTP Request nodes with your API key:
   - Edit "PageSpeed Insights API - Mobile" node
   - Edit "PageSpeed Insights API - Desktop" node
   - Add `key` parameter with your API key value

## Usage

### Trigger the Workflow

The workflow can be triggered in several ways:

#### 1. Via Webhook (Recommended)

The workflow includes a webhook trigger. After activating the workflow:

```bash
# Using curl
curl -X POST https://your-n8n-instance.com/webhook/website-performance-audit \
  -H "Content-Type: application/json" \
  -d '{"websiteUrl": "https://example.com"}'

# Using wget
wget --post-data='{"websiteUrl": "https://example.com"}' \
  --header='Content-Type: application/json' \
  https://your-n8n-instance.com/webhook/website-performance-audit
```

#### 2. Manual Execution

1. Open the workflow in N8N
2. Click "Execute Workflow"
3. Provide a test URL in the webhook node
4. Click "Execute Workflow" again

#### 3. Schedule

Add a Schedule trigger node to run the workflow automatically:
- Daily, weekly, or monthly audits
- Monitor performance trends over time

## Workflow Components

### Nodes

1. **Webhook Trigger**: Accepts POST requests with website URL
2. **Check URL Provided**: Validates that a URL was provided
3. **HTTP Request - Get Website**: Fetches the website
4. **PageSpeed Insights API - Mobile**: Runs mobile performance audit
5. **PageSpeed Insights API - Desktop**: Runs desktop performance audit
6. **Parse Mobile Results**: Extracts key metrics from mobile audit
7. **Parse Desktop Results**: Extracts key metrics from desktop audit
8. **Merge Mobile and Desktop**: Combines results from both audits
9. **Format Report**: Structures data for reporting
10. **Aggregate Results**: Consolidates all metrics
11. **Generate Report**: Creates formatted Markdown report

### Data Flow

```
Webhook → Validation → Fetch Website → Split to Mobile & Desktop APIs
                                              ↓
                                      Parse Both Results
                                              ↓
                                         Merge Data
                                              ↓
                                       Format & Generate Report
```

## Output

The workflow generates a comprehensive Markdown report with:

### Performance Scores Table
```markdown
| Category | Mobile | Desktop |
|----------|--------|---------|
| Performance | 85/100 | 92/100 |
| Accessibility | 95/100 | 96/100 |
| Best Practices | 90/100 | 91/100 |
| SEO | 88/100 | 90/100 |
```

### Key Metrics
- First Contentful Paint (FCP)
- Largest Contentful Paint (LCP)
- Total Blocking Time (TBT)
- Cumulative Layout Shift (CLS)
- Speed Index

## Customization

### Add More Metrics

Edit the "Parse Mobile Results" and "Parse Desktop Results" nodes to extract additional metrics:

```javascript
{
  "name": "timeToInteractive",
  "value": "={{ $json.lighthouseResult.audits['interactive'].displayValue }}",
  "type": "string"
}
```

### Add AI Analysis (Optional)

Integrate with AI services like OpenAI or Google Gemini:

1. Add an AI node after "Aggregate Results"
2. Send the performance data to the AI
3. Get recommendations and insights
4. Include in the final report

Example prompt for AI:
```
Analyze these website performance metrics and provide recommendations:
- Performance: 85/100
- Accessibility: 95/100
- SEO: 88/100
Suggest 3-5 specific improvements.
```

### Store Results

Add a database node to store historical results:

1. Add a database node (PostgreSQL, MySQL, MongoDB, etc.)
2. Insert results after "Format Report"
3. Track performance trends over time
4. Create dashboards

### Send Notifications

Add notification nodes:

1. **Email**: Send report via email
2. **Slack**: Post to a Slack channel
3. **Discord**: Send to Discord webhook
4. **SMS**: Send alerts for critical issues

## Troubleshooting

### Workflow Fails to Execute

- Check that the webhook URL is correct
- Verify the website URL is valid and accessible
- Ensure API credentials are configured (if using API key)

### Rate Limiting Errors

- Add delays between API calls
- Use an API key for higher rate limits
- Reduce the frequency of workflow executions

### Missing Metrics

- Some websites may not return all metrics
- Add error handling to gracefully handle missing data
- Use default values for missing metrics

### Slow Execution

- PageSpeed Insights API can take 30-60 seconds per request
- Consider running mobile and desktop audits sequentially instead of parallel
- Add timeout settings to prevent hanging

## Advanced Features

### Comparison with Previous Results

1. Store results in a database
2. Query previous results
3. Calculate deltas and trends
4. Highlight improvements or regressions

### Multi-URL Analysis

Modify the workflow to analyze multiple URLs:

1. Add a "Split in Batches" node
2. Process URLs one at a time
3. Aggregate all results
4. Generate comparative report

### Custom Thresholds

Add conditional logic:

```javascript
if (performanceScore < 50) {
  // Send alert
  // Trigger remediation workflow
}
```

## Resources

- [N8N Documentation](https://docs.n8n.io/)
- [PageSpeed Insights API Documentation](https://developers.google.com/speed/docs/insights/v5/get-started)
- [Lighthouse Documentation](https://developer.chrome.com/docs/lighthouse/)
- [Web Vitals](https://web.dev/vitals/)

## Contributing

Contributions are welcome! Please feel free to:
- Submit improvements to the workflow
- Add new features
- Report issues
- Share your customizations

## License

This workflow is licensed under the MIT License - see the LICENSE file in the root directory.
