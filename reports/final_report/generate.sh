pandoc --filter pandoc-citeproc -B title.md final_report.md appendix.md -H preamble.tex --variable classoption=twocolumn --bibliography=final_report.bib --output final_report.md.pdf
