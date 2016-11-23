# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)


from openerp import models, fields


class SaleOrderOption(models.Model):
    _inherit = 'sale.order.option'
    _description = "Sale Options"

    image_small = fields.Binary('Product Image', related='product_id.image_small', readonly=True)
    currency_id = fields.Many2one(related='order_id.currency_id', store=True, string='Currency', readonly=True)
