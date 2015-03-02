# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-2013 Softteknik(www.softteknik.com).
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
 'name': 'Amount to Word',
 'version': '0.1',
 'depends': ['account'],
 'category': 'Account',
 'author': 'Softteknik',
 'description': """
add amount to text in customer invoice(account.invoice)""",
 'website': 'http://www.softteknik.com',
 'data': ['amount_word_view.xml'],
 'installable': True,
 'active': False,
 }