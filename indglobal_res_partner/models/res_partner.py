# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models,_
import re
from odoo.exceptions import ValidationError,UserError

class ResPartner(models.Model):
	_inherit = "res.partner"

	customer_id = fields.Char('Customer ID')
	forum_code = fields.Integer('Forum Code')
	track_points = fields.Integer('Track points')
	collected_points = fields.Integer('Collected Points')
	tin = fields.Char('TIN')
	dl_20 = fields.Char('DL20')
	dl_21 = fields.Char('DL21')
	fssai_no = fields.Char('FSSAINo')
	rcs_id = fields.Char('RCS ID')
	customer_type = fields.Selection([('retail', 'Retail')],string='Customer category')
	trade_customer = fields.Selection([('retail', 'Retailer')],string='Trade Customer Category')
	channel_type_id = fields.Many2one('channel.type',string="Channel Type")
	beat = fields.Char('Beat')
	zone = fields.Char('Zone')
	market_district = fields.Char('Market District')
	sub_district = fields.Char('Sub District')
	pop_group = fields.Selection([('2_5', '2 - 5'),('5_10', '5 - 10'),('51_100', '51 - 100')],string='Pop Group')

	_sql_constraints = [('customer_id', 'unique(customer_id)', 'Customer ID already exists!'),]

	@api.constrains('vat')
	def _check_validations(self):
		if self.vat:
			if(len(self.vat)!=15):
				raise ValidationError(_('GSTIN Number length should be in 15 !..'))
		if self.tin:
			if (len(self.tin)!= 11):
				raise ValidationError(_('TIN Number length should be in 11 !..'))
		if self.mobile:
			match = re.match("^[0-9]*$",self.mobile)
			if match == None:
				raise ValidationError(_("Enter correct 'Mobile' Number"))
		if self.email:
			match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
			if match == None:
				raise ValidationError('Not a valid "Email" ID') 
		return True