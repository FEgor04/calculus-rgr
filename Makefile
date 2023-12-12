all: main.pdf

main.pdf: main.tex figures/vec_lines.pdf
	latexmk -pdf main.tex

.PHONY: main.pdf 

figures/%.pdf: src/python/%.py
	source venv/bin/activate; python3 $< --save $@
