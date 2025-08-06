# Research Notes System (Now Blog-Based)

This repository now includes a blog-based research notes system that uses blog posts with special tagging to organize research content alongside regular blog posts.

## Overview

The research notes system now consists of:
- Blog posts with a special `research-note` tag
- A blog page at `/blog/` with filtering capabilities
- Integration with existing project pages
- Unified content management system
- Templates for creating new posts

## Creating Research Notes

### 1. Using Scripts (Recommended)

The easiest way to create research notes is using the automated scripts:

```bash
# Interactive Python script (recommended)
python3 scripts/create_blog_post.py

# Bash script with arguments
./scripts/create_blog_post.sh "Note Title" research-note "Project Name" ["Description"]
```

The scripts will:
- Auto-generate proper front matter
- Validate project names against existing projects (for research notes)
- Create appropriate file names and slugs
- Provide template structure based on post type
- Handle tags and categories interactively
- Automatically add `research-note` tag for research notes

See `scripts/README.md` for detailed usage instructions.

### 2. Manual Creation

Create a new markdown file in the `_posts/` directory with the following format:

```markdown
---
layout: post
title: "Your Research Note Title"
date: 2025-08-05
description: "Brief description of the research note"
tags:
  - research-note
  - tag1
  - tag2
categories:
  - research
related_project: "Exact Project Title"
featured: false
---

Your content here...
```

### 3. Using the Template

Copy a template structure for quick creation:

```bash
# Copy an existing research note post and modify it
cp _posts/2025-08-05-test-research-note.md _posts/YYYY-MM-DD-your-note-title.md
```

## Linking to Projects

To link a research note to a project:

1. Set the `related_project` field in the frontmatter to match the **exact title** of the project
2. The project title must match what's defined in the project's frontmatter

Example:
- Project title: `"Modelling Gold Stress Strain Curves in LAMMPS"`
- Research note: `related_project: "Modelling Gold Stress Strain Curves in LAMMPS"`

## Features

### Blog Page with Filtering
- View all posts at `/blog/`
- Quick filter for research notes: `/blog/tag/research-note/`
- Filter by any tag: `/blog/tag/[tag-name]/`
- Filter by category: `/blog/category/[category-name]/`
- Featured posts section
- Pagination support

### Project Integration
- Project pages can show related research notes
- Research notes can link back to projects
- Links to other notes from the same project

### Unified Content Management
- All content in `_posts/` directory
- Uses standard Jekyll blog functionality
- No custom collections or layouts
- Consistent with Jekyll best practices

### Navigation
- Blog page is in the main navigation
- Easy filtering between all posts and research notes
- Consistent styling across all post types

## File Structure

```
_posts/                    # All blog posts and research notes
├── 2025-08-04-first-post.md
├── 2025-08-05-test-research-note.md
└── 2025-08-05-your-new-post.md

scripts/                   # Generation scripts
├── create_blog_post.py    # Python script (recommended)
├── create_blog_post.sh    # Bash script
└── README.md

_pages/
├── blog.md               # Main blog page with filtering
└── ...

_projects/                # Project pages (for linking)
├── Molecular_Dynamics.md
└── Waveguide.md
```

## Front Matter Options

### For Research Notes:
- `layout`: Must be `post`
- `title`: Title of the research note
- `date`: Date in YYYY-MM-DD format
- `description`: Brief description shown in listings
- `tags`: Array of tags (must include `research-note`)
- `categories`: Array of categories
- `related_project`: Exact project title for linking
- `featured`: Set to `true` to show in featured section

### For Regular Blog Posts:
- `layout`: Must be `post`
- `title`: Title of the blog post
- `date`: Date in YYYY-MM-DD format
- `description`: Brief description
- `tags`: Array of tags
- `categories`: Array of categories
- `featured`: Set to `true` to show in featured section

## Examples

See the existing posts for examples:
- `/blog/` - All posts
- `/blog/tag/research-note/` - Research notes only
- Individual posts show proper tagging and project links

## Styling and Theme Support

The system includes theme-aware alert/note styling that adapts to both light and dark modes:

### Alert Types

```html
<!-- Info/Tip alerts (blue theme) -->
<div class="alert alert-info">
  <i class="fa-solid fa-lightbulb alert-icon"></i>
  <strong>Tip:</strong> Your tip content here.
</div>

<!-- Warning alerts (yellow/orange theme) -->
<div class="alert alert-warning">
  <i class="fa-solid fa-exclamation-triangle alert-icon"></i>
  <strong>Important:</strong> Your warning content here.
</div>

<!-- Danger alerts (red theme) -->
<div class="alert alert-danger">
  <i class="fa-solid fa-times-circle alert-icon"></i>
  <strong>Error:</strong> Your error content here.
</div>
```

### Theme Adaptation

- **Light Mode**: Uses light backgrounds with darker text for better readability
- **Dark Mode**: Uses darker backgrounds with lighter text and adjusted colors
- **Icons**: Automatically color-matched to the alert theme
- **Links**: Inherit theme colors and hover states

The research notes section cards also automatically adapt to the current theme with proper background colors, text colors, and border styles.
