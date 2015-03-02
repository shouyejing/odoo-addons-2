# coding=utf-8

from datetime import timedelta
from openerp import models, fields, api, exceptions, _
import openerp.addons.decimal_precision as dp


class repair_category(models.Model):
    _name = 'repair.category'
    _description = "Repair Category"

    name = fields.Char(string='Category', index=True)


class repair_brand(models.Model):
    _name = 'repair.brand'
    _description = "Repair Brand"

    name = fields.Char(string='Brand', index=True)


class service_condition(models.Model):
    _name = 'service.condition'
    _description = "Service Condition"

    name = fields.Text(string='Condition', translate=True)


class repair_service(models.Model):
    _name = 'repair.service'
    _description = "Repair Service"
    _inherit = 'mail.thread'

    name = fields.Char(required=True)
    issue = fields.Text(string='Issue')
    color = fields.Integer()
    guarantee = fields.Boolean(string='Guarantee')
    repair_date = fields.Date(default=fields.Date.today, string='Service Date')
    partner_id = fields.Many2one('res.partner', string='Partner',
                                 required=True)
    repair_line = fields.One2many('repair.service.line', 'repair_id',
                                  string='Repair Lines')
    serial_no = fields.Char(string='Serial No', index=True)
    category = fields.Many2one(
        'repair.category', string='Category', select=True)
    model = fields.Char(string='Model No', index=True)
    brand = fields.Many2one('repair.brand', string='Brand', select=True)
    reviewer_id = fields.Many2one('res.users', string='Reviewer', select=True,
                                  default=lambda self: self.env.user)
    user_id = fields.Many2one('res.users', string='Assigned to', select=True,
                              track_visibility='onchange')
    solution = fields.Text(string='Solution')
    condition = fields.Many2one(
        'service.condition', string='Condition', translate=True)

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('done', 'Done'),
            ('return', 'Return'),
        ]
    )

    @api.one
    def action_draft(self):
        self.state = 'draft'

    @api.one
    def action_confirm(self):
        self.state = 'confirmed'

    @api.one
    def action_done(self):
        self.state = 'done'

    @api.one
    def action_return(self):
        self.state = 'return'


class repair_service_line(models.Model):
    _name = 'repair.service.line'
    _description = "Repair Services Line"

    @api.model
    def _default_currency(self):
        return self.env.user.company_id.currency_id

    repair_id = fields.Many2one('repair.service', string='Repair Service')
    product_id = fields.Many2one('product.product', string='Product',
                                 ondelete='set null', domain=[('type', '=', 'service')])
    quantity = fields.Float(string='Quantity',
                            digits=dp.get_precision('Product Unit of Measure'))
    price_unit = fields.Float(string='Unit Price', required=True,
                              digits=dp.get_precision('Product Price'), default=1)
    currency_id = fields.Many2one('res.currency', string="Currency", required=True,
                                  default=_default_currency,
                                  domain=[('name', 'in', ['TRY', 'EUR'])])

    @api.onchange('product_id')
    def onchange_scanned_ean(self):
        price_unit = self.product_id.list_price
        self.price_unit = self.env.user.company_id.currency_id.compute(price_unit,
                                                                       self.currency_id)
