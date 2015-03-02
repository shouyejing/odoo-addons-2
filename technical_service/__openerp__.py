# -*- coding: utf-8 -*-


{
    'name': 'Technical Service',
    'version': '1.0',
    'complexity': "normal",
    'description': """
    Common Technical Service and repair module
""",
    "author": "Softteknik",
    "website": "",
    "category": "Generic Module",
    "depends": ["base", "product", "account"],


    "data": [
        #'security/repair_security.xml',
        'security/ir.model.access.csv',
        'views/technical_service_view.xml',
        'views/technical_service_workflow.xml',
		'views/technical_services_data.xml',
		'report/service_report.xml',
		'report/report_repair_service.xml',
		#'technical_services_data.xml',
        
                    ],
    'demo_xml': [],
    'installable': True,
    'auto_install': False,
}
