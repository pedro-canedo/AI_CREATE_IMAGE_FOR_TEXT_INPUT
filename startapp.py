from asyncio.log import logger
import sys
from interface.api.routes import routes as flask_app
from interface.cli.main import cli as cli_app

def start_flask():
    logger.info("initializing flask app")
    flask_app.app.run(debug=True, host='localhost', port=5000)
    logger.info("Flask app started")

def start_cli():
    cli_app()

def main():
    if len(sys.argv) < 2:
        print("Please provide the app to start (flask or cli)")
        return

    app_to_start = sys.argv[1]
    if app_to_start == 'flask':
        start_flask()
    elif app_to_start == 'cli':
        start_cli()
    else:
        print(f"Unknown app: {app_to_start}")

if __name__ == "__main__":
    main()
