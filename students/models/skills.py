from odoo import models, fields

class Skills(models.Model):
    _name = 'skills.skills'
    _description = 'Skills'
    _inherit=['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Name", required=True)
    students_id = fields.Many2many(comodel_name="students.students", string="Students", )
