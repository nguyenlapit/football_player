from odoo import fields,models

POSITIONS = [('0', 'Thủ môn'), ('1', 'Hậu vệ'),('2', 'Trung vệ'),('3', 'Tiền đạo'),('4', 'Hậu vệ trái'),('5', 'Hậu vệ phải'),('6', 'Trung vệ trái'),('7', 'Trung vệ phải')]

class Football_Player(models.Model):
    _name = 'football.player'

    name = fields.Char(string='Tên cầu thủ',required = True)
    avatar = fields.Binary(string='Hình ảnh', attachment=True)
    birthday = fields.Date('Ngày sinh',required = True)
    height = fields.Float('Chiều cao')
    weight = fields.Integer('Cân nặng')
    name_club = fields.Char(string='Tên câu lạc bộ')
    num_club = fields.Integer('Số áo tại câu lạc bộ')
    position = fields.Selection(string="Vị trí sở trường", selection=POSITIONS, POSITIONS=POSITIONS[0][Thủ môn], required=True)
    county_team = fields.Many2one(comodel_name='res.country', string='Quốc gia')
    num_county = fields.Integer('Số áo đội quốc gia')


class Football_Club(models.Model):
    _name = 'football.club'
    _rec_name = 'nameclub'

    nameclub = fields.Char(size=100,string='Tên câu lạc bộ')
    logoclub = fields.Binary(string='Logo', attachment = True)
    found_year = fields.Date(string='Ngày thành lập', requited = True)
    cup = fields.Many2one(comodel_name='football.cup', string='Giải đấu')
    county = fields.Many2one(comodel_name = 'res.country',string='Quốc gia')

class Football_Cup(models.Model):
    _name = 'football.cup'
    _rec_name = 'name_cup'
    name_cup = fields.Char(size=100,string='Giải đấu')
    cup_note = fields.Html(string='Ghi chú')




