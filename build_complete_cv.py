__author__ = 'nicholas'

import yaml
from cv_preamble import *

# Get data for cv.
with  open('research_experiences.yaml') as f:
    data= yaml.load(f)

# Create Latex file, and the CV object to build sections out of.
doc = get_cv_doc('docs/delgrosso_cv')
with doc.create(CV(data, arguments='Nicholas A. Del Grosso')) as cv:

    def format_personal(entry):
        for key, value in entry.items():
            if 'mail' in key:
                value = Email(value)
            return HeaderOnly([key, value])
    cv.build_section('Personal Info', format_personal)

    cv.build_section_itemized('Goals', lambda x: x)

    cv.build_section('Education', lambda x: NewEntry([x['Date'], x['Degree'], x['Institute'], '']))

    cv.build_section('Research Experience', lambda x: NewEntry([' -\n  '.join([x['StartDate'], x['EndDate']]),
                                                                       x['Institute'], x['Supervisor'], x['Description']]))

    cv.build_section('Industry Experience', lambda x: NewEntry([' -\n '.join(x['StartDate', x['EndDate']]),
                                                                       x['Position'], x['Institute'], x['Description']]))

    cv.build_section('Journal Publications', lambda x: Description(x))

    cv.build_section('Conference Publications', lambda x: NewEntry([x['Date'], x['Conference'],
                                                                           x['Title'], x['Description']]))

    # def format_skill_item(entry):
    #     import pdb
    #     pdb.set_trace()
    #     return bold(''.join(entry.keys())) + NoEscape(': ') + NoEscape(', '.join(entry.values()))
    # build_section_itemized(cv, data, 'Skills', format_skill_item)

    cv.build_section('Awards', lambda x: DescMarg([x['Date'], x['Title']]))

    # Add a signature at the bottom
    cv.append(includegraphics(options='width=5cm', arguments='images/Signaturetransparant.png'))


doc.generate_pdf()
doc.generate_tex();