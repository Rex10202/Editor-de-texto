# Text Editor with Tkinter
This project is a simple text editor application created using the Tkinter library in Python. It provides basic text editor functionalities, such as opening, saving, and saving files with different names, along with a prompt to save unsaved changes before closing the application.

# Features
- Open files: Allows the user to open existing text files.
- Save files: Allows the user to save the current file.
- Save as: Allows the user to save the current file with a new name or location.
- Exit: Allows the user to exit the application, with a prompt if there are unsaved changes.

# Requirements
- Python 3.x
- Tkinter (usually included in the standard Python installation)

# Functionality Description
# Initialization
- Title and configuration: The main window of the text editor has the title "Text Editor" and is configured to have a minimum size of 600x600 pixels.
- Text area: A Tkinter text widget is used to display and edit the content of the file.

# Menu
- File Menu: Contains options to open, save, save as, and exit the application.
- Open: Allows the user to select and open an existing text file.
- Save: Saves the current content to the opened file.
- Save as: Allows the user to save the current content to a new file.
- Exit: Closes the application, prompting the user to save changes if there are unsaved modifications.

# File Management
- Opening files: When a file is opened, its content is loaded into the text area, replacing any existing content.
- Saving files: Saves the content of the text area to the current file. If there is no file opened, it prompts the user to select a location and name to save the file.

# Closing Prompt
- Change detection: Before closing the application, it checks if there are unsaved changes in the file content.
- Warning dialog: If there are unsaved changes, it displays a warning to the user with options to save, not save, or cancel the closing.

# Additional Notes
- The main window and the text area automatically adjust to fill the available space.
- The text area is configured to wrap words instead of breaking lines of text in half.
- The application uses standard Tkinter file dialogs for opening and saving files, providing a familiar user experience.
