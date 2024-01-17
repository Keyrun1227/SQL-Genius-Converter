# SQL-Genius-Converter🤖💬

SQL-Genius-Converter Chat Interface is a Flask web application that allows users to interact with a text-to-SQL model through a chat interface. The application sends user-provided natural language queries to an external text-to-SQL API, converts them into SQL queries, and displays the conversation history.

## How It Works 🚀

1. **User Interaction:**
   - Users type queries into the chat input area.
   - Clicking the "Send" button sends the query to the server.

2. **Server Processing:**
   - Flask server handles incoming requests.
   - User's query is sent to an external text-to-SQL API.
   - API processes the query and returns a SQL response.

3. **Display Results:**
   - User's query and API's SQL response are displayed in the chat history.
   - Chat history supports both user and bot messages.

## Technologies Used 🛠️

- **Flask:** Web application framework for handling HTTP requests.
- **JavaScript:** Used for asynchronous communication and dynamic content.
- **Bootstrap:** CSS framework for styling the user interface.

## Project Structure 📂

- **`app.py`:** Flask application handling routes and communication with the external API.
- **`index.html`:** HTML template defining the structure of the chat interface.
- **`styles.css`:** Custom styles for the application.

## How to Run 🏃

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Keyrun1227/SQL-Genius-Converter.git 
   cd SQL-Genius-Converter  
   ```
2. **Install Dependencies:**
    ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application:**
    ```bash
   python app.py
   ```
## Themes 🌈

- The application supports both light and dark themes.
- Toggle between themes using the "Toggle Theme" button in the navigation bar.

## External Text2SQL API 🌐

- The application assumes interaction with an external API at: [https://toolske.com/text2sql/php/generatesql.php](https://toolske.com/text2sql/php/generatesql.php).
- Ensure proper API connectivity for accurate functionality.

## Notes and Acknowledgments 📝

- Error handling is implemented for API requests.
- Contributions, feedback, and bug reports are welcome.
- Special thanks to the developers of Flask, Bootstrap, and the external Text2SQL API.

Happy Developing! 🤗🚀
