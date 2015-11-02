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

publications:
	python publi.py --english
	latexmk -f -pdf publi_EN
	python publi.py --francais
	latexmk -f -pdf publi_FR

contributions:
	python publi.py --english --software
	latexmk -f -pdf publi_EN
	mv publi_EN.pdf contributions_EN.pdf
	python publi.py --francais --software
	latexmk -f -pdf publi_FR
	mv publi_FR.pdf contributions_FR.pdf

show:
	open publi_EN.pdf
	open publi_FR.pdf
	open contributions_EN.pdf
	open contributions_FR.pdf

all: clean contributions publications show
