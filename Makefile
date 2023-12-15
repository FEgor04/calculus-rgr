FIGURES_DIR := figures
FIGURES_SRC_DIR := src/python

AUX_DIR := aux

DEP_FILE := .deps.d

LATEXMK_FLAGS := -pdf -pdflatex="pdflatex -interaction=nonstopmode" \
								 -use-make -auxdir=$(AUX_DIR) 											\
								 -M -MF $(DEP_FILE)

.PHONY: clean format

all: main.pdf

main.pdf: main.tex $(AUX_DIR) $(FIGURES_DIR)
	latexmk $(LATEXMK_FLAGS) $<

figures/%.pdf: src/python/%.py | $(FIGURES_DIR)
	source venv/bin/activate; python3 $< --save $@

clean:
	rm -rf $(FIGURES_DIR) $(AUX_DIR) $(DEP_FILE) main.pdf **/*.bak*
	latexmk -C main.tex

format:
	latexindent **/*.tex -w

$(FIGURES_DIR) $(AUX_DIR):
	mkdir $@

$(DEP_FILE):
	touch $@

-include $(DEP_FILE)
