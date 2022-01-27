from odoo import models, fields


class Region(models.Model):
    _name = "geographical.region"

    _sql_constraints = [("internal_division", "UNIQUE (name)", "Geographical Region Name should be unique!")]

    name = fields.Char(string="Geographical Region")
