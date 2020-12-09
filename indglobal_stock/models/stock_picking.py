from odoo import api, fields, models, _
from odoo.exceptions import UserError

class Picking(models.Model):
	_inherit = "stock.picking"
	_order = 'name desc'

	digital_signature = fields.Binary(string='Approver Sign')

	# def button_confirm(self):
	# 	print ('QQQQQQQQQQQQQQQQQ')
	# 	res = super(Picking, self).button_confirm()
	# 	print ('AAAAAAAAAAAAAAAAAAAAAAA')
	# 	if not self.digital_signature:
	# 		raise UserError(_('Please validate after getting Signature'))
	# 	return res