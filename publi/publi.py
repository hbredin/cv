import bibparse
import sys

# parse bib file
papers = bibparse.parse_bib('bredin.bib')
# get publication types
btypes = set([paper.btype for paper in papers])

subpapers = {}
for btype in btypes:
    subpapers[btype] = [paper.key for paper in papers if paper.btype == btype]

order = ['article', 'inbook', 'inproceedings', 'phdthesis']
titles = {'inproceedings': 'Conference and workshop proceedings',
          'article': 'Journal articles',
          'inbook': 'Book chapters',
          'phdthesis': 'PhD thesis',
          'wtf': 'Other publications'}
subpapers['wtf'] = [paper.key for paper in papers if paper.btype not in order]
order.append('wtf')

f = open('publi.tex', 'w')

f.write('\\documentclass{simplecv}\n')
f.write('\\usepackage[margin=1.5in]{geometry}\n')
f.write('\\usepackage[square, numbers, sort]{natbib}\n')

f.write('\\usepackage{multibib}\n')

for btype in order:
    f.write('\\newcites{%s}{%s}\n' % (btype, titles[btype]))

f.write('\\begin{document}\n')
f.write('\\pagestyle{empty}\n')

f.write('\\leftheader{LIMSI-CNRS\\\\BP 133\\\\91403 Orsay Cedex\\\\France\n')
f.write('}\n')

f.write('\\rightheader{TEL: +33 (0) 1 69 85 81 84\\\\\n')
f.write('\\texttt{\small bredin@limsi.fr}\\\\\n')
f.write('\\texttt{\small http://herve.niderb.fr/}\n')
f.write('}\n')

f.write("\\title{Herv\\'{e} Bredin -- Publications}\n")

f.write('\\maketitle\n')

f.write('\\vspace{-1cm}\n')
f.write('\\begin{center}\n')
f.write('(last updated on July 22nd, 2012)\n')
f.write('\\end{center}\n')

for btype in order:
    if not subpapers[btype]:
        continue
    f.write('\\nocite%s{%s}\n' % (btype, ",".join(subpapers[btype])))
    f.write('\\bibliography%s{bredin}\n' % btype)
    f.write('\\bibliographystyle%s{plainyr-rev}\n' % btype)

f.write('\\end{document}\n')

f.close()

