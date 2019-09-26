pandoc --filter pandoc-citeproc -B title.md project_plan.md -H preamble.tex --variable classoption=twocolumn --csl=ieee.csl --bibliography=project_plan.bib --output project_plan.md.pdf
