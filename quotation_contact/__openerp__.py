# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{
    'name': 'Quotation Contact',
    'version': '1.0',
    'license': 'AGPL-3',
    'category': 'Sale',
    'summary': 'Sale Quotation Contact',
    'description': """
    Adds sale ordering contact in sale order.
    """,
    'author': 'softteknik',
    'website': 'www.softteknik.com',
    'depends': [
        'sale',      
    ],
    'data': [
            'views/quotation_contact_view.xml',
    ],
    'demo': [
    ],
    'test': [

    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': [],
}
