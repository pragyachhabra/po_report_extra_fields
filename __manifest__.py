# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016-TODAY Linserv Aktiebolag, Sweden (<http://www.linserv.se>).
#
##############################################################################
{
    "name": "Purchase Order Report Extra Fields",
    "version": "1.0",
    "author": "Linserv AB",
    "category": "Purchase",
    "summary": "Purchase Order Report Extra Fields",
    "website": "www.linserv.se",
    "contributors": [
        'Pragya Chhabra <pragyachhabbra@gmail.com'
    ],
    "license": "",
    "depends": ['base', 'purchase', 'website_quote'],
    'description': """
        
        Additional fields,
        Hides "Invoice Order" button in Purchase Order, which prevents invoice creation from multiple purchase orders,
        Purchase Order's Estimate By field to Project.
        
    """,
    "demo": [],
    "data": [

        'views/inherited_purchase_report_templates.xml',
    ],
    "test": [],
    "js": [],
    "css": [],
    "qweb": [],
    "installable": True,
    "auto_install": False,
}
