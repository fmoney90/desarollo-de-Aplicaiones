from  flask import Flask,request, render_template, redirect
from va_module import velocidad

app = Flask( __name__)

@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Unidad2')


@app.route('/BYMEUnidad2', methods=['POST'])
def execute() -> 'html':
    e = float(request.form['e'])
    t = float(request.form['t'])


    title = 'This is the equation\'s result'
    result = velocidad(e, t)
    return render_template('result.html',
                           the_title=title,
                           the_e=e,
                           the_t=t,
                           the_result=result, )


if __name__ == '__main__':
    app.run()
