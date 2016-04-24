# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).



{
    'name': 'Sale Quotation Pdf',
    'summary': 'Sale Quotation QWEB PDF',
    'version': '1.0',
    'category': 'Sale',
    'description' : """This module help to print sale quotation reports.""",
    'author': 'Softteknik',
    'website': 'http://www.softteknik.com',
    'depends': ['sale','website_quote','sale_comment_template'],
    'data': [
            'data/paperformat.xml',
            # 'data/sale_report.xml',
            'views/report_menu.xml',
            'views/quotation_view.xml',
			'template/sale_order_layout.xml',
            
            # 'views/sale_order.xml',
            ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
