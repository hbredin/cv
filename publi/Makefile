clean:
	rm -f publi_*.tex
	rm -f *.aux
	rm -f *.bbl
	rm -f *.blg
	rm -f *.dvi
	rm -f *.pdf
	rm -f *.log
	rm -f *.pyc
	rm -f *fdb_latexmk

pdf:
	python publi.py --english
	latexmk -f -pdf publi_EN
	python publi.py --francais
	latexmk -f -pdf publi_FR

show:
	open publi_EN.pdf
	open publi_FR.pdf
	
all: clean pdf show
	

