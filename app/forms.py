from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Length, required


class CategoriaForm(Form):
    nome = StringField('Nome', [Length(max=255), required()])


class ProductForm(Form):
    barcode = StringField('Barcode', [Length(max=255), required()])
    descrizione = StringField('Descrizione', [Length(max=255), required()])


if __name__ == '__main__':

    form = ProductForm()
    print(form.barcode.label)
    print(form.barcode)
    print(form.descrizione.label)
    print(form.descrizione)