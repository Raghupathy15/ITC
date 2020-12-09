from odoo import api, fields, models, _
from odoo.exceptions import UserError

class AccountMoveLine(models.Model):
	_inherit = "account.move.line"

	@api.constrains('quantity')
	def _check_quantity(self):
		qty_count = 0
		same_inv_qty = 0
		if self.move_id.inv_split_ref:
			parent_inv = self.env['account.move'].sudo().search([('name','=',self.move_id.inv_split_ref)])
			if parent_inv:
				for line in parent_inv.invoice_line_ids:
					qty_count += line.quantity
				same_inv = self.env['account.move'].sudo().search([('inv_split_ref','=',self.move_id.inv_split_ref)])
				if same_inv:
					for same in same_inv.invoice_line_ids:
						same_inv_qty += same.quantity
						if qty_count < same_inv_qty:
							raise UserError(_('Quantity should be less than the invoice no "%s".'%(self.move_id.inv_split_ref)))

