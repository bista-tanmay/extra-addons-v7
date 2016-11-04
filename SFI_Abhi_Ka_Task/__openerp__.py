{
    'name': 'SFI Task',
    'version': '1.0',
    'sequence':'1',
    'category':'SFI Task',
    'description': """
    Calculate % task
    """,
    'author': 'Tanmay @ Bista Solutions',
    'depends': ['base_setup','sale'],
    'data': [
             'views/sale_line_ytd_view.xml',
             'views/res_partner_view.xml',
             ],
    'installable': True,
    'auto_install': False,
    'application': '1',
}
