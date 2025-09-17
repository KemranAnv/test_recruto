from flask import Flask, request, render_template
import re
import os
import logging

app = Flask(__name__)

# Базовое логирование
logging.basicConfig(level=logging.INFO)
app.logger.info('Starting Flask application...')

@app.route('/')
def hello():
    name = request.args.get('name', 'Recruto').strip()
    message = request.args.get('message', 'Давай дружить').strip()
    
    # Валидация: только буквы, цифры, пробелы и некоторые символы (для кириллицы и латиницы)
    if not re.match(r'^[\w\sа-яА-ЯёЁ!,.?-]+$', name) or not name:
        name = 'Recruto'
    if not re.match(r'^[\w\sа-яА-ЯёЁ!,.?-]+$', message) or not message:
        message = 'Давай дружить'
    
    return render_template('index.html', name=name, message=message)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)