# Blog Post Scripts

This directory contains scripts to automatically generate blog posts with proper front matter. The scripts can create both regular blog posts and research note posts with special tagging.

## Available Scripts

### 1. `create_blog_post.sh` (Shell Script)
A bash script for quick blog post creation with command-line arguments.

**Usage:**
```bash
./scripts/create_blog_post.sh "Post Title" [type] ["Project Name"] ["Description"]
```

**Post Types:**
- `research-note` - A research note (default)
- `blog-post` - A regular blog post

**Examples:**
```bash
# Create a research note
./scripts/create_blog_post.sh "Force Field Validation" research-note "Modelling Gold Stress Strain Curves in LAMMPS"

# Create a regular blog post
./scripts/create_blog_post.sh "My Thoughts on Jekyll" blog-post "" "Personal reflections"

# With description
./scripts/create_blog_post.sh "Coupling Tests" research-note "Designing a Silicon Nitride Waveguide" "Testing fiber coupling efficiency"
```

**Features:**
- Command-line argument support
- Interactive prompts for tags and categories
- Project validation against existing projects (for research notes)
- Colored output for better UX
- Automatic tagging (research notes get 'research-note' tag)

### 2. `create_blog_post.py` (Python - Recommended)
A Python script with interactive prompts and better error handling.

**Usage:**
```bash
python3 scripts/create_blog_post.py
```

**Features:**
- Interactive post type selection (research note vs blog post)
- Interactive project selection from available projects (for research notes)
- Input validation and error handling
- Colored terminal output
- No external dependencies (uses only Python standard library)
- YAML front matter generation
- Summary and confirmation before creation
- Automatic tagging for research notes

## Generated File Structure

All scripts create blog post files with this structure:

### For Research Notes:
```markdown
---
layout: post
title: "Your Research Note Title"
date: 2025-08-05
description: "Brief description"
tags:
  - research-note
  - tag1
  - tag2
categories:
  - research
related_project: "Project Name"
featured: false
---

## Overview
[Template content...]
```

### For Regular Blog Posts:
```markdown
---
layout: post
title: "Your Blog Post Title"
date: 2025-08-05
description: "Brief description"
tags:
  - blog
  - tag1
categories:
  - category1
featured: false
---

Write your blog post content here...
```

## Common Workflow

1. **Create a new blog post:**
   ```bash
   python3 scripts/create_blog_post.py
   ```

2. **Edit the generated file:**
   ```bash
   code _posts/2025-08-05-your-post-title.md
   ```

3. **Preview locally:**
   ```bash
   bundle exec jekyll serve
   ```

4. **View blog posts:** `http://localhost:4000/blog/`
5. **Filter research notes:** `http://localhost:4000/blog/tag/research-note/`

## Tips

### Post Types
- **Research Notes**: Use for research-related content, automatically tagged with `research-note`
- **Blog Posts**: Use for general content, tutorials, personal thoughts, etc.

### Project Names (Research Notes Only)
- Use exact project titles as they appear in `_projects/*.md`
- Scripts will validate against existing projects
- You can still use custom project names if needed

### Tags and Categories
**Research Note tags:** `research-note`, `simulation`, `experiment`, `analysis`, `literature-review`, `methodology`, `results`, `molecular-dynamics`, `photonics`, `optimization`

**Blog Post tags:** `technology`, `personal`, `tutorial`, `update`, `jekyll`, `programming`

**Common categories:** `research`, `blog`, `technology`, `personal`, `tutorial`, `project`

### Featured Posts
- Set `featured: true` to display in the featured section
- Featured posts appear at the top of the blog page

### File Naming
Scripts automatically create slugs from titles:
- "LAMMPS Parameter Study" → `2025-08-05-lammps-parameter-study.md`
- "My Jekyll Setup" → `2025-08-05-my-jekyll-setup.md`

## Filtering and Organization

The blog system supports filtering:
- **All posts**: `/blog/`
- **Research notes only**: `/blog/tag/research-note/`
- **By tag**: `/blog/tag/[tag-name]/`
- **By category**: `/blog/category/[category-name]/`

## Troubleshooting

### "Not in Jekyll site root directory"
Run scripts from the main site directory (where `_config.yml` is located):
```bash
cd /path/to/your/site
python3 scripts/create_blog_post.py
```

### "File already exists"
Either:
- Choose a different title
- Manually delete the existing file
- Add a suffix to make the title unique

### Permission denied
Make scripts executable:
```bash
chmod +x scripts/create_blog_post.sh
chmod +x scripts/create_blog_post.py
```

## Customization

### Modify Template Content
Edit the template content in the script files (search for "get_template_content" function).
Modify the front matter generation section to include additional fields like:
- `author`
- `thumbnail`
- `giscus_comments`
- `related_publications`

### Custom Categories/Tags
Modify the suggestion lists in the scripts to match your research areas.
