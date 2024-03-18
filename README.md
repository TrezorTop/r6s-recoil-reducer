Sure, here's a basic README for your project:

```markdown
# Recoil Reducer

Recoil Reducer is a Python application that helps you manage recoil in shooter games. It uses the win32api for mouse manipulations.

## Prerequisites

- Python 3.10
- pip

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/TrezorTop/R6S-recoil-reducer.git
```

Navigate to the project directory:

```bash
cd R6S-recoil-reducer
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Building

To build the application, run the following command:

```bash
python -m PyInstaller --onefile --hidden-import=pywintypes --add-data="./settings;settings" main.py
```

The built application will be in the `dist` folder.

## Usage

Start the application by running the executable in the `dist` folder.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
