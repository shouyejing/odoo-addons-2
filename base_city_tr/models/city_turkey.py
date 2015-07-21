# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp import netsvc


class CityTurkey(models.Model):
    _name = 'city.turkey'
    _description = 'Turkey City'
    # _rec_name = 'name'
    _order = 'country_id, name asc'

    @api.one
    @api.depends('city_turkey', 'district_turkey')
    def _compute_name(self):
        self.name = self.city_turkey + '-' + self.district_turkey

    name = fields.Char(string='Name', store=True, compute='_compute_name')
    kod = fields.Char(string='Kod', size=6)
    city_turkey = fields.Char(string='City Name', size=64)
    district_turkey = fields.Char(string='District Name', size=64)
    country_id = fields.Many2one('res.country', string='Country')


class TurkeyPartner(models.Model):
    _inherit = 'res.partner'
    _description = "Turkey City Partner"

    city_id = fields.Many2one('city.turkey', 'City Search')

    @api.multi
    def on_change_city_id(self, city_id):
        res = {}
        if city_id:
            city = self.env['city.turkey'].browse(city_id)
            res['city'] = city.city_turkey
            res['street2'] = city.district_turkey
            res['country_id'] = city.country_id

        return {'value': res}

        # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
