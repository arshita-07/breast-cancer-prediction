from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    radius_mean = FloatField(label = 'Radius Mean', validators=[DataRequired()])
    texture_mean = FloatField(label = 'Texture Mean', validators=[DataRequired()])
    smoothness_mean = FloatField(label = 'Radius Mean', validators=[DataRequired()])
    compactness_mean = FloatField(label = 'Compactness Mean', validators=[DataRequired()])
    symmetry_mean = FloatField(label = 'Symmetry Mean', validators=[DataRequired()])
    fractal_dimension_mean = FloatField(label = 'Fractal Dimension Mean', validators=[DataRequired()])
    radius_se = FloatField(label = 'Radius Standard Error', validators=[DataRequired()])
    texture_se = FloatField(label = 'Texture Standard Error', validators=[DataRequired()])
    smoothness_se = FloatField(label = 'Radius Standard Error', validators=[DataRequired()])
    compactness_se = FloatField(label = 'Compactness Standard Error', validators=[DataRequired()])
    symmetry_se = FloatField(label = 'Symmetry Standard Error', validators=[DataRequired()])
    fractal_dimension_se = FloatField(label = 'Fractal Dimension Standard Error', validators=[DataRequired()])
    submit = SubmitField('Submit')