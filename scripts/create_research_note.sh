#!/bin/bash

# Research Notes Generator Script
# Usage: ./create_research_note.sh "Note Title" "Project Name" [description]

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to show usage
show_usage() {
    echo -e "${BLUE}Usage:${NC}"
    echo "  $0 \"Note Title\" \"Project Name\" [\"Description\"]"
    echo ""
    echo -e "${BLUE}Examples:${NC}"
    echo "  $0 \"Force Field Validation\" \"Modelling Gold Stress Strain Curves in LAMMPS\""
    echo "  $0 \"Coupling Efficiency Tests\" \"Designing a Silicon Nitride Waveguide\" \"Testing fiber coupling methods\""
    echo ""
    echo -e "${BLUE}Available Projects:${NC}"
    
    # List available projects
    if [ -d "_projects" ]; then
        for project_file in _projects/*.md; do
            if [ -f "$project_file" ]; then
                project_title=$(grep "^title:" "$project_file" | sed 's/title: //' | tr -d '"')
                echo "  - $project_title"
            fi
        done
    fi
}

# Function to create slug from title
create_slug() {
    echo "$1" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-\|-$//g'
}

# Function to prompt for tags
get_tags() {
    echo -e "${YELLOW}Enter tags (comma-separated):${NC}"
    read -r tags_input
    
    # Convert comma-separated tags to YAML array format
    if [ -n "$tags_input" ]; then
        # Split by comma, trim whitespace, and format as YAML array
        echo "$tags_input" | sed 's/,/\n/g' | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//' | sed 's/^/  - /' | tr '\n' '\0' | sed 's/\x0$//' | sed 's/\x0/\n/g'
    else
        echo "  - research"
    fi
}

# Function to prompt for categories
get_categories() {
    echo -e "${YELLOW}Enter categories (comma-separated):${NC}"
    echo "Common categories: simulation, experiment, analysis, literature-review, methodology, results"
    read -r categories_input
    
    # Convert comma-separated categories to YAML array format
    if [ -n "$categories_input" ]; then
        echo "$categories_input" | sed 's/,/\n/g' | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//' | sed 's/^/  - /' | tr '\n' '\0' | sed 's/\x0$//' | sed 's/\x0/\n/g'
    else
        echo "  - research"
    fi
}

# Check if we're in the right directory
if [ ! -f "_config.yml" ]; then
    echo -e "${RED}Error: Not in Jekyll site root directory${NC}"
    echo "Please run this script from the root of your Jekyll site."
    exit 1
fi

# Check arguments
if [ $# -lt 2 ]; then
    echo -e "${RED}Error: Missing required arguments${NC}"
    echo ""
    show_usage
    exit 1
fi

# Get arguments
note_title="$1"
project_name="$2"
description="$3"

# Create slug and filename
slug=$(create_slug "$note_title")
date=$(date +%Y-%m-%d)
filename="_research_notes/${date}-${slug}.md"

# Check if file already exists
if [ -f "$filename" ]; then
    echo -e "${RED}Error: File $filename already exists${NC}"
    exit 1
fi

# Verify project exists
project_found=false
if [ -d "_projects" ]; then
    for project_file in _projects/*.md; do
        if [ -f "$project_file" ]; then
            project_title=$(grep "^title:" "$project_file" | sed 's/title: //' | tr -d '"')
            if [ "$project_title" = "$project_name" ]; then
                project_found=true
                break
            fi
        fi
    done
fi

if [ "$project_found" = false ]; then
    echo -e "${YELLOW}Warning: Project '$project_name' not found in _projects directory${NC}"
    echo "Continue anyway? (y/n)"
    read -r continue_choice
    if [ "$continue_choice" != "y" ] && [ "$continue_choice" != "Y" ]; then
        exit 1
    fi
fi

# Prompt for description if not provided
if [ -z "$description" ]; then
    echo -e "${YELLOW}Enter a brief description:${NC}"
    read -r description
fi

# Get tags and categories interactively
echo ""
tags=$(get_tags)
echo ""
categories=$(get_categories)

# Ask if this should be featured
echo ""
echo -e "${YELLOW}Should this be a featured note? (y/n):${NC}"
read -r featured_choice
if [ "$featured_choice" = "y" ] || [ "$featured_choice" = "Y" ]; then
    featured="true"
else
    featured="false"
fi

# Create the research note file
cat > "$filename" << EOF
---
layout: research_note
title: "$note_title"
date: $date
description: "$description"
tags:
$tags
categories:
$categories
related_project: "$project_name"
featured: $featured
---

## Overview

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
EOF

echo -e "${GREEN}✓ Research note created successfully:${NC} $filename"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "1. Edit the content in: $filename"
echo "2. Build and serve the site: bundle exec jekyll serve"
echo "3. View at: http://localhost:4000/research-notes/"
echo ""
echo -e "${BLUE}Quick edit:${NC} code $filename"
