from odoo import models, fields


class Job(models.Model):
    _name = "Job.title"

    _sql_constraints = [("internal_division", "UNIQUE (name)", "Job Title Name should be unique!")]

    name = fields.Char(string="Job Title")
