pandoc --filter pandoc-xnos --filter pandoc-citeproc report.md -H preamble.tex --variable classoption=twocolumn --bibliography=report.bib --output report.md.pdf 
