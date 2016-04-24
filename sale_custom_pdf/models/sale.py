# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    contact_id = fields.Many2one('res.partner', 'Contact',
                                 domain="[('parent_id','=',partner_id)]")
