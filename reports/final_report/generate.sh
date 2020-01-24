pandoc --filter pandoc-citeproc -B title.md project_plan.md gantt.tex -H preamble.tex --variable classoption=twocolumn --bibliography=project_plan.bib --output project_plan.md.pdf
