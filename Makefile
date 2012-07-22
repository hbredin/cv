pdf:
	pdflatex CV_EN_short.tex
	pdflatex CV_FR_short.tex

show:
	open CV_EN_short.pdf
	open CV_FR_short.pdf
	
all: pdf show

