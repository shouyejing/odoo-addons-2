# -*- coding: utf-8 -*-

from openerp import models, fields, api
from amount_to_text_tr import amount_to_text_tr
# from openerp.tools.translate import _


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    _description = "Account invoice"

    @api.one
    @api.depends('amount_total')
    def _amount_in_words(self):
        self.amount_words = amount_to_text_tr(self.amount_total)

    amount_words = fields.Char(u'Yazı ile', compute='_amount_in_words', help="The amount in words")
