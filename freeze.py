from app import app
from flask_frozen import Freezer

app.config['FREEZER_BASE_URL'] = 'https://docs/Portfolio/'
app.config['FREEZER_DESTINATION'] = 'docs'
# app.config['FREEZER_DESTINATION_IGNORE'] = []
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    freezer.serve()
