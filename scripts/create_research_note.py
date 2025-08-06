#!/usr/bin/env python3
"""
Research Notes Generator for Jekyll Site
Creates research note files with proper front matter and template content.

Usage:
    python3 scripts/create_research_note.py
    python3 scripts/create_research_note.py --title "Note Title" --project "Project Name"
"""

import os
import sys
import argparse
import re
from datetime import datetime
from pathlib import Path
import yaml

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
                # Extract front matter
                if content.startswith('---'):
                    front_matter_end = content.find('---', 3)
                    if front_matter_end != -1:
                        front_matter = content[3:front_matter_end]
                        data = yaml.safe_load(front_matter)
                        if 'title' in data:
                            projects.append(data['title'])
        except Exception as e:
            print_colored(f"Warning: Could not read {project_file}: {e}", Colors.YELLOW)
    
    return sorted(projects)

def validate_project(project_name, available_projects):
    """Check if project exists and offer suggestions"""
    if project_name in available_projects:
        return True
    
    print_colored(f"Project '{project_name}' not found.", Colors.YELLOW)
    
    if available_projects:
        print_colored("Available projects:", Colors.BLUE)
        for i, project in enumerate(available_projects, 1):
            print(f"  {i}. {project}")
        
        # Offer fuzzy matching
        close_matches = [p for p in available_projects if project_name.lower() in p.lower()]
        if close_matches:
            print_colored("\nDid you mean:", Colors.YELLOW)
            for match in close_matches:
                print(f"  - {match}")
    
    return False

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

def get_tags():
    """Get tags from user input"""
    tags_input = get_user_input(
        "Enter tags (comma-separated, e.g., 'simulation, analysis, molecular-dynamics')",
        default="research",
        required=False
    )
    
    if not tags_input:
        return ["research"]
    
    # Split by comma and clean up
    tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
    return tags

def get_categories():
    """Get categories from user input"""
    print_colored("\nCommon categories: simulation, experiment, analysis, literature-review, methodology, results", Colors.BLUE)
    
    categories_input = get_user_input(
        "Enter categories (comma-separated)",
        default="research",
        required=False
    )
    
    if not categories_input:
        return ["research"]
    
    # Split by comma and clean up
    categories = [cat.strip() for cat in categories_input.split(',') if cat.strip()]
    return categories

def select_project_interactive(available_projects):
    """Interactive project selection"""
    if not available_projects:
        return get_user_input("Enter project name")
    
    print_colored("\nAvailable projects:", Colors.BLUE)
    for i, project in enumerate(available_projects, 1):
        print(f"  {i}. {project}")
    
    print(f"  {len(available_projects) + 1}. Enter custom project name")
    
    while True:
        choice = input(f"\nSelect project (1-{len(available_projects) + 1}): ").strip()
        
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(available_projects):
                return available_projects[choice_num - 1]
            elif choice_num == len(available_projects) + 1:
                return get_user_input("Enter project name")
            else:
                print_colored(f"Please enter a number between 1 and {len(available_projects) + 1}", Colors.RED)
        except ValueError:
            print_colored("Please enter a valid number", Colors.RED)

def create_research_note(title, project_name, description, tags, categories, featured=False):
    """Create the research note file"""
    # Create filename
    slug = create_slug(title)
    date = datetime.now().strftime('%Y-%m-%d')
    filename = f"_research_notes/{date}-{slug}.md"
    
    # Check if file exists
    if os.path.exists(filename):
        print_colored(f"Error: File {filename} already exists", Colors.RED)
        return None
    
    # Create directory if it doesn't exist
    os.makedirs("_research_notes", exist_ok=True)
    
    # Create front matter
    front_matter = {
        'layout': 'research_note',
        'title': title,
        'date': date,
        'description': description,
        'tags': tags,
        'categories': categories,
        'related_project': project_name,
        'featured': featured
    }
    
    # Template content
    content = """## Overview

Brief overview of what this note covers.

## Methodology

Describe the methods or approach used.

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
    
    # Write file
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("---\n")
            yaml.dump(front_matter, f, default_flow_style=False, allow_unicode=True)
            f.write("---\n\n")
            f.write(content)
        
        print_colored(f"✓ Research note created successfully: {filename}", Colors.GREEN)
        return filename
    
    except Exception as e:
        print_colored(f"Error creating file: {e}", Colors.RED)
        return None

def main():
    parser = argparse.ArgumentParser(description='Create a new research note')
    parser.add_argument('--title', '-t', help='Note title')
    parser.add_argument('--project', '-p', help='Related project name')
    parser.add_argument('--description', '-d', help='Note description')
    parser.add_argument('--featured', '-f', action='store_true', help='Mark as featured')
    parser.add_argument('--interactive', '-i', action='store_true', default=True, help='Interactive mode (default)')
    
    args = parser.parse_args()
    
    # Check if we're in the right directory
    if not os.path.exists('_config.yml'):
        print_colored("Error: Not in Jekyll site root directory", Colors.RED)
        print("Please run this script from the root of your Jekyll site.")
        sys.exit(1)
    
    print_colored("Research Notes Generator", Colors.BOLD)
    print_colored("=" * 25, Colors.BLUE)
    
    # Get available projects
    available_projects = get_available_projects()
    
    # Get title
    if args.title:
        title = args.title
    else:
        title = get_user_input("Enter note title")
    
    # Get project
    if args.project:
        project_name = args.project
        if not validate_project(project_name, available_projects):
            proceed = get_user_input("Continue with this project name? (y/n)", default="y")
            if proceed.lower() != 'y':
                sys.exit(1)
    else:
        project_name = select_project_interactive(available_projects)
    
    # Get description
    if args.description:
        description = args.description
    else:
        description = get_user_input("Enter brief description")
    
    # Get tags and categories (always interactive for now)
    print_colored("\nTags and Categories:", Colors.BLUE)
    tags = get_tags()
    categories = get_categories()
    
    # Featured flag
    if not args.featured:
        featured_input = get_user_input("Mark as featured? (y/n)", default="n", required=False)
        featured = featured_input.lower() in ['y', 'yes']
    else:
        featured = args.featured
    
    # Summary
    print_colored("\nSummary:", Colors.BLUE)
    print(f"Title: {title}")
    print(f"Project: {project_name}")
    print(f"Description: {description}")
    print(f"Tags: {', '.join(tags)}")
    print(f"Categories: {', '.join(categories)}")
    print(f"Featured: {featured}")
    
    # Confirm
    confirm = get_user_input("\nCreate this research note? (y/n)", default="y")
    if confirm.lower() != 'y':
        print("Cancelled.")
        sys.exit(0)
    
    # Create the file
    filename = create_research_note(title, project_name, description, tags, categories, featured)
    
    if filename:
        print_colored("\nNext steps:", Colors.BLUE)
        print(f"1. Edit content: code {filename}")
        print("2. Build site: bundle exec jekyll serve")
        print("3. View at: http://localhost:4000/research-notes/")

if __name__ == "__main__":
    main()
