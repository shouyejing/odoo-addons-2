# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).



{
    'name': 'Sale Quotation Optional Pdf',
    'summary': 'Sale Quotation Optional Products & Services QWEB PDF',
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'Sale',
    'description': """This module help to print sale quotation reports.""",
    'author': 'Softteknik',
    'website': 'http://www.softteknik.com',
    'depends': ['sale', 'website_quote', 'sale_comment_template', 'quotation_contact','web_tree_image'],
    'data': [
        'data/paper_format.xml',
        'views/report_menu.xml',
		'views/quotation_option.xml',
        'template/body_layout.xml',
        'template/header_footer_layout.xml',

    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
