pandoc --toc --filter pandoc-xnos --filter pandoc-citeproc -B title.md -B declaration.md final_report.md appendix.md -H preamble.tex --bibliography=final_report.bib --output final_report.md.pdf
