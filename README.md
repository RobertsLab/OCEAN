# Genomic Data Platform Template

This repository serves as a template for creating integrated genomic data platforms with built-in genome browsers. It was originally developed for *Ostrea chilensis* (Chilean flat oyster) research but has been generalized for use with any species.

## Features

- 🧬 **Integrated Genome Browser**: Built-in JBrowse genome browser for interactive genomic data exploration
- 📊 **Interactive Data Tables**: R-powered tables for annotations, BLAST results, and pathway data  
- 🎨 **Responsive Web Interface**: Clean, modern website built with Quarto
- 🔧 **Easy Customization**: Template-driven configuration system
- 📱 **Mobile Friendly**: Works on desktop and mobile devices
- 🌐 **GitHub Pages Ready**: Easy deployment to GitHub Pages

## Technology Stack

- **[Quarto](https://quarto.org/)**: Website generation and R integration
- **[JBrowse](https://jbrowse.org/)**: Genome browser component
- **R**: Data analysis and interactive tables
- **YAML**: Configuration management

## Quick Start

### 1. Prerequisites

- [Quarto](https://quarto.org/docs/get-started/) (>= 1.0)
- [R](https://www.r-project.org/) (>= 4.0) with packages:
  - `tidyverse`
  - `DT` 
  - `readxl`
  - `plotly`
- Python (>= 3.6) with `pyyaml` and `jinja2`

### 2. Setup Your Project

1. **Fork or clone this repository**
   ```bash
   git clone https://github.com/RobertsLab/OCEAN.git
   cd OCEAN
   ```

2. **Install Python dependencies**
   ```bash
   pip install pyyaml jinja2
   ```

3. **Configure your project**
   
   Copy and edit the configuration file:
   ```bash
   cp template-config.yml my-project-config.yml
   ```
   
   Edit `my-project-config.yml` with your species and project information:
   ```yaml
   # Project Information
   project:
     name: "MyGenome"
     full_name: "My Species Genome Project"
     description: "An integrated platform for my species research"
   
   # Species Information  
   species:
     scientific_name: "Species scientificus"
     common_name: "common species name"
     description: "the common species"
     emoji: "🧬"
   
   # Update data sources with your URLs
   data_sources:
     nr_blast: "https://example.com/path/to/nr.csv"
     uniprot: "https://example.com/path/to/uniprot.txt"
     # ... etc
   ```

4. **Generate your project files**
   ```bash
   python setup-template.py my-project-config.yml
   ```

5. **Add your genomic data**
   
   Place your genome files in the appropriate directories:
   ```
   docs/jbrowse/data/
   ├── v1/
   │   ├── your-genome.fasta
   │   ├── your-genome.fasta.fai
   │   ├── genes.gff3
   │   └── annotations/
   └── tracks/
   ```

6. **Build and preview**
   ```bash
   cd quarto
   quarto preview
   ```

### 3. Customize Further

#### Website Styling
- Edit `quarto/styles.css` for custom styling
- Modify `quarto/_quarto.yml` for navigation and theme changes

#### Genome Browser
- Update JBrowse configuration in `docs/jbrowse/config.json`
- Add track data to `docs/jbrowse/data/`
- Configure assemblies, annotations, and quantitative tracks

#### Data Sources
- Update URLs in your config file to point to your data
- Modify R code in `explore.qmd` template for custom analysis

## Configuration Reference

### Project Settings
```yaml
project:
  name: "ProjectName"           # Short identifier
  full_name: "Full Project Name" # Display name
  description: "Project description"
```

### Species Information
```yaml
species:
  scientific_name: "Genus species"
  common_name: "common name"
  description: "descriptive text"
  emoji: "🧬"  # Optional branding emoji
```

### Data Sources
All data source URLs can be customized:
```yaml
data_sources:
  nr_blast: "URL to BLAST results CSV"
  uniprot: "URL to UniProt annotations"
  pathways: "URL to pathway data"
  gene_gff: "URL to gene annotations GFF"
```

### Population/Study Data
The template includes optional population study components:
```yaml
population_info:
  enabled: true  # Set to false to hide this section
  title: "Population Information"
  description: "Study description"
  map_embed: "Google Maps embed URL"
  locations:
    - name: "Site 1"
      salinity: "High"
      # ... other characteristics
```

### JBrowse Configuration
Define genome assemblies and basic tracks:
```yaml
jbrowse:
  version: "v3.6.4"
  assemblies:
    - name: "Assembly Name"
      fasta_url: "URL to FASTA file"
      fai_url: "URL to FASTA index"
```

## Directory Structure

```
your-project/
├── template-config.yml          # Main configuration
├── setup-template.py           # Template processor
├── templates/                  # Template files
│   ├── index.qmd.template
│   ├── about.qmd.template
│   ├── explore.qmd.template
│   ├── _quarto.yml.template
│   └── jbrowse-config.json.template
├── quarto/                     # Generated Quarto source
│   ├── index.qmd
│   ├── about.qmd
│   ├── explore.qmd
│   ├── _quarto.yml
│   ├── img/
│   └── styles.css
└── docs/                       # Generated website
    ├── index.html
    ├── about.html
    ├── jbrowse/
    │   ├── config.json
    │   ├── data/
    │   └── index.html
    └── ...
```

## Deployment

### GitHub Pages
1. Push your repository to GitHub
2. Enable GitHub Pages in repository settings
3. Set source to `/docs` folder
4. Your site will be available at `https://username.github.io/repository-name`

### Manual Deployment
Build the site and deploy the `docs/` folder to any web server:
```bash
cd quarto
quarto render
# Upload docs/ folder to your web server
```

## Examples

See the original OCEAN project configuration for a complete example of a working genomic data platform.

## Contributing

Feel free to submit issues and enhancement requests! This template is designed to be flexible and extensible.

## License

This template is provided under the same license as the original OCEAN project.

## Citation

If you use this template for your research, please cite the original OCEAN project and any relevant publications.

---

**Need help?** Check the [Issues](https://github.com/RobertsLab/OCEAN/issues) page or submit a new issue with the `template` label.