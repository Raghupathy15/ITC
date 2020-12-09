# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Sale Master',
    'version' : '1.1',
	'author' : 'Indglobal digital private limited',
    'summary': 'Adding additional fields in Sale Master',
    'description': """Inheriting fields in Sale Master""",
    'category' : 'Sale',
    'website': 'https://www.indglobal.com',
    'depends' : ['base', 'sale','account','indglobal_masters'],
    'data': ['views/sale_view.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OEEL-1',
}
