pandoc --toc --filter pandoc-xnos --filter pandoc-citeproc --csl assets/ieee.csl -B title.md -B declaration.md final_report.md appendix.md user_guide.md -H preamble.tex -V geometry:margin=1in --bibliography=final_report.bib --output final_report.md.pdf
