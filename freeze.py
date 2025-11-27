from app import app
from flask_frozen import Freezer


if __name__ == '__main__':
    app.config['FREEZER_BASE_URL'] = 'https://docs/Portfolio/'
    app.config['FREEZER_DESTINATION'] = 'docs'
    # app.config['FREEZER_DESTINATION_IGNORE'] = []
    freezer = Freezer(app)
    freezer.freeze()
    freezer.serve()
