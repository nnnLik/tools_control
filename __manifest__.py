# -*- coding: utf-8 -*-
{
    'name': "Tools control",

    'summary': """
        Tool Control app and Tool Control ERP is a system that helps to keep the workplace, documentation and team relationships in order. 
    """,

    'description': """
        Everything is in its place 
        An employee used a tool but forgot to return or damaged it? No more lost inventory, no more lost profits!  
        Tool Control ERP is a convenient repository for reports created in ToolControl mobile application. 
        
        The ToolControl app takes a photo of a worker at the moment when she/he takes a tool. 
        Images are sent to Tool Control ERP, where you can always check who took this or that tool last and contact that person directly.  
    """,

    'author': "5sControl",
    'website': "https://eigsoft.com/5scontrol",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/tools_control_menu.xml',
    ],
    'application': True,
    'license': 'LGPL-3'
}
