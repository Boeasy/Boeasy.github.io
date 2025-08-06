#!/usr/bin/env python3
"""
Blog Post Generator for Jekyll Site
Creates blog post files with proper front matter and template content.
Can create regular blog posts or research note posts with special tagging.
No external dependencies required.

Usage:
    python3 scripts/create_blog_post.py
"""

import os
import sys
import re
from datetime import datetime
from pathlib import Path

# Color codes for terminal output
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    BLUE = '\033[0;34m'
    YELLOW = '\033[1;33m'
    BOLD = '\033[1m'
    NC = '\033[0m'  # No Color

def print_colored(text, color):
    """Print colored text to terminal"""
    print(f"{color}{text}{Colors.NC}")

def create_slug(title):
    """Create URL-friendly slug from title"""
    # Convert to lowercase and replace non-alphanumeric with hyphens
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', title.lower())
    # Remove leading/trailing hyphens and multiple consecutive hyphens
    slug = re.sub(r'^-+|-+$', '', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug

def get_available_projects():
    """Get list of available projects from _projects directory"""
    projects = []
    projects_dir = Path("_projects")
    
    if not projects_dir.exists():
        return projects
    
    for project_file in projects_dir.glob("*.md"):
        try:
            with open(project_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Simple extraction of title from front matter
                lines = content.split('\n')
                in_front_matter = False
                for line in lines:
                    if line.strip() == '---':
                        if not in_front_matter:
                            in_front_matter = True
                        else:
                            break
                    elif in_front_matter and line.startswith('title:'):
                        # Extract title, handling quotes
                        title = line.replace('title:', '').strip()
                        title = title.strip('"\'')
                        projects.append(title)
                        break
        except Exception as e:
            print_colored(f"Warning: Could not read {project_file}: {e}", Colors.YELLOW)
    
    return sorted(projects)

def get_user_input(prompt, default=None, required=True):
    """Get user input with optional default value"""
    if default:
        full_prompt = f"{prompt} [{default}]: "
    else:
        full_prompt = f"{prompt}: "
    
    while True:
        response = input(full_prompt).strip()
        
        if response:
            return response
        elif default:
            return default
        elif not required:
            return ""
        else:
            print_colored("This field is required.", Colors.RED)

def get_post_type():
    """Get the type of post to create"""
    print_colored("\\nPost Types:", Colors.BLUE)
    print("  1. Research Note - A note related to research projects")
    print("  2. Regular Blog Post - A general blog post")
    
    while True:
        choice = input("\\nSelect post type (1-2): ").strip()
        
        if choice == "1":
            return "research_note"
        elif choice == "2":
            return "blog_post"
        else:
            print_colored("Please enter 1 or 2", Colors.RED)

def get_tags(post_type):
    """Get tags from user input"""
    if post_type == "research_note":
        default_tags = "research-note"
        suggestion = "research-note, simulation, analysis, molecular-dynamics"
    else:
        default_tags = "blog"
        suggestion = "technology, personal, tutorial, update"
    
    tags_input = get_user_input(
        f"Enter tags (comma-separated, e.g., '{suggestion}')",
        default=default_tags,
        required=False
    )
    
    if not tags_input:
        return [default_tags]
    
    # Split by comma and clean up
    tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
    
    # Ensure research-note tag is included for research notes
    if post_type == "research_note" and "research-note" not in tags:
        tags.insert(0, "research-note")
    
    return tags

def get_categories(post_type):
    """Get categories from user input"""
    if post_type == "research_note":
        print_colored("\\nCommon research categories: simulation, experiment, analysis, literature-review, methodology, results", Colors.BLUE)
        default_categories = "research"
    else:
        print_colored("\\nCommon blog categories: technology, personal, tutorial, project", Colors.BLUE)
        default_categories = "blog"
    
    categories_input = get_user_input(
        "Enter categories (comma-separated)",
        default=default_categories,
        required=False
    )
    
    if not categories_input:
        return [default_categories]
    
    # Split by comma and clean up
    categories = [cat.strip() for cat in categories_input.split(',') if cat.strip()]
    return categories

def select_project_interactive(available_projects, post_type):
    """Interactive project selection (only for research notes)"""
    if post_type != "research_note":
        return None
        
    if not available_projects:
        return get_user_input("Enter project name (optional)", required=False)
    
    print_colored("\\nAvailable projects:", Colors.BLUE)
    for i, project in enumerate(available_projects, 1):
        print(f"  {i}. {project}")
    
    print(f"  {len(available_projects) + 1}. Enter custom project name")
    print(f"  {len(available_projects) + 2}. No project (skip)")
    
    while True:
        choice = input(f"\\nSelect project (1-{len(available_projects) + 2}): ").strip()
        
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(available_projects):
                return available_projects[choice_num - 1]
            elif choice_num == len(available_projects) + 1:
                return get_user_input("Enter project name", required=False)
            elif choice_num == len(available_projects) + 2:
                return None
            else:
                print_colored(f"Please enter a number between 1 and {len(available_projects) + 2}", Colors.RED)
        except ValueError:
            print_colored("Please enter a valid number", Colors.RED)

def format_yaml_list(items):
    """Format a list as YAML array"""
    if not items:
        return "[]"
    return "\\n".join(f"  - {item}" for item in items)

def get_template_content(post_type):
    """Get template content based on post type"""
    if post_type == "research_note":
        return """

## Overview

Brief overview of what this note covers.

<div class="alert alert-info">
  <i class="fa-solid fa-lightbulb alert-icon"></i>
  <strong>Tip:</strong> Use the alert boxes below to highlight important information that adapts to both light and dark themes.
</div>

## Methodology

Describe the methods or approach used.

<div class="alert alert-warning">
  <i class="fa-solid fa-exclamation-triangle alert-icon"></i>
  <strong>Important:</strong> Remember to validate your parameters and document any assumptions.
</div>

## Results

Present your findings here.

### Key Findings

1. First finding
2. Second finding  
3. Third finding

## Discussion

Discuss implications and interpretations.

## Next Steps

- [ ] Action item 1
- [ ] Action item 2
- [ ] Action item 3

## References

- Reference 1
- Reference 2
"""
    else:
        return """

Write your blog post content here...

## Introduction

Start with an engaging introduction.

## Main Content

Add your main content sections here.

## Conclusion

Wrap up your thoughts.
"""

def create_blog_post(title, description, tags, categories, post_type, project_name=None, featured=False):
    """Create the blog post file"""
    # Create filename
    slug = create_slug(title)
    date = datetime.now().strftime('%Y-%m-%d')
    filename = f"_posts/{date}-{slug}.md"
    
    # Check if file exists
    if os.path.exists(filename):
        print_colored(f"Error: File {filename} already exists", Colors.RED)
        return None
    
    # Create directory if it doesn't exist
    os.makedirs("_posts", exist_ok=True)
    
    # Create front matter
    front_matter = f"""---
layout: post
title: "{title}"
date: {date}
description: "{description}"
tags:
{format_yaml_list(tags)}
categories:
{format_yaml_list(categories)}"""
    
    # Add project field only for research notes
    if post_type == "research_note" and project_name:
        front_matter += f"""
related_project: "{project_name}\""""
    
    front_matter += f"""
featured: {str(featured).lower()}
---"""
    
    # Get template content
    content = get_template_content(post_type)
    
    # Write file
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(front_matter)
            f.write(content)
        
        post_type_display = "Research note" if post_type == "research_note" else "Blog post"
        print_colored(f"✓ {post_type_display} created successfully: {filename}", Colors.GREEN)
        return filename
    
    except Exception as e:
        print_colored(f"Error creating file: {e}", Colors.RED)
        return None

def main():
    # Check if we're in the right directory
    if not os.path.exists('_config.yml'):
        print_colored("Error: Not in Jekyll site root directory", Colors.RED)
        print("Please run this script from the root of your Jekyll site.")
        sys.exit(1)
    
    print_colored("Blog Post Generator", Colors.BOLD)
    print_colored("=" * 20, Colors.BLUE)
    
    # Get post type
    post_type = get_post_type()
    
    # Get available projects (only needed for research notes)
    available_projects = get_available_projects() if post_type == "research_note" else []
    
    # Get title
    title = get_user_input("Enter post title")
    
    # Get project (only for research notes)
    project_name = select_project_interactive(available_projects, post_type)
    
    # Get description
    description = get_user_input("Enter brief description")
    
    # Get tags and categories
    print_colored("\\nTags and Categories:", Colors.BLUE)
    tags = get_tags(post_type)
    categories = get_categories(post_type)
    
    # Featured flag
    featured_input = get_user_input("Mark as featured? (y/n)", default="n", required=False)
    featured = featured_input.lower() in ['y', 'yes']
    
    # Summary
    print_colored("\\nSummary:", Colors.BLUE)
    post_type_display = "Research Note" if post_type == "research_note" else "Blog Post"
    print(f"Type: {post_type_display}")
    print(f"Title: {title}")
    if project_name:
        print(f"Project: {project_name}")
    print(f"Description: {description}")
    print(f"Tags: {', '.join(tags)}")
    print(f"Categories: {', '.join(categories)}")
    print(f"Featured: {featured}")
    
    # Confirm
    confirm = get_user_input("\\nCreate this post? (y/n)", default="y")
    if confirm.lower() != 'y':
        print("Cancelled.")
        sys.exit(0)
    
    # Create the file
    filename = create_blog_post(title, description, tags, categories, post_type, project_name, featured)
    
    if filename:
        print_colored("\\nNext steps:", Colors.BLUE)
        print(f"1. Edit content: code {filename}")
        print("2. Build site: bundle exec jekyll serve")
        print("3. View at: http://localhost:4000/blog/")
        if post_type == "research_note":
            print("4. Filter research notes: http://localhost:4000/blog/tag/research-note/")

if __name__ == "__main__":
    main()
