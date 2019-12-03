pandoc --filter pandoc-xnos --filter pandoc-citeproc -B title.md report.md -H preamble.tex --variable classoption=twocolumn --bibliography=report.bib --output report.md.pdf
