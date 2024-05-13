import tkinter as tk
import tkcalendar

# Color palette for the GymGenie GUI.
black = "BLACK"
white = "WHITE"
dark_red = "#9B2226"
red = "#AE2012"
brown = "#BB3E03"
orange = "#CA6702"
yellow = "#EE9B00"
dark_blue = "#005F73"
blue = "#357F93"
light_blue = "#5d99a9"

def create_frame(root, **kwargs):
    """
    Creates a frame with customizable properties.

    Parameters
    ----------
    root : tkinter.Tk or tkinter.Toplevel
        The root or top-level window in which the frame should be placed.

    **kwargs : dict, optional
        Additional keyword arguments to customize the frame.
        Supported keyword arguments include:
            - bg: Background color of the frame (default is "blue")
            - pady: Padding in the y-direction (default is 20)
            - rows: Number of rows to configure in the frame (default is 1)
            - columns: Number of rows to configure in the frame (default is 1)

    Returns
    -------
    frame : tkinter.Frame
        The created frame widget.
    """
    # Default values
    bg = kwargs.get("bg", blue)
    pady = kwargs.get("pady", 20)
    rows = kwargs.get("rows", 1)
    columns = kwargs.get("columns", 1)

    # Create frame
    frame = tk.Frame(root, bg=bg, pady=pady)
    frame.pack(fill=tk.BOTH, expand=True)

    # Configure rows
    for i in range(rows):
        frame.rowconfigure(i, weight=1)

    # Configure columns
    for i in range(columns):
        frame.columnconfigure(i, weight=1)

    return frame


def create_button(frame, command, text, **kwargs):
    """
    Creates a button with customizable properties.

    Parameters
    ----------
    frame : tkinter.Frame
        The frame in which the button should be placed.

    command : function
        A function for what should happen when the button is clicked.

    text : str
        The text that should be displayed on the button.

    **kwargs : dict, optional
        Additional keyword arguments to customize the button.
        Supported keyword arguments include:
            - font: Tuple specifying the font (default is ("Arial", 12, "bold"))
            - width: Width of the button (default is 20)
            - height: Height of the button (default is 1)
            - background: Background color of the button (default is dark blue)
            - foreground: Foreground color of the button (default is white)
            - activebackground: Background color of the button when active (default is light blue)
            - activeforeground: Foreground color of the button when active (default is white)
            - border: Border width of the button (default is 0)
            - cursor: Cursor style when hovering over the button (default is "hand2")

    Returns
    -------
    button : tkinter.Button
        The created button widget.
    """
    # Default values
    font = kwargs.get("font", ("Arial", 12, "bold"))
    width = kwargs.get("width", 20)
    height = kwargs.get("height", 1)
    background = kwargs.get("background", dark_blue)
    foreground = kwargs.get("foreground", "white")
    activebackground = kwargs.get("activebackground", light_blue)
    activeforeground = kwargs.get("activeforeground", "white")
    border = kwargs.get("border", 0)
    cursor = kwargs.get("cursor", "hand2")

    button = tk.Button(
        frame,
        command=command,
        text=text,
        font=font,
        background=background,
        foreground=foreground,
        activebackground=activebackground,
        activeforeground=activeforeground,
        width=width,
        height=height,
        border=border,
        cursor=cursor
    )
    return button

def create_entry(frame, **kwargs):
    """
    Creates an entry widget with customizable properties.

    Parameters
    ----------
    frame : tkinter.Frame
        The frame in which the entry should be placed.

    **kwargs : dict, optional
        Additional keyword arguments to customize the entry.
        Supported keyword arguments include:
            - font: Tuple specifying the font (default is ("Arial", 10, "normal"))
            - background: Background color of the entry (default is white)
            - foreground: Foreground color of the entry (default is black)
            - width: Width of the entry (default is 10)
            - show: Character to be displayed in place of the input (default is None)
            - textvariable: Tkinter variable to associate with the entry (default is None)

    Returns
    -------
    entry : tkinter.Entry
        The created entry widget.
    """
    # Default values
    font = kwargs.get("font", ("Arial", 10, "normal"))
    background = kwargs.get("background", "white")
    foreground = kwargs.get("foreground", "black")
    width = kwargs.get("width", 15)
    show = kwargs.get("show", None)
    textvariable = kwargs.get("textvariable", None)

    entry = tk.Entry(
        frame,
        font=font,
        background=background,
        foreground=foreground,
        width=width,
        show=show,
        textvariable=textvariable
    )
    return entry

def create_label(frame, **kwargs):
    """
    Creates a label widget with customizable properties.

    Parameters
    ----------
    frame : tkinter.Frame
        The frame in which the label should be placed.

    **kwargs : dict, optional
        Additional keyword arguments to customize the label.
        Supported keyword arguments include:
            - text: String of the text to be displayed on the label.
            - textvariable: tkinter.StringVar to associate with the label's text.
            - font: Tuple specifying the font (default is ("Arial", 10, "bold"))
            - background: Background color of the label (default is blue)
            - foreground: Foreground color of the label (default is white)
            - width: Width of the label (default is 10)
            - height: Height of the label (default is 1)

    Returns
    -------
    label : tkinter.Label
        The created label widget.
    """
    # Default values
    text = kwargs.get("text", "")
    textvariable = kwargs.get("textvariable", None)
    font = kwargs.get("font", ("Arial", 10, "bold"))
    background = kwargs.get("background", blue)
    foreground = kwargs.get("foreground", white)
    width = kwargs.get("width", 10)
    height = kwargs.get("height", 1)

    label = tk.Label(
        frame,
        text=text,
        textvariable=textvariable,
        font=font,
        background=background,
        foreground=foreground,
        width=width,
        height=height
    )
    return label

def create_scale(frame, **kwargs):
    """
    Creates a Scale widget with customizable properties.

    Parameters
    ----------
    frame : tkinter.Frame
        The frame in which the scale should be placed.

    **kwargs : dict, optional
        Additional keyword arguments to customize the scale.
        Supported keyword arguments include:
            - from_: The starting value of the scale.
            - to: The ending value of the scale.
            - resolution: The resolution of the scale.
            - variable: The tkinter variable associated with the scale.
            - orient: Orientation of the scale ('horizontal' or 'vertical').
            - length: Length of the scale widget.
            - command: Function to be called when the scale value changes.
            - bg: Background color of the scale.
            - fg: Foreground color of the scale.

    Returns
    -------
    scale : tkinter.Scale
        The created Scale widget.
    """
    # Default values
    from_ = kwargs.get('from_', 1)
    to = kwargs.get('to', 10)
    resolution = kwargs.get('resolution', 1)
    variable = kwargs.get('variable', None)
    orient = kwargs.get('orient', 'horizontal')
    length = kwargs.get('length', 100)
    command = kwargs.get('command', None)
    bg = kwargs.get('bg', None)
    fg = kwargs.get('fg', None)

    # Create the scale widget
    scale = tk.Scale(frame, from_=from_, to=to, resolution=resolution, variable=variable,
                     orient=orient, length=length, command=command, bg=bg, fg=fg)
    return scale

def create_option_menu(frame, options, selected_option, **kwargs):
    """
    Creates an OptionMenu widget with customizable properties.

    Parameters
    ----------
    frame : tkinter.Frame
        The frame in which the OptionMenu should be placed.

    options : list
        List of options for the dropdown menu.

    selected_option : tkinter.StringVar
        Variable to store the selected option.

    command : function, optional
        Function to be called when an option is selected (default is None).

    **kwargs : dict, optional
        Additional keyword arguments to customize the OptionMenu.
        Supported keyword arguments include:
            - command : Function to be called when an option is selected (default is None).
            - font: Tuple specifying the font (default is ("Arial", 10, "bold"))
            - background: Background color of the OptionMenu (default is None)
            - foreground: Foreground color of the OptionMenu (default is None)
            - width: Width of the OptionMenu (default is None)
            - height: Height of the OptionMenu (default is None)

    Returns
    -------
    option_menu : tkinter.OptionMenu
        The created OptionMenu widget.
    """
    # Default values
    command = kwargs.get("command", None)
    font = kwargs.get("font", ("Arial", 10, "bold"))
    background = kwargs.get("background", None)
    foreground = kwargs.get("foreground", None)
    width = kwargs.get("width", None)
    height = kwargs.get("height", None)

    # Create the OptionMenu widget
    option_menu = tk.OptionMenu(frame, selected_option, *options, **kwargs)

    return option_menu

def open_calendar(root, date):
    """
    Opens a new window where you can choose a date and updates the provided date variable with the 
    chosen date.

    Parameters
    ----------
    root : tkinter.Tk or tkinter.Toplevel
        The root or top-level window where the calendar window will be opened.

    date : tkinter.StringVar
        A tkinter StringVar variable that stores the selected date.
    """


    date_window = tk.Toplevel(root)
    date_window.title("Pick a Date")

    calendar = tkcalendar.Calendar(date_window)
    calendar.pack(padx=10, pady=10)

    confirm_button = tk.Button(date_window, text="Confirm", command=lambda: select_date(date, calendar, date_window))
    confirm_button.pack(pady=10)

def select_date(date, calendar, date_window):
    """
    Updates the provided Tkinter variable with the selected date from a calendar widget.

    Parameters
    ----------
    date : tkinter.StringVar
        The Tkinter variable to be updated with the selected date.

    calendar : tkcalendar.Calendar
        The calendar widget used for selecting the date.

    date_window : tkinter.Toplevel
        The window containing the calendar widget.
    """
    selected_date = calendar.selection_get()
    date.set(selected_date)
    date_window.destroy()