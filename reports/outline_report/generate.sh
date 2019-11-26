pandoc --filter pandoc-xnos --filter pandoc-citeproc report.md -H preamble.tex --variable classoption=article --bibliography=report.bib --output report.md.pdf 
