# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)

########################################
# Turkish
#########################################

to_19 = ('Sıfır', 'Bir', 'İki', 'Üç', 'Dört', 'Beş', 'Altı',
         'Yedi', 'Sekiz', 'Dokuz', 'On', 'Onbir', 'Oniki', 'Onüç',
         'Ondört', 'Onbeş', 'Onaltı', 'Onyedi', 'Onsekiz', 'Ondokuz')
tens = (
    'Yirmi', 'Otuz', 'Kırk', 'Elli', 'Altmış', 'Yetmiş', 'Seksen', 'Doksan')
denom = ('',
         'Bin', 'Milyon', 'Milyar', 'Triliyon', 'Katrilyon',
         'Quintillion', 'Sextillion', 'Septillion', 'Octillion', 'Nonillion',
         'Decillion', 'Undecillion', 'Duodecillion', 'Tredecillion',
         'Quattuordecillion', 'Sexdecillion', 'Septendecillion',
         'Octodecillion', 'Novemdecillion', 'Vigintillion')

# convert a value < 100 to Turkish.
def _convert_nn(val):
    if val == 1:
        return 'un'
    if val < 20:
        return to_19[val]
    for (dcap, dval) in ((k, 20 + (10 * v)) for (v, k) in enumerate(tens)):
        if dval + 10 > val:
            if val % 10:
                return dcap + '-' + to_19[val % 10]
            return dcap


# convert a value < 1000 to Turkish, special cased because it is the level that kicks
# off the < 100 special case.  The rest are more general.  This also allows you to
# get strings in the form of 'forty-five hundred' if called directly.
def _convert_nnn(val):
    word = ''
    (mod, rem) = (val % 100, val // 100)
    if rem == 1:
        word = 'Yüz '
    if rem == 2:
        word = 'İkiyüz '
    if rem > 2:
        word = to_19[rem] + ' Yüz'
        if mod > 0:
            word = word + ' '
    if mod == 1 and rem != 0:
        word = word + 'unu'
    if mod == 1 and rem == 0:
        word = ''
    if mod > 1:
        word = word + _convert_nn(mod)
    return word


def english_number(val):
    if val < 100:
        return _convert_nn(val)
    if val < 1000:
        return _convert_nnn(val)
    for (didx, dval) in ((v - 1, 1000 ** v) for v in range(len(denom))):
        if dval > val:
            mod = 1000 ** didx
            l = val // mod
            r = val - (l * mod)
            ret = _convert_nnn(l) + ' ' + denom[didx]
            if r > 0:
                ret = ret + ', ' + english_number(r)
            return ret


def amount_to_text(number, currency):
    number = '%.2f' % number
    units_name = currency
    list = str(number).split('.')
    start_word = english_number(int(list[0]))
    end_word = english_number(int(list[1]))
    cents_number = int(list[1])
    cents_name = (cents_number > 1) and 'Kuruş' or 'Kuruş'

    return ' '.join(filter(None,
                           [start_word, units_name,
                            (start_word or units_name) and (
                                end_word or cents_name) and 've',
                            end_word, cents_name]))


########################################
# Generic functions
########################################

_translate_funcs = {'tr': amount_to_text}

##############################################################################
# TODO: we should use the country AND language (ex: septante VS soixante dix)
# TODO: we should use en by default, but the translation func is yet to be
# implemented
# ############################################################################

def amount_to_text(nbr, lang='tr', currency='Lira'):
    """ Converts an integer to its textual representation, using the language
     set in the context if any.

        Example::

            1654: thousands six cent cinquante-quatre.
    """
    import openerp.loglevels as loglevels
    # if nbr > 10000000:
    # _logger.warning(_("Number too large '%d', can not translate it"))
    # return str(nbr)

    if not _translate_funcs.has_key(lang):
        _logger.warning(_("no translation function found for lang: '%s'"),
                        lang)
        # TODO: (default should be en) same as above
        lang = 'en'
    return _translate_funcs[lang](abs(nbr), currency)


if __name__ == '__main__':
    from sys import argv

    lang = 'nl'
    if len(argv) < 2:
        for i in range(1, 200):
            print i, ">>", int_to_text(i, lang)
        for i in range(200, 999999, 139):
            print i, ">>", int_to_text(i, lang)
    else:
        print int_to_text(int(argv[1]), lang)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: