#!/usr/bin/env python3
"""
Template processor for genomic data platform
Generates project files from templates and configuration
"""

import yaml
import json
import os
import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, Template

def load_config(config_path):
    """Load YAML configuration file"""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def process_template(template_path, output_path, config):
    """Process a single template file"""
    env = Environment(loader=FileSystemLoader(Path(template_path).parent))
    template = env.get_template(Path(template_path).name)
    
    # Render the template
    rendered = template.render(**config)
    
    # Write to output file
    with open(output_path, 'w') as f:
        f.write(rendered)
    
    print(f"Generated: {output_path}")

def setup_project(config_path):
    """Set up a new project from templates"""
    # Load configuration
    config = load_config(config_path)
    
    # Create directories
    quarto_dir = Path("quarto")
    docs_dir = Path("docs") 
    jbrowse_dir = docs_dir / "jbrowse"
    
    quarto_dir.mkdir(exist_ok=True)
    jbrowse_dir.mkdir(parents=True, exist_ok=True)
    
    # Template mappings: (template_file, output_file)
    templates = [
        ("templates/index.qmd.template", "quarto/index.qmd"),
        ("templates/about.qmd.template", "quarto/about.qmd"), 
        ("templates/explore.qmd.template", "quarto/explore.qmd"),
        ("templates/browse.qmd.template", "quarto/browse.qmd"),
        ("templates/_quarto.yml.template", "quarto/_quarto.yml"),
        ("templates/jbrowse-config.json.template", "docs/jbrowse/config.json")
    ]
    
    # Process each template
    for template_file, output_file in templates:
        if Path(template_file).exists():
            process_template(template_file, output_file, config)
        else:
            print(f"Warning: Template {template_file} not found")
    
    print(f"\nProject setup complete! Website title: {config['website']['title']}")
    print(f"Species: {config['species']['scientific_name']}")
    print("\nNext steps:")
    print("1. Update your data sources in template-config.yml")
    print("2. Add your genome data files to docs/jbrowse/data/")
    print("3. Build the website with: quarto render quarto/")

def main():
    if len(sys.argv) != 2:
        print("Usage: python setup-template.py <config-file>")
        print("Example: python setup-template.py template-config.yml")
        sys.exit(1)
    
    config_file = sys.argv[1]
    if not Path(config_file).exists():
        print(f"Error: Config file {config_file} not found")
        sys.exit(1)
    
    setup_project(config_file)

if __name__ == "__main__":
    main()