import sys
from app import app
from streamlit import runtime
from streamlit.web import cli

def main():
    app()
if __name__ == '__main__':
    if runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(cli.main())