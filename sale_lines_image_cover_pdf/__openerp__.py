# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).



{
    'name': 'Sale Quotation line image Pdf',
    'summary': 'Sale Quotation Line Image QWEB PDF',
    'version': '1.0',
	'license': 'AGPL-3',
    'category': 'Sale',
    'description' : """This module help to print sale quotation reports.""",
    'author': 'Softteknik',
    'website': 'http://www.softteknik.com',
    'depends': ['sale','website_quote','sale_comment_template','quotation_contact'],
    'data': [
            'data/paperformat.xml',
            'views/report_menu.xml',
            'template/body_lines_image_layout.xml',
			#'template/header_footer_layout.xml',
                        
            ],
    'demo': [],
    'test': [],
    'installable': True,
	'application': False,
    'auto_install': False,
}
