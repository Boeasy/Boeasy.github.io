#!/bin/bash

# Blog Post Generator Script
# Usage: ./create_blog_post.sh "Post Title" [type] [project] [description]

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to show usage
show_usage() {
    echo -e "${BLUE}Usage:${NC}"
    echo "  $0 \"Post Title\" [type] [\"Project Name\"] [\"Description\"]"
    echo ""
    echo -e "${BLUE}Types:${NC}"
    echo "  research-note - A research note (default)"
    echo "  blog-post     - A regular blog post"
    echo ""
    echo -e "${BLUE}Examples:${NC}"
    echo "  $0 \"Force Field Validation\" research-note \"Modelling Gold Stress Strain Curves in LAMMPS\""
    echo "  $0 \"My Thoughts on Jekyll\" blog-post \"\" \"Personal reflections on using Jekyll\""
    echo "  $0 \"Coupling Efficiency Tests\" research-note \"Designing a Silicon Nitride Waveguide\" \"Testing fiber coupling methods\""
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
    local post_type="$1"
    
    if [ "$post_type" = "research-note" ]; then
        echo -e "${YELLOW}Enter tags (comma-separated, will include 'research-note' automatically):${NC}"
        echo -e "${BLUE}Suggestions: simulation, analysis, molecular-dynamics, waveguide${NC}"
    else
        echo -e "${YELLOW}Enter tags (comma-separated):${NC}"
        echo -e "${BLUE}Suggestions: technology, personal, tutorial, update${NC}"
    fi
    
    read -r tags_input
    
    # Convert comma-separated tags to YAML array format
    if [ -n "$tags_input" ]; then
        # For research notes, ensure research-note tag is included
        if [ "$post_type" = "research-note" ]; then
            if [[ "$tags_input" != *"research-note"* ]]; then
                tags_input="research-note, $tags_input"
            fi
        fi
        
        # Split by comma, trim whitespace, and format as YAML array
        echo "$tags_input" | sed 's/,/\n/g' | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//' | sed 's/^/  - /' | tr '\n' '\0' | sed 's/\x0$//' | sed 's/\x0/\n/g'
    else
        if [ "$post_type" = "research-note" ]; then
            echo "  - research-note"
        else
            echo "  - blog"
        fi
    fi
}

# Function to prompt for categories
get_categories() {
    local post_type="$1"
    
    if [ "$post_type" = "research-note" ]; then
        echo -e "${YELLOW}Enter categories (comma-separated):${NC}"
        echo -e "${BLUE}Common research categories: simulation, experiment, analysis, literature-review, methodology, results${NC}"
    else
        echo -e "${YELLOW}Enter categories (comma-separated):${NC}"
        echo -e "${BLUE}Common blog categories: technology, personal, tutorial, project${NC}"
    fi
    
    read -r categories_input
    
    # Convert comma-separated categories to YAML array format
    if [ -n "$categories_input" ]; then
        echo "$categories_input" | sed 's/,/\n/g' | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//' | sed 's/^/  - /' | tr '\n' '\0' | sed 's/\x0$//' | sed 's/\x0/\n/g'
    else
        if [ "$post_type" = "research-note" ]; then
            echo "  - research"
        else
            echo "  - blog"
        fi
    fi
}

# Function to get template content
get_template_content() {
    local post_type="$1"
    
    if [ "$post_type" = "research-note" ]; then
        cat << 'EOF'

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
EOF
    else
        cat << 'EOF'

Write your blog post content here...

## Introduction

Start with an engaging introduction.

## Main Content

Add your main content sections here.

## Conclusion

Wrap up your thoughts.
EOF
    fi
}

# Check if we're in the right directory
if [ ! -f "_config.yml" ]; then
    echo -e "${RED}Error: Not in Jekyll site root directory${NC}"
    echo "Please run this script from the root of your Jekyll site."
    exit 1
fi

# Check arguments
if [ $# -lt 1 ]; then
    show_usage
    exit 1
fi

# Parse arguments
TITLE="$1"
POST_TYPE="${2:-research-note}"
PROJECT_NAME="$3"
DESCRIPTION="$4"

# Validate post type
if [ "$POST_TYPE" != "research-note" ] && [ "$POST_TYPE" != "blog-post" ]; then
    echo -e "${RED}Error: Post type must be 'research-note' or 'blog-post'${NC}"
    exit 1
fi

# Create slug and filename
SLUG=$(create_slug "$TITLE")
DATE=$(date +%Y-%m-%d)
FILENAME="_posts/${DATE}-${SLUG}.md"

# Check if file already exists
if [ -f "$FILENAME" ]; then
    echo -e "${RED}Error: File $FILENAME already exists${NC}"
    exit 1
fi

# Create _posts directory if it doesn't exist
mkdir -p "_posts"

# Get description if not provided
if [ -z "$DESCRIPTION" ]; then
    echo -e "${YELLOW}Enter a brief description:${NC}"
    read -r DESCRIPTION
fi

# Get tags and categories interactively
echo ""
TAGS=$(get_tags "$POST_TYPE")
echo ""
CATEGORIES=$(get_categories "$POST_TYPE")

# Create the file
echo -e "${BLUE}Creating blog post: $FILENAME${NC}"

# Write front matter
cat > "$FILENAME" << EOF
---
layout: post
title: "$TITLE"
date: $DATE
description: "$DESCRIPTION"
tags:
$TAGS
categories:
$CATEGORIES
EOF

# Add project field only for research notes
if [ "$POST_TYPE" = "research-note" ] && [ -n "$PROJECT_NAME" ]; then
    echo "related_project: \"$PROJECT_NAME\"" >> "$FILENAME"
fi

# Close front matter
echo "featured: false" >> "$FILENAME"
echo "---" >> "$FILENAME"

# Add template content
get_template_content "$POST_TYPE" >> "$FILENAME"

echo -e "${GREEN}✓ Blog post created successfully: $FILENAME${NC}"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "1. Edit content: code $FILENAME"
echo "2. Build site: bundle exec jekyll serve"
echo "3. View at: http://localhost:4000/blog/"
if [ "$POST_TYPE" = "research-note" ]; then
    echo "4. Filter research notes: http://localhost:4000/blog/tag/research-note/"
fi
