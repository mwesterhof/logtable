PRECISION = 3
DIGITS = 5
PER_PAGE = 50

all: table.pdf

table.pdf: table.tex
	pdflatex table.tex

table.tex: log_template.tex *.py Makefile
	python generate.py ${PRECISION} ${DIGITS} ${PER_PAGE} table.tex

clean:
	-rm table.*

watch:
	ag -l |entr make

export: table.pdf
	cp table.pdf exported.pdf
