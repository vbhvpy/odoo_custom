# -*- coding: utf-8 -*-
{
    'name': "Perfomance Evaluation",

    'summary': """
         Extend functioality for performance Evaluation""",

    'description': """
        This will be used for the Employee performance evaluation Program in the system.
    """,

    'author': "Vaibhav, Snackat",
    'website': "www.snackat.com",

    'category': 'Human Resources/Employees',
    'version': '14.0.1',
    'license': 'AGPL-3',
    'depends': ['hr', 'base'],
    'data': [
        'security/performance_evaluation_security.xml',
        'security/ir.model.access.csv',
        'views/performance_evaluation_view.xml',
        'data/ir_sequence_data.xml',
    ],

    'installable': True,
    'application': True,
        
}
