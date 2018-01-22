# coding: utf-8
{
    'name': 'Instance Creator',
    'summary': '''
    Instance creator for test_app_github. This is the app.
    ''',
    'author': 'Vauxoo',
    'website': 'https://www.vauxoo.com',
    'license': 'AGPL-3',
    'category': 'Installer',
    'version': '11.0.0.0.0.0',
    'depends': ['l10n_mx_edi','l10n_mx_reports','company_country',
    ],
    'test': [
    ],
    'data': [
        'data/res_company.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'post_init_hook': 'post_init_hook',
    'auto_install': False,
    'application': True,
}