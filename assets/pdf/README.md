# PDF Assets Directory

This directory contains PDF files for projects and research notes.

## File Organization

- `project_name_report.pdf` - Main technical reports
- `project_name_presentation.pdf` - Presentation slides
- `project_name_supplementary.pdf` - Additional materials

## Usage in Projects

### Method 1: Front Matter Links
```yaml
---
pdf: assets/pdf/your_file.pdf
presentation: assets/pdf/your_presentation.pdf
---
```

### Method 2: Direct Links in Content
```markdown
<a href="{{ '/assets/pdf/your_file.pdf' | relative_url }}" target="_blank">Download PDF</a>
```

### Method 3: Styled Alert Boxes
```markdown
<div class="alert alert-info">
  <i class="fa-solid fa-file-pdf alert-icon"></i>
  <strong>Report:</strong> 
  <a href="{{ '/assets/pdf/your_file.pdf' | relative_url }}" target="_blank">Download Report</a>
</div>
```

### Method 4: Embedded PDF
```markdown
<iframe src="{{ '/assets/pdf/your_file.pdf' | relative_url }}" width="100%" height="600px">
  <p>Your browser does not support PDFs. <a href="{{ '/assets/pdf/your_file.pdf' | relative_url }}">Download the PDF</a>.</p>
</iframe>
```

## File Size Considerations

- Keep PDFs under 10MB for web performance
- Consider compressing large files
- Use descriptive filenames without spaces
