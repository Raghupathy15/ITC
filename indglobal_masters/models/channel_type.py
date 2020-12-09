# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models,_
import re
from odoo.exceptions import ValidationError,UserError

class ChannelType(models.Model):
	_name = "channel.type"
	_description = "Channel Type Master"
	_inherit = 'mail.thread'

	name = fields.Char('Name',track_visibility='always')