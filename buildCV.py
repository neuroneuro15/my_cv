__author__ = 'nicholas'

from pylatex import Document, Section, Subsection, Command, Package, UnsafeCommand
from pylatex.base_classes import CommandBase, Arguments
from pylatex.utils import italic, NoEscape
from pylatex.document import Environment


doc = Document('docs/delgrosso_cv',
               documentclass='article')

# Set Packages
doc.packages.append(Package('marginnote'))
doc.packages.append(Package('graphicx'))
doc.packages.append(Package('classicthesis', ['nochapters']))
doc.packages.append(Package('currvita', ['LabelsAligned']))
doc.packages.append(Package('hyperref'))
#
# Make New Commands
class MarginText(CommandBase):
    _latex_name = 'MarginText'
doc.append(UnsafeCommand('newcommand', r'\MarginText', options=1,
                 extra_arguments=r'\marginpar{\raggedleft\small#1}')
           )

doc.append(UnsafeCommand('newlength', r'\datebox', ))
doc.append(UnsafeCommand('settowidth', r'\datebox', extra_arguments='Tuebingen, Germany'))


##
class NewEntry(CommandBase):
    _latex_name = 'NewEntry'
doc.append(UnsafeCommand('newcommand', r'\NewEntry', options=2,
              extra_arguments=r'\noindent\hangindent=2em\hangafter=0 \parbox{\datebox}{\small \textit{#1}}\hspace{1.5em} #2 \vspace{0.5em}\\')
           )

##
doc.append(UnsafeCommand('hypersetup',
                         extra_arguments=r'colorlinks, breaklinks, urlcolor=Maroon, linkcolor=Maroon')
           )

doc.append(UnsafeCommand('renewcommand', r'\cvheadingfont', extra_arguments=r'\LARGE\color{Maroon}')
           )

##
class Description(CommandBase):
    _latex_name = 'Description'
doc.append(UnsafeCommand('newcommand', r'\Description', options=1,
                         extra_arguments=r'\hangindent=2em\hangafter=0\noindent\raggedright\footnotesize{#1}\par\normalsize\vspace{1em}\\')
           )

##
class SubHeading(CommandBase):
    _latex_name = 'SubHeading'
doc.append(UnsafeCommand('newcommand', r'\SubHeading', options=1,
                         extra_arguments=r'\vspace{.5em}\noindent\spacedlowsmallcaps{#1}\vspace{0.7em}\\'))

# Make Preamble
doc.preamble.append(Command('title', 'Research Experiences'))
doc.preamble.append(Command('author', 'Nicholas A. Del Grosso'))
doc.preamble.append(Command('date', NoEscape(r'\today')))


doc.append(SubHeading('Research Experiences'))
doc.append(NewEntry(['Universitat Tuebingen', 'Prof. Dr. Niels Birbaumer']))
doc.append(NewEntry(['Universitat Tuebingen', 'Prof. Dr. Niels Birbaumer']))
doc.generate_pdf()
doc.generate_tex()