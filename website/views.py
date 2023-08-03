from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import  login_required,  current_user
views = Blueprint('views', __name__)
from .models import Product
from . import db
import json
from sqlalchemy import or_


@views.route('/', methods=['POST'])
@login_required
def home():
    itemsearched = request.form.get('searched')
    products = Product.query
    products = products.filter(or_(Product.product_name.like('%' + itemsearched + '%'), (Product.abcam_id.like('%' + itemsearched + '%')), (Product.description.like('%' + itemsearched + '%')))).all()
    print(products)
    multiple = "no"
    if len(products) == 0:
        multiple = "none"
    if len(products) > 1:
        multiple = "yes"
    return render_template("search.html", user=current_user, searched=itemsearched, products=products, multiple=multiple)

@views.route('/', methods=['GET'])
@login_required
def home_get():
    return render_template("Main Page.html", user=current_user)

@views.route('/search', methods=["POST"])
def search():
    pass
