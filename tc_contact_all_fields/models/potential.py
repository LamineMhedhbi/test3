from odoo import models, fields


class Potential(models.Model):
    _name = "potential"

    _sql_constraints = [("internal_division", "UNIQUE (name)", "Potential Name should be unique!")]

    name = fields.Char(string="Potential")
