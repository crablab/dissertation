pandoc --filter pandoc-citeproc -B title.md declaration.md interim.md -H preamble.tex --variable classoption=twocolumn --bibliography=interim.bib --output interim.md.pdf
