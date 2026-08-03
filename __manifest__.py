{
    'name': "Freelance Project Tracker",

    'depends': ['base', 'project'],

    'application': True,

    "data": [
        "security/ir.model.access.csv",
        "views/freelance_project_views.xml",
        "views/freelance_project_category_views.xml",
        "views/res_partner_views.xml",
        "views/freelance_marketplace_menus.xml",
    ],

}
