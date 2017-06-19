# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp.osv import fields, osv , orm
from datetime import time, datetime
from openerp.tools.translate import _

class superheros_modelo(osv.osv):
	_name = 'superheros.modelo'
	_description = 'Formulario Super Heroes'
	_columns = {
		'nombre' : fields.char('Nombre' , size=256, required = True, help ='Este es el nombre'),
        'poder' : fields.char('Poder' , size=256, required = True, help ='¿Cuál es su poder?'),
		'equipo' : fields.char('Equipo',size=256, required= True, help ='¿Capitán América o Ironman?'),
		'puntuacion' : fields.integer('Puntuacion', required=True),
		'active': fields.boolean('Activo'),
	}
	_defaults = {
		'active' : 'true',
	}
superheros_modelo()