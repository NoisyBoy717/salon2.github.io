
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/services/<service>')
def service_detail(service):
    # Здесь можно заменить на загрузку данных из базы или файла
    workers = {
        'hair': {
            'title': 'Парикмахер',
            'name': 'Алина Смирнова',
            'experience': 7,
            'description': 'Специалист по женским и мужским стрижкам, окрашиванию и укладке.'
        },
        'nails': {
            'title': 'Мастер маникюра',
            'name': 'Екатерина Новикова',
            'experience': 5,
            'description': 'Эксперт по маникюру, педикюру и дизайну ногтей.'
        },
        'makeup': {
            'title': 'Визажист',
            'name': 'Ольга Васильева',
            'experience': 6,
            'description': 'Профессиональный макияж на любые мероприятия.'
        },
        'spa': {
            'title': 'СПА-мастер',
            'name': 'Марина Белова',
            'experience': 8,
            'description': 'СПА-процедуры, массаж и ароматерапия.'
        },
        'cosmetology': {
            'title': 'Косметолог',
            'name': 'Наталья Орлова',
            'experience': 10,
            'description': 'Уход за кожей, чистка, омолаживающие процедуры.'
        },
    }

    info = workers.get(service)
    if not info:
        return "Услуга не найдена", 404
    return render_template('worker.html', **info)

if __name__ == '__main__':
    app.run(debug=True)


