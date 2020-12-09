{
    'name' : 'Loyalty Management System',
    'version' : '1.1',
	'author' : 'Indglobal digital private limited',
    'summary': 'Loyalty Management System',
    'sequence': 1,
    'description': """Loyalty Management System""",
    'category' : 'base',
    'website': 'https://www.indglobal.com',
    'depends' : ['base','mail'],
    'data': [
            'views/loyalty_mgt_views.xml',
            'security/ir.model.access.csv',
            ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OEEL-1',
}