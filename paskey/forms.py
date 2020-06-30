from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from urllib.parse import urlparse

class openKey(FlaskForm):
    paskey = StringField(validators=[DataRequired()])
    submit = SubmitField()

class generateKey(FlaskForm):
    url = StringField(validators=[DataRequired()])
    submit = SubmitField()
    def validate_url(self, url):
        if urlparse(url.data).scheme != 'http' or urlparse(url.data).scheme != 'https':
            if "." not in urlparse("http://"+url.data).netloc:
                raise ValidationError("Not a valid url !")
            else:
                url.data = "http://" + url.data
        elif "." not in urlparse(url.data).netloc:
            raise ValidationError("Not a valid url !")


