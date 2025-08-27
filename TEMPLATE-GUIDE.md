# Using OCEAN as a Template

This directory contains the template system for creating new genomic data platforms based on the OCEAN architecture.

## Quick Start for New Projects

### 1. Copy and Configure

```bash
# Copy the template configuration
cp template-config.yml my-species-config.yml

# Edit the configuration for your species
vim my-species-config.yml
```

### 2. Key Configuration Sections

#### Project Information
```yaml
project:
  name: "YourProject"  # Short name, used in code
  full_name: "Your Species Genomics Platform"  # Display name
  description: "Brief description of your platform"
```

#### Species Information
```yaml
species:
  scientific_name: "Genus species"
  common_name: "common name"
  description: "the [adjective] [common name]"  # Used in sentences
  emoji: "🧬"  # Optional branding emoji
```

#### Data Sources
Update all URLs to point to your data:
```yaml
data_sources:
  nr_blast: "https://your-server.com/blast-results.csv"
  uniprot: "https://your-server.com/uniprot-annotations.txt" 
  pathways: "https://your-server.com/pathway-data.csv"
  gene_gff: "https://your-server.com/gene-annotations.gff3"
```

#### JBrowse Configuration
```yaml
jbrowse:
  assemblies:
    - name: "Your Assembly v1.0"
      fasta_url: "https://your-server.com/genome.fasta"
      fai_url: "https://your-server.com/genome.fasta.fai"
```

### 3. Generate Your Site

```bash
# Install Python dependencies
pip install pyyaml jinja2

# Generate your project files
python setup-template.py my-species-config.yml

# Copy your genome data files
mkdir -p docs/jbrowse/data/v1/
cp your-genome-files/* docs/jbrowse/data/v1/

# Copy your images
cp your-logo.png quarto/img/
```

### 4. Build and Test

```bash
cd quarto
quarto preview  # Test locally
quarto render   # Build for deployment
```

## Template Customization

### Adding New Data Sections

1. Add data sources to your config:
```yaml
data_sources:
  new_data_type: "https://your-server.com/new-data.csv"
```

2. Modify `templates/explore.qmd.template` to add R code for your new data.

3. Regenerate with `python setup-template.py your-config.yml`

### Customizing Population/Study Information

The template includes a flexible population information section:

```yaml
population_info:
  enabled: true  # Set to false to hide completely
  title: "Population Information"  # Customize section title
  description: "Your study description"
  
  # Optional map
  map_embed: "Google Maps embed URL"
  
  # Customizable location table
  locations:
    - name: "Site 1"
      salinity: "High"
      freshwater_input: "Low"
      tidal_exchange: "High" 
      human_influence: "Low"
```

You can:
- Change column names by editing the template
- Add/remove columns as needed
- Disable the entire section with `enabled: false`

### JBrowse Tracks

The template creates basic gene, ncRNA, and repeat tracks. To add more:

1. Add track data sources to your config
2. Edit `templates/jbrowse-config.json.template` 
3. Add new track definitions following JBrowse v3 syntax

### Styling and Branding

- Update `quarto/styles.css` for custom CSS
- Replace `quarto/img/` files with your logos/images
- Modify the celebration message and platform features in your config

## Example Configurations

See the `examples/` directory for:
- `arabidopsis-config.yml` - Plant genomics example
- Additional species examples (add your own!)

## File Structure After Setup

```
your-project/
├── template-config.yml          # Original template config
├── my-species-config.yml        # Your customized config
├── setup-template.py           # Template processor
├── templates/                  # Template source files
├── quarto/                     # Generated Quarto source
│   ├── index.qmd               # Homepage
│   ├── about.qmd               # About page with species info
│   ├── explore.qmd             # Data exploration page
│   ├── browse.qmd              # Genome browser page
│   └── _quarto.yml             # Quarto configuration
└── docs/                       # Generated website
    ├── index.html
    ├── jbrowse/
    │   ├── config.json         # JBrowse configuration
    │   └── data/               # Your genome data files
    └── ...
```

## Tips for Success

1. **Start Small**: Begin with basic gene and assembly data, add complexity later
2. **Test Early**: Use `quarto preview` to test changes immediately  
3. **Version Control**: Commit your config files and generated templates
4. **Document Changes**: Keep notes on customizations for future reference
5. **Community**: Share your configurations as examples for others

## Troubleshooting

### Common Issues

1. **Missing Dependencies**: Install Quarto, R packages, and Python modules
2. **Data URLs**: Ensure all data sources are publicly accessible
3. **File Paths**: Use absolute URLs for external data, relative paths for local files
4. **JBrowse Data**: Ensure FASTA files have corresponding .fai index files

### Getting Help

- Check the main README.md for general setup instructions
- Review example configurations in `examples/`
- Submit issues with the `template` label for template-specific problems