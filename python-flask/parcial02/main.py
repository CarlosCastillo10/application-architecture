from flask_migrate import Migrate
from src.config import config_dict
from src import create_app, db

app_config = config_dict['config']
app = create_app(app_config)
Migrate(app, db)

if __name__ == '__main__':
    app.run()
