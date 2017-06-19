# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

##########################################################################

{
	'name': 'Super HEROS Manuel',
	'version': '1.0',
	'author': 'Manuel García Amador',
	'category': 'Ocio',
	'summary': 'Ejemplo de un modulo de odoo',
    'website': 'manugara53@gmail.com',
	'description': """
Modulo de Super heroes de MARVEL para la clase de Sistemas de Gestion empresarial.
=========================
Esto es un trabajo para entregar.
    """,
	'license': 'AGPL-3',
    'depends': ['sale'],
	'update_xml': [
		'superheros_view.xml',
	],
	'installable': True,
	'active': False,
}
		