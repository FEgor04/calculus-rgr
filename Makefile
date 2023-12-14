FIGURES_DIR := figures
FIGURES_SRC_DIR := src/python

AUX_DIR := aux

LATEXMK_FLAGS := -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make -auxdir=$(AUX_DIR)

.PHONY: clean

all: main.pdf

main.pdf: main.tex $(AUX_DIR) $(FIGURES_DIR)
	latexmk $(LATEXMK_FLAGS) $<

figures/%.pdf: src/python/%.py | $(FIGURES_DIR)
	source venv/bin/activate; python3 $< --save $@

clean:
	rm -rf $(FIGURES_DIR) $(AUX_DIR) main.pdf
	latexmk -C main.tex

$(FIGURES_DIR) $(AUX_DIR):
	mkdir $@

