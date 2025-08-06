# Research Notes Scripts

This directory contains scripts to automatically generate research notes with proper front matter.

## Available Scripts

### 1. `create_research_note.sh` (Shell Script)
A bash script for quick note creation with command-line arguments.

**Usage:**
```bash
./scripts/create_research_note.sh "Note Title" "Project Name" ["Description"]
```

**Examples:**
```bash
# Basic usage
./scripts/create_research_note.sh "Force Field Validation" "Modelling Gold Stress Strain Curves in LAMMPS"

# With description
./scripts/create_research_note.sh "Coupling Tests" "Designing a Silicon Nitride Waveguide" "Testing fiber coupling efficiency"
```

**Features:**
- Command-line argument support
- Interactive prompts for tags and categories
- Project validation against existing projects
- Colored output for better UX

### 2. `create_research_note_simple.py` (Python - Recommended)
A Python script with interactive prompts and better error handling.

**Usage:**
```bash
python3 scripts/create_research_note_simple.py
```

**Features:**
- Interactive project selection from available projects
- Input validation and error handling
- Colored terminal output
- No external dependencies (uses only Python standard library)
- YAML front matter generation
- Summary and confirmation before creation

### 3. `create_research_note.py` (Python - Advanced)
Full-featured Python script with command-line options (requires PyYAML).

**Installation:**
```bash
pip install PyYAML
```

**Usage:**
```bash
# Interactive mode
python3 scripts/create_research_note.py

# Command-line mode
python3 scripts/create_research_note.py --title "Note Title" --project "Project Name" --description "Description"
```

## Generated File Structure

All scripts create files with this structure:

```markdown
---
layout: research_note
title: "Your Note Title"
date: 2025-08-05
description: "Brief description"
tags:
  - tag1
  - tag2
categories:
  - category1
related_project: "Project Name"
featured: false
---

## Overview
[Template content...]
```

## Common Workflow

1. **Create a new research note:**
   ```bash
   python3 scripts/create_research_note_simple.py
   ```

2. **Edit the generated file:**
   ```bash
   code _research_notes/2025-08-05-your-note-title.md
   ```

3. **Preview locally:**
   ```bash
   bundle exec jekyll serve
   ```

4. **View at:** `http://localhost:4000/research-notes/`

## Tips

### Project Names
- Use exact project titles as they appear in `_projects/*.md`
- Scripts will validate against existing projects
- You can still use custom project names if needed

### Tags and Categories
**Common tags:** `simulation`, `experiment`, `analysis`, `literature-review`, `methodology`, `results`, `molecular-dynamics`, `photonics`, `optimization`

**Common categories:** `simulation`, `experiment`, `analysis`, `literature-review`, `methodology`, `results`

### Featured Notes
- Set `featured: true` to display in the featured section
- Featured notes appear at the top of the research notes page

### File Naming
Scripts automatically create slugs from titles:
- "LAMMPS Parameter Study" → `2025-08-05-lammps-parameter-study.md`
- "Waveguide Mode Analysis" → `2025-08-05-waveguide-mode-analysis.md`

## Troubleshooting

### "Not in Jekyll site root directory"
Run scripts from the main site directory (where `_config.yml` is located):
```bash
cd /path/to/your/site
python3 scripts/create_research_note_simple.py
```

### "File already exists"
Either:
- Choose a different title
- Manually delete the existing file
- Add a suffix to make the title unique

### Permission denied
Make scripts executable:
```bash
chmod +x scripts/create_research_note.sh
chmod +x scripts/create_research_note_simple.py
```

## Customization

### Modify Template Content
Edit the template content in the script files (search for "Template content" section).

### Add Custom Fields
Modify the front matter generation section to include additional fields like:
- `author`
- `thumbnail`
- `giscus_comments`
- `related_publications`

### Custom Categories/Tags
Modify the suggestion lists in the scripts to match your research areas.
