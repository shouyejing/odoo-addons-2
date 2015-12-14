# -*- coding: utf-8 -*-


{
    'name': 'User Accounts Information',
    'version': '8.0.1.0',
    'licence': 'AGPL v3',
	'summary': 'user name, password, host_name or ip',
    'description': """
    Managing user accounts for example Modem, firewall, hosting ... 
""",
    'author': 'Softteknik',
    'website': '',
    'category': 'Generic Module',
    'depends': ['base', 'mail'],


    'data': [
            'views/account_service_view.xml',
			'views/account_service_data.xml',
			'security/account_service_security.xml',
			'security/ir.model.access.csv',
       
        ],
    'demo_xml': [],
    'installable': True,
    'auto_install': False,
}
