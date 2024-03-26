import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
import base64


# check for excluded characters
def character_check(form, field):
    excluded_chars = "*?!'^+%&/()=}][{$#@<>"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed."
            )

class RegisterForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])
    firstname = StringField(validators=[DataRequired(), character_check])
    lastname = StringField(validators=[DataRequired(), character_check])
    phone = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired(), Length(min=6,max=12, message='Password must be between 6 and 12 characters long')])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password', message='Both password fields must match')])
    pin_key = StringField(validators=[DataRequired(), Length(min=32, max=32, message='Pin must be 32 characters long')])
    submit = SubmitField()

    # phone number format checker
    def validate_phone(self, phone):
        p = re.compile(r'\d{5} \d{6}')
        if not p.match(self.phone.data):
            raise ValidationError("Phone must be in the form XXXXX-XXXXXX")

    # password format checker
    def validate_password(self, password):
        p = re.compile(r'(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[*?!^+%&/()=}{$#@<>])')
        if not p.match(self.password.data):
            raise ValidationError("Password must contain 1 digit, 1 lowercase, 1 uppercase and 1 special character")
        
    def validate_pin_key(self, pin_key):
        try:
            decoded_bytes = base64.b32decode(self.pin_key.data.encode('utf-8'))
            if len(decoded_bytes) != 20:  # Check if the decoded bytes length is 20
                raise ValidationError('Pin must be 32 characters long and base32 encoded')
        except base64.binascii.Error:
            raise ValidationError('Invalid base32 encoding. Must only use letters A-Z and digits 2-7')




class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired()])
    pin = StringField(validators=[DataRequired()])
    submit = SubmitField()