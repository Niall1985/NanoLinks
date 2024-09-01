# NanoLinks

**NanoLinks** is a simple URL shortener built with Python and Flask. It allows users to shorten long URLs and provides a shortened URL that redirects to the original link.

## Features

- Shortens long URLs into shorter, manageable links
- Simple and user-friendly interface

## Requirements

- Python 3.x
- Flask

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/shortsnap.git
   cd shortsnap
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install Flask
   ```

## Usage

1. **Run the Flask Application**

   ```bash
   python main.py
   ```

   The server will start, and you can access the application at `http://localhost:5000`.

2. **Shorten a URL**

   - Open your browser and go to `http://localhost:5000`.
   - Enter the long URL in the form and click "Shorten".

3. **Access Shortened URL**

   - The application will display a shortened URL. Click on it or copy-paste it into your browser to be redirected to the original URL.

## Code Structure

- `main.py`: The main Flask application file that handles URL shortening and redirection.
- `templates/index.html`: The HTML template for the user interface.

## License

This project is licensed under the [GNU General Public License (GPL) v3.0](https://www.gnu.org/licenses/gpl-3.0.html). See the [LICENSE](LICENSE) file for details.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. For any issues or feature requests, please open an issue on the GitHub repository.

## Acknowledgements

- Flask for the web framework
- Python for the programming language


