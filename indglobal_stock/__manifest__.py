# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Stock customization',
    'version' : '1.1',
	'author' : 'Indglobal digital private limited',
    'summary': 'Adding additional fields in stock',
    'description': """Inheriting fields in stock""",
    'category' : 'Stock',
    'website': 'https://www.indglobal.com',
    'depends' : ['base', 'stock'],
    'data': [
            'views/stock_move_views.xml',
            'views/stock_picking_views.xml',
            'data/ir_sequence_data.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OEEL-1',
}
