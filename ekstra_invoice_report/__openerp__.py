# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (C) 2014-Today OpenERP SA (<http://www.openerp.com>).
# (<http://www.softteknik.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Ekstra Invoice Layouts',
    'version': '1.0',
    'sequence': 18,
	'category': 'Invoice',
    'summary': 'Additional reports to be printed for invoice The amount to words view',
    'description': """
Create additional printouts of invoices
=======================================
Adds additonal layout of invoice and button under Print drop down option.
""",

    'author': 'Softteknik',
    'website': 'http://www.softteknik.com',
    'depends': ['account', 'report', 'amount_word'],
    'category': 'Account',
    'data': [
        'partner_view.xml',
        'invoice_ekstra.xml',
        'views/report_ekstra_invoice.xml'
    ],
    'installable': True,
    'active': False,
}
