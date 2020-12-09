# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Product Fields',
    'version' : '1.1',
	'author' : 'Indglobal digital private limited',
    'summary': 'Adding additional fields in Product Master',
    'description': """Inheriting fields in Product Master""",
    'category' : 'Product',
    'website': 'https://www.indglobal.com',
    'depends' : ['base', 'product'],
    'data': ['views/product_view.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OEEL-1',
}
