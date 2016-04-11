# -*- coding: utf-8 -*-


########################################
# Turkish
#########################################

to_19_tr = (u'Sıfır', u'Bir', u'İki', u'Üç', u'Dört', u'Beş', u'Altı',
            u'Yedi', u'Sekiz', u'Dokuz', u'On', u'Onbir', u'Oniki', u'Onüç',
            u'Ondört', u'Onbeş', u'Onaltı', u'Onyedi', u'Onsekiz', u'Ondokuz')

tens_tr = (u'Yirmi', u'Otuz', u'Kırk', u'Elli', u'Altmış', u'Yetmiş', u'Seksen', u'Doksan')

denom_tr = ('', u'Bin', u'Milyon', u'Milyar', u'Triliyon', u'Katrilyon')


# convert a value < 100 to Turkish.

def _convert_nn_tr(val):
    if val == 1:
        return 'un'
    if val < 20:
        return to_19_tr[val]
    for (dcap, dval) in ((k, 20 + (10 * v)) for (v, k) in enumerate(tens_tr)):
        if dval + 10 > val:
            if val % 10:
                return dcap + '-' + to_19_tr[val % 10]
            return dcap


# convert a value < 1000 to Turkish, special cased because it is the level that kicks
# off the < 100 special case.  The rest are more general.  This also allows you to
# get strings in the form of 'forty-five hundred' if called directly.

def _convert_nnn_tr(val):
    word = ''
    (mod, rem) = (val % 100, val // 100)
    if rem == 1:
        word = u'Yüz '
    if rem == 2:
        word = u'İkiyüz '
    if rem > 2:
        word = to_19_tr[rem] + u' Yüz'
        if mod > 0:
            word += ' '
    if mod == 1 and rem != 0:
        word += 'unu'
    if mod == 1 and rem == 0:
        word = ''
    if mod > 1:
        word = word + _convert_nn_tr(mod)
    return word


def turkish_number(val):
    if val < 100:
        return _convert_nn_tr(val)
    if val < 1000:
        return _convert_nnn_tr(val)
    for (didx, dval) in ((v - 1, 1000 ** v) for v in range(len(denom_tr))):
        if dval > val:
            mod = 1000 ** didx
            l = val // mod
            r = val - (l * mod)
            ret = _convert_nnn_tr(l) + ' ' + denom_tr[didx]
            if r > 0:
                ret = ret + ' ' + turkish_number(r)
            return ret


def amount_to_text_tr(number,  currency='Lira'):
    number = '%.2f' % number
    units_name = currency
    list = str(number).split('.')
    start_word = turkish_number(int(list[0]))
    end_word = turkish_number(int(list[1]))
    cents_number = int(list[1])
    cents_name = (cents_number > 1) and u'Kuruş' or u'Kuruş'
    final_result = start_word + ' ' + units_name + ' ' + end_word + ' ' + cents_name
    return final_result
