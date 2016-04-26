# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Default Sale Order PDF Customize',
    'version': '8.0.1.0.0',
    'author': 'Softteknik',
    'license': 'AGPL-3',
    'description': """
        Default Sale Order PDF Customize
    """,
    'category': 'Sales',
    'sequence': 3,
    'website': 'http://softteknik.com',
    'images': [],
    'depends': [
        'sale_comment_template',
        'website_quote',
        ],

    'demo_xml': [],
    'data': [
        # 'data/paperformat.xml',
        'template/pdf_sale_order.xml',
        'template/pdf_sale_order_layout.xml',
        'template/pdf_sale_order_layout_header.xml',
        'template/pdf_sale_order_layout_footer.xml',
        ],
    'test': [],
    'auto_install': False,
    'application': False,
    'installable': True,
    
}
