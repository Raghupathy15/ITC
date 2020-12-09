# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Purchase Extend',
    'version' : '1.1',
    'author' : 'INDGLOBAL Digital Pvt Ltd',
    'summary': 'purchase',
    'description': """
Purchase
====================
System in Odoo allows you to keep track of your purchase.
    """,
    'category': 'Purchase',
    'website': 'https://www.indglobaldigital.com/',
    'depends' : ['purchase'],
    'data': [
        'views/purchase_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
