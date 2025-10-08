# Website Performance Assessment Toolkit

A comprehensive toolkit for technical website performance assessments, combining Python automation and N8N workflow orchestration for analyzing performance, accessibility, SEO, code quality, and technology stack detection.

## 🚀 Features

- **Performance Analysis**: Measure Core Web Vitals (FCP, LCP, TBT, CLS, Speed Index)
- **Accessibility Assessment**: WCAG compliance and accessibility scores
- **SEO Evaluation**: Search engine optimization best practices
- **Best Practices**: Code quality and web development standards
- **Tech Stack Detection**: Identify frameworks, libraries, and technologies
- **Multi-Device Testing**: Mobile and desktop analysis
- **Automated Workflows**: N8N integration for continuous monitoring
- **Detailed Reports**: Console output and JSON export

## 📁 Project Structure

```
website-performance/
├── python/              # Python CLI tool for website audits
│   ├── website_audit.py # Main audit script
│   ├── requirements.txt # Python dependencies
│   └── README.md        # Python tool documentation
├── n8n/                 # N8N workflow for automation
│   ├── workflow.json    # N8N workflow definition
│   └── README.md        # N8N setup and usage guide
├── LICENSE              # MIT License
└── README.md            # This file
```

## 🛠️ Quick Start

### Python Tool

The Python tool provides a command-line interface for quick website audits:

```bash
cd python/
pip install -r requirements.txt
python website_audit.py https://example.com
```

For detailed usage and options, see [python/README.md](python/README.md).

### N8N Workflow

The N8N workflow enables automated, scheduled audits and integrations:

1. Install N8N: `npm install n8n -g`
2. Import the workflow from `n8n/workflow.json`
3. Configure and activate

For detailed setup instructions, see [n8n/README.md](n8n/README.md).

## 📊 What Gets Analyzed

### Performance Metrics
- **First Contentful Paint (FCP)**: Time until first content appears
- **Largest Contentful Paint (LCP)**: Time until main content loads
- **Total Blocking Time (TBT)**: Sum of time blocked from user interaction
- **Cumulative Layout Shift (CLS)**: Visual stability measurement
- **Speed Index**: How quickly content is visually displayed

### Assessment Categories
- **Performance Score** (0-100): Overall loading and runtime performance
- **Accessibility Score** (0-100): WCAG compliance and accessibility features
- **Best Practices Score** (0-100): Code quality and security best practices
- **SEO Score** (0-100): Search engine optimization effectiveness

### Technology Detection
- Frontend frameworks (React, Angular, Vue.js)
- JavaScript libraries (jQuery, Bootstrap, etc.)
- Content Management Systems
- Server technologies

## 💡 Use Cases

### Development Teams
- Monitor performance during development
- Catch regressions before deployment
- Set performance budgets and track compliance

### QA & Testing
- Include in CI/CD pipelines
- Automated pre-release checks
- Compare staging vs production performance

### Site Monitoring
- Track performance trends over time
- Alert on performance degradation
- Regular scheduled audits

### Client Reporting
- Generate comprehensive reports
- Benchmark against competitors
- Track improvement initiatives

## 🔧 Tools & Technologies

- **Python 3.7+**: CLI tool and scripting
- **N8N**: Workflow automation and orchestration
- **Google PageSpeed Insights API**: Performance analysis powered by Lighthouse
- **Lighthouse**: Google's automated auditing tool

## 📖 Documentation

Each component has detailed documentation:

- **[Python Tool Documentation](python/README.md)**: CLI usage, examples, and API key setup
- **[N8N Workflow Documentation](n8n/README.md)**: Workflow setup, customization, and integration

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests
- Improve documentation
- Share your use cases and workflows

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the [N8N PageSpeed Insights workflow](https://n8n.io/workflows/6166-automate-website-performance-analysis-and-comparison-using-gemini-and-pagespeed-insights/)
- Powered by Google's [PageSpeed Insights API](https://developers.google.com/speed/docs/insights/v5/get-started)
- Built on [Lighthouse](https://developer.chrome.com/docs/lighthouse/) technology

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check the documentation in `python/` and `n8n/` folders
- Review the [PageSpeed Insights API documentation](https://developers.google.com/speed/docs/insights/v5/get-started)

---

**Happy auditing! 🎯**
