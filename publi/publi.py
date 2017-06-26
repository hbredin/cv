from argparse import ArgumentParser
import bibparse
import sys

argparser = ArgumentParser(description='A tool to generate publication list')

argparser.add_argument('--english', action='store_true',
                       help="Generate english version")

argparser.add_argument('--francais', action='store_true',
                       help="Produire la version francaise")

argparser.add_argument('--software', action='store_true',
                       help="Add software/logiciel section")

args = argparser.parse_args()

if args.english == args.francais:
    sys.stderr.write("You must choose between 'english' and 'francais'\n")
    sys.exit()

# parse bib file
papers = bibparse.parse_bib('bredin.bib')
# get publication types
btypes = set([paper.btype for paper in papers])

subpapers = {}
for btype in btypes:
    subpapers[btype] = [paper.key for paper in papers if paper.btype == btype]

order = ['article', 'inbook', 'inproceedings', 'phdthesis']

if args.english:
    titles = {'inproceedings': 'Conference and workshop proceedings',
              'article': 'Journal articles',
              'inbook': 'Book chapters',
              'phdthesis': 'PhD thesis',
              'wtf': 'Other publications'}
else:
    titles = {'inproceedings': "Actes de conf\\'{e}rences et ateliers",
              'article': "Articles de journaux",
              'inbook': "Chapitres d'ouvrages",
              'phdthesis': "Th\`{e}se",
              'wtf': "Autres publications"}

subpapers['wtf'] = [paper.key for paper in papers if paper.btype not in order]
order.append('wtf')

if args.english:
    f = open('publi_EN.tex', 'w')
else:
    f = open('publi_FR.tex', 'w')

f.write('\\documentclass{simplecv}\n')
f.write('\\usepackage[margin=1.5in]{geometry}\n')
f.write('\\usepackage[square, numbers, sort]{natbib}\n')

f.write('\\usepackage{multibib}\n')

for btype in order:
    n = len(subpapers[btype])
    if n > 1:
        f.write('\\newcites{%s}{%s (%d)}\n' % (btype, titles[btype], n))
    else:
        f.write('\\newcites{%s}{%s}\n' % (btype, titles[btype]))

f.write('\\begin{document}\n')
f.write('\\pagestyle{empty}\n')

f.write('\\leftheader{LIMSI-CNRS\\\\BP 133\\\\91403 Orsay Cedex\\\\France\n')
f.write('}\n')

f.write('\\rightheader{TEL: +33 (0) 1 69 85 81 84\\\\\n')
f.write('\\texttt{\small bredin@limsi.fr}\\\\\n')
f.write('\\texttt{\small http://herve.niderb.fr/}\n')
f.write('}\n')

if args.software:
    if args.english:
        f.write("\\title{Herv\\'{e} Bredin -- Scientific contributions}\n")
    else:
        f.write("\\title{Herv\\'{e} Bredin -- Contributions scientifiques}\n")        
else:
    f.write("\\title{Herv\\'{e} Bredin -- Publications}\n")

f.write('\\maketitle\n')

# (last updated on ...)
from datetime import date
f.write('\\vspace{-1cm}\n')
f.write('\\begin{center}\n')
if args.english:
    f.write('(last updated on %s)\n' % date.today().strftime("%B %d, %Y"))
else:
    import locale
    locale.setlocale(locale.LC_ALL, '')
    f.write('(derni\`{e}re mise \`{a} jour le %s)\n' % date.today().strftime(" %d %B %Y"))

f.write('\\end{center}\n')

for btype in order:
    if not subpapers[btype]:
        continue
    f.write('\\nocite%s{%s}\n' % (btype, ",".join(subpapers[btype])))
    f.write('\\bibliography%s{bredin}\n' % btype)
    f.write('\\bibliographystyle%s{plainyr-rev}\n' % btype)

if args.software:
    if args.english:
        f.write('\\input{software}\n')
    if args.francais:
        f.write('\\input{logiciel}\n')

f.write('\\end{document}\n')

f.close()
