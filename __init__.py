from app import create_app

__version__ = '1.0.0'

if __name__ == '__main__':
    app = create_app()
    app.run()