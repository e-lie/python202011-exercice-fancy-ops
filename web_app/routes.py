from flask import render_template
from . import web_app
from computation_libs.fancy_int_operations import fancy_operations 


@web_app.route('/')
@web_app.route('/index')
def index():
    return render_template('index.html', title='Webcalculator Home')

@web_app.route('/<operation_name>/<int_n>/<int_m>', methods=['GET'])
def compute(operation_name, int_n , int_m):
    try:
        operation_function = fancy_operations[operation_name]['function']
        operation_symbol = fancy_operations[operation_name]['symbol']
        fancy_result = operation_function(int(int_n), int(int_m))
    except:
        return render_template("invalid.html", title="Webcalculator Invalid Computation")

    title = "Webcalculator fancy {op}".format(op=operation_name)

    return render_template(
            "operation.html",
            title=title,
            operation_name=operation_name,
            operation_symbol=operation_symbol,
            int_n=int_n,
            int_m=int_m,
            fancy_result=fancy_result
        )
