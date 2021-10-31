from datetime import date

from marshmallow import Schema, fields


class Task(Schema):
    id = fields.Str(required=False)
    description = fields.Str(required=False, load_default='Empty')
    start = fields.Str(required=False, format="%dd-%mm-%YYYY", missing="Any", default="Any")
    end = fields.Str(required=False, format="%dd-%mm-%YYYY", missing="Any", default="Any")
    completed = fields.Boolean(required=False, load_default=False)
    creationDate = fields.Date(required=False, load_default=date.today())


class ManyTasks(Schema):
    tasks = fields.List(fields.Nested(Task), required=True)

