FIGURES_DIR := figures
FIGURES_SRC_DIR := src/python

FIGURES_SRC = $(wildcard $(FIGURES_SRC_DIR)/*_plot.py)
FIGURES_ARTIFACTS := $(FIGURES_SRC:$(FIGURES_SRC_DIR)/%.py=$(FIGURES_DIR)/%.pdf)

.PHONY: main.pdf clean

all: main.pdf

main.pdf: main.tex $(FIGURES_ARTIFACTS)
	latexmk -pdf main.tex

figures/%.pdf: src/python/%.py $(FIGURES_DIR)
	source venv/bin/activate; python3 $< --save $@

clean:
	rm -rf $(FIGURES_DIR) main.pdf
	latexmk -C main.tex

$(FIGURES_DIR):
	mkdir $@
