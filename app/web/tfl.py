

from app.view_models.tfl import Tfl
from app.web import web
from flask import request, jsonify, render_template
from app.forms.tfl_search import SearchForm
from app.spyder.search_tfl import search_on_tfl


@web.route('/tfl')
def search():

    form=SearchForm(request.args)
    if form.validate() :
        query=form.query.data.strip()
        result=search_on_tfl.search_by_query (query)
        tfl_data=Tfl()
        tfl_data._cut_tfl_data(result)

    return render_template('search_result.html',data=tfl_data.tfls)

