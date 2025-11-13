import os

from datetime import datetime

ROOT = os.getcwd()

def format_datetime():
    """Returns the current datetime in a format suitable for filenames."""
    return datetime.now().strftime("%Y-%m-%d_%H:%M:%S")


class Menu:

    @staticmethod
    def list_files_2_menu(root, word):
        # Folder receives 'f' for any 'f' within the root, if the join of root + f is a directory
        folders = [f for f in os.listdir(root) if not os.path.isdir(os.path.join(root, f))
                   and not f.startswith('.')
                   and not f.startswith('_')]

        print('\n')
        for i, pastas in enumerate(folders):
            print('{} - {}'.format(i, pastas))
        folder = int(input(f'\nWhich {word} do you want to do with?\n'))
        return os.path.join(root, folders[folder])


    @staticmethod
    def list_folders_2_menu(root: str) -> list[str]:
        """
         List all folders in the given root directory, excluding hidden folders
         and those starting with '_'.

         Args:
             root (str): Path to the root directory.

         Returns:
             list: List of folder names in the root directory.
         """
        return [
            folder for folder in os.listdir(root)
            if os.path.isdir(os.path.join(root, folder))
               and not folder.startswith('.')
               and not folder.startswith('_')
        ]


    @staticmethod
    def recursive_folder_navigation(path: str, word: str) -> str:
        """
        Navigate folders recursively until the user selects a directory without subdirectories
        or decides to exit.

        Args:
            path (str): Path to the root directory.
            word (str): Word to display in choice prompt.

        Returns:
            str: Path to the selected folder, or None if the user exits.
        """
        while True:
            folders = Menu.list_folders_2_menu(path)

            if not folders:
                print(f"No more subfolders in: {path}")
                return path

            print('\nAvailable folder options:\n')
            for index, folder_name in enumerate(folders):
                print(f'{index} - {folder_name}')
            print(f'{len(folders)} - Exit')

            try:
                selected_index = int(input(f'\nWhich {word} do you want to select? '))
                if selected_index == len(folders):  # Exit option
                    print("Exiting navigation.")
                    return None

                selected_folder = os.path.join(path, folders[selected_index])
                path = selected_folder  # Update root for the next iteration
            except (ValueError, IndexError):
                print("Invalid selection. Please choose a valid number.")
