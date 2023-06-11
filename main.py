from business.service import Service
from presentation.app import App, AppFrame
import tkinter as tk


def main():
    """
    Entry point for the program
    """
    app = App()
    AppFrame(app)
    app.mainloop()


if __name__ == "__main__":
    main()
