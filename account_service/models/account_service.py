# coding=utf-8

from openerp import models, fields, api


class ServiceName(models.Model):
    _name = 'service.name'
    _description = "Service Name"

    name = fields.Char(string='Service Name')


class AccountService(models.Model):
    _name = 'account.service'
    _description = "Account Service"
    _inherit = 'mail.thread'

    name = fields.Char(string='Code', default='New')
    color = fields.Integer()
    start_date = fields.Date(default=fields.Date.today, string='Start Date')
    end_date = fields.Date(string='End Date')
    partner_id = fields.Many2one('res.partner', string='Partner',
                                 required=True)
    account_service_ids = fields.One2many('account.service.line', 'account_service_id',
                                          string='Account Service Lines')
    user_id = fields.Many2one('res.users', string='User', select=True,
                              default=lambda self: self.env.user)
    state = fields.Selection([('open', 'Open'), ('closed', 'Closed')])

    @api.one
    def action_open(self):
        self.state = 'open'

    @api.one
    def action_closed(self):
        self.state = 'closed'

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('account.service') or 'New'

        result = super(AccountService, self).create(vals)
        return result


class AccountServiceLine(models.Model):
    _name = 'account.service.line'
    _description = "Repair Services Line"

    name = fields.Char(string='User Name')
    account_service_id = fields.Many2one('account.service')
    service_name_id = fields.Many2one('service.name', string='Service Name')
    password = fields.Char(string='Password')
    host_name = fields.Char(string='Host or IP')
    date = fields.Date(default=fields.Date.today, string='Date')
