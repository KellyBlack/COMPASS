

# Files to be created:
FILE = experimental
DVIFILE = $(FILE).dvi
TEXFILE = $(DVIFILE:.dvi=.tex)
BIBFILE = $(DVIFILE:.dvi=.bbl)
PDFFILE = $(DVIFILE:.dvi=.pdf)
DEPENDS = 

# /usr/include/make/commondefs and /usr/include/make/commonrules
# define some useful Makefile rules.  For example, they
# defines a 'clean' target, so you can type 'make clean'
# to remove all .o files (or other files generated during
# compilation). See the file /usr/include/make/commonrules for
# documentation on what targets are supported.

# include /usr/include/make/commondefs

TARGETS=$(DVIFILE)
LATEX=latex
BIBTEX=bibtex
PDFLATEX=pdflatex

.SUFFIXES: .tex .bbl


.tex.dvi:
	$(LATEX) $*

.tex.bbl:
	$(LATEX) $*
	$(BIBTEX) $*
	$(LATEX) $*

.bbl:
	$(LATEX) $*
	$(BIBTEX) $*
	$(LATEX) $*



default: $(DVIFILE)

# include $(COMMONRULES)

$(DVIFILE): $(TEXFILE) $(BIBFILE) $(DEPENDS)
	@echo $(BIBFILE)
	$(LATEX) $(FILE)
	$(LATEX) $(FILE)


$(BIBFILE):
	$(LATEX) $(FILE)
	$(BIBTEX) $(FILE)
	$(LATEX) $(FILE)


$(PDFFILE): $(TEXFILE) $(BIBFILE) $(DEPENDS)
	@echo $(BIBFILE)
	$(PDFLATEX) $(FILE)
	$(PDFLATEX) $(FILE)

xdvi:	
	xdvi -s 5 $(FILE)&

clean:
	rm -fr *.aux *.log *.dvi *.bbl *.lot *.lof *.blg *.toc *.out texfile.ps *~


