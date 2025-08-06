# Research Notes System

This repository now includes a research notes system that allows you to create and manage notes related to your research projects.

## Overview

The research notes system consists of:
- A new `research_notes` collection
- A dedicated research notes page at `/research-notes/`
- A custom layout for research notes with project linking
- Integration with existing project pages
- Templates for creating new notes

## Creating Research Notes

### 1. Using Scripts (Recommended)

The easiest way to create research notes is using the automated scripts:

```bash
# Interactive Python script (recommended)
python3 scripts/create_research_note_simple.py

# Bash script with arguments
./scripts/create_research_note.sh "Note Title" "Project Name" ["Description"]
```

The scripts will:
- Auto-generate proper front matter
- Validate project names against existing projects
- Create appropriate file names and slugs
- Provide a template structure
- Handle tags and categories interactively

See `scripts/README.md` for detailed usage instructions.

### 2. Manual Creation

Create a new markdown file in the `_research_notes/` directory with the following format:

```markdown
---
layout: research_note
title: "Your Research Note Title"
date: 2025-08-05
description: "Brief description of the research note"
tags: [tag1, tag2, tag3]
categories: [category]
related_project: "Exact Project Title"
featured: false
---

Your content here...
```

### 2. Using the Template

Copy the template from `_templates/research_notes/template.md` and customize it:

```bash
cp _templates/research_notes/template.md _research_notes/YYYY-MM-DD-your-note-title.md
```

## Linking to Projects

To link a research note to a project:

1. Set the `related_project` field in the frontmatter to match the **exact title** of the project
2. The project title must match what's defined in the project's frontmatter

Example:
- Project title: `"Modelling Gold Stress Strain Curves in LAMMPS"`
- Research note: `related_project: "Modelling Gold Stress Strain Curves in LAMMPS"`

## Features

### Research Notes Page
- View at `/research-notes/`
- Paginated listing of all research notes
- Featured notes section
- Links to related projects

### Project Integration
- Project pages automatically show related research notes
- Links back to the main research notes page

### Custom Layout
- Research notes use the `research_note` layout
- Shows related project information at the top
- Links to other notes from the same project
- Proper tagging and categorization

### Navigation
- Research notes page is in the main navigation (nav_order: 3)
- Consistent with blog page styling

## File Structure

```
_research_notes/           # Collection directory
├── 2025-08-03-quantum-photonics-review.md
├── 2025-08-04-waveguide-modes.md
└── 2025-08-05-lammps-optimization.md

_templates/research_notes/ # Templates
└── template.md

_layouts/
└── research_note.liquid  # Custom layout

_includes/
└── research_notes.liquid # Include for project pages

_pages/
└── research_notes.md     # Main research notes page
```

## Frontmatter Options

- `layout`: Must be `research_note`
- `title`: Title of the research note
- `date`: Date in YYYY-MM-DD format
- `description`: Brief description shown in listings
- `tags`: Array of tags for categorization
- `categories`: Array of categories
- `related_project`: Exact project title for linking
- `featured`: Set to `true` to show in featured section
- `thumbnail`: Optional image for the note

## Examples

See the existing research notes for examples:
- `/research-notes/2025/quantum-photonic-integration/`
- `/research-notes/2025/waveguide-mode-analysis-results/`
- `/research-notes/2025/lammps-simulation-parameters-optimization/`
