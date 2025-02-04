# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this 
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'open62541'
copyright = '2025, The open62541 authors'
author = 'The open62541 authors'

version = '${OPEN62541_VER_MAJOR}.${OPEN62541_VER_MINOR}'
release = '${OPEN62541_VER_MAJOR}.${OPEN62541_VER_MINOR}.${OPEN62541_VER_PATCH}${OPEN62541_VER_LABEL}'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.graphviz',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

master_doc = 'toc'

numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_logo = 'open62541_html.png'

# -- Options for LaTeX output ---------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_logo = "open62541.png"

latex_documents = [
  # (startdocname,   targetname,      title,                     author, theme,    toctree_only)
    (master_doc,     'open62541.tex', 'open62541 Documentation', author, 'manual', False),
]

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',

# Font settings
'fontpkg': r"""
\usepackage[scaled=.98,varqu,varl]{zi4}
\usepackage[default,semibold]{sourcesanspro}
""",

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '11pt',

# Clean up the header and footer
'preamble': r"""
\fancypagestyle{normal}{
    \fancyhf{}
    \fancyfoot[RO,LE]{\thepage}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[RO,LE]{\thepage}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}""",

'maketitle': r"""
    \makeatletter
 \begin{titlepage}%
      \begingroup % for PDF information dictionary
       \def\endgraf{ }\def\and{\& }%
       \pdfstringdefDisableCommands{\def\\{, }}% overwrite hyperref setup
       \hypersetup{pdfauthor={\@author}, pdftitle={\@title}}%
      \endgroup
    \begin{flushright}%
	\vspace*{2\baselineskip}
      \begin{minipage}{.75\linewidth}
      \sphinxlogo
      \end{minipage} \bigskip \par
      \py@HeaderFamily
      {\Huge \@title \par}
      {\itshape\LARGE \py@release\releaseinfo \par}
      \bigskip
      {\large \@date \par}%
    \end{flushright}
  \end{titlepage}%
  \if@openright\cleardoublepage\else\clearpage\fi
\makeatother
""",

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# -- Options for manual page output ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-manual-page-output

man_pages = [
  # (source start file, name,        description,               authors,  manual section)
    (master_doc,        'open62541', 'open62541 Documentation', [author], 1)
]
