import bibparse
import sys

# def print_tab_title(title, papers):
#     href = ''.join(title.split())
#     sys.stdout.write('<li><a href="#%s" data-toggle="tab">%s (%d)</a></li>\n' % (href, title, len(papers)))
# 
# def print_tab_content(title, papers, active=False):
#     previous_year = ''
#     href = ''.join(title.split())
#     papers = reversed(sorted(papers, key=lambda paper: int(paper.data['Year'])))
#     if active:
#         sys.stdout.write('<div class="tab-pane fade in active" id="%s">\n' % href)
#     else:
#         sys.stdout.write('<div class="tab-pane fade in" id="%s">\n' % href)
#     sys.stdout.write('<div class="accordion" id="accordion%s">\n' % href)
#     for paper in papers:
#         if paper.data['Year'] != previous_year:
#             sys.stdout.write('<h3>%s</h3>\n' % paper.data['Year'])
#             previous_year = paper.data['Year']
#         sys.stdout.write('<div class="accordion-group">\n')
#         sys.stdout.write('    <div class="accordion-heading">\n')
#         sys.stdout.write('        <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion%s" href="#collapse%s_%s">\n' % (href, paper.key, href))
#         sys.stdout.write('        %s\n' % paper.data['Title'])
#         sys.stdout.write('        </a>\n')
#         sys.stdout.write('    </div>\n')
#         sys.stdout.write('    <div id="collapse%s_%s" class="accordion-body collapse">\n' % (paper.key, href))
#         sys.stdout.write('        <div class="accordion-inner">\n')
#         sys.stdout.write('        %s\n' % ', '.join(paper.data['Author'].split(' and ')))
#         if 'Booktitle' in paper.data:
#             sys.stdout.write('<p><em>%s</em></p>\n' % paper.data['Booktitle'])
#         if 'Journal' in paper.data:
#             sys.stdout.write('<p><em>%s</em></p>\n' % paper.data['Journal'])
#         if 'Abstract' in paper.data:
#             sys.stdout.write('<blockquote><p>%s</p></blockquote>\n' % paper.data['Abstract'])
#         sys.stdout.write('        </div>\n')
#         sys.stdout.write('    </div>\n')
#         sys.stdout.write('</div>\n')
#     sys.stdout.write('</div>\n')
#     sys.stdout.write('</div>\n')

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


f.write('\\begin{center}\n')
f.write('Last updated on July 22nd, 2012.\n')
f.write('\\end{center}\n')

for btype in order:
    if not subpapers[btype]:
        continue
    f.write('\\nocite%s{%s}\n' % (btype, ",".join(subpapers[btype])))
    f.write('\\bibliography%s{bredin}\n' % btype)
    f.write('\\bibliographystyle%s{plainyr-rev}\n' % btype)

f.write('\\end{document}\n')

f.close()

