# CSV Analysis Assistant

A Streamlit application that allows users to upload CSV files and ask analytical questions about their data using AI-powered analysis.

## Features

- Upload and analyze CSV files
- Ask natural language questions about your data
- Get AI-powered insights and analysis
- User-friendly interface
- Robust error handling

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file:
```bash
cp .env.example .env
```

5. Edit the `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
MODEL_NAME=gpt-3.5-turbo
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run src/app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

3. Upload a CSV file and start asking questions about your data!

## Project Structure

```
.
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── src/
    ├── app.py
    └── agent.py
```

- `src/app.py`: Main Streamlit application
- `src/agent.py`: CSV analysis agent implementation
- `requirements.txt`: Python dependencies
- `.env.example`: Example environment configuration

## Deployment

### Local Development
1. Follow the installation instructions above
2. Run the application using `streamlit run src/app.py`

### GitHub Deployment
1. Create a new repository on GitHub
2. Initialize git in your local project:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
3. Link your local repository to GitHub:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

### Continuous Integration
The project includes a GitHub Actions workflow that:
- Runs on push to main branch and pull requests
- Tests the application with Python 3.8
- Performs linting checks using flake8

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Streamlit for the web framework
- LangChain for the AI agent implementation
- OpenAI for the language model 