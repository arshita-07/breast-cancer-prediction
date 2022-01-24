
from dataclasses import dataclass
from flask import Flask,render_template
from forms import InputForm
from model import Calc

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"

@app.route('/home', methods=["GET","POST"])
def hello():
    iform = InputForm()
    if iform.validate_on_submit():
        return render_template('home.html', form = iform, data=Calc(iform.radius_mean.data, iform.texture_mean.data, iform.smoothness_mean.data,iform.compactness_mean.data,iform.symmetry_mean.data,iform.fractal_dimension_mean.data,iform.radius_se.data, iform.texture_se.data, iform.smoothness_se.data,iform.compactness_se.data,iform.symmetry_se.data,iform.fractal_dimension_se.data))
    else:
        print(iform.errors)
    return render_template('home.html', form = iform, data= "")

if __name__ == '__main__':
    app.run()

