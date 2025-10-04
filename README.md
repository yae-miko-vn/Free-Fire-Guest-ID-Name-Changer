# Guest ID Name Changer

A Python script for automatically changing guest account nicknames in bulk using an asynchronous approach for efficiency.

## 📋 Overview

This tool allows you to:
- Load guest account credentials from a JSON file
- Generate random nicknames with a customizable base name
- Change account names in bulk with concurrent requests
- Handle errors and timeouts gracefully

## 🚀 Features

- **Asynchronous Processing**: Handles multiple requests concurrently for faster execution
- **Customizable Naming**: Generate nicknames with your preferred base name
- **Error Handling**: Comprehensive error reporting for failed requests
- **Configurable Limits**: Adjust concurrent connections and timeout settings
- **Simple Setup**: Easy configuration through environment variables and JSON files

## 📁 Project Structure

```
guest-name-changer/
├── Guest_ID_Name_Changer.py  # Main script
├── guest-accounts.json       # Account credentials storage
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd guest-name-changer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🔧 Configuration

### 1. Account Setup
Edit `guest-accounts.json` to include your guest accounts:
```json
[
    {
        "uid": "4038272419",
        "password": "A82E0644DF741410E73E2AFA5AD1013F96B414A137C9932DF14D72BB87E6A479"
    }
]
```

### 2. Script Configuration
Modify the constants in `Guest_ID_Name_Changer.py`:
```python
NICKNAME_BASE = "Inazuma"      # Your preferred base name
MAX_CONCURRENT = 10            # Maximum concurrent requests
TIMEOUT_SECONDS = 15           # Request timeout in seconds
API_URL = "http://changenamedat.onrender.com/change"  # API endpoint
```

## 🎯 Usage

Run the script with:
```bash
python Guest_ID_Name_Changer.py
```

### Expected Output
```
[1] ✅ New Nickname: Inazuma_AbC123 (Status: 200)
[2] ❌ ERROR for UID 3908830790 - Message: Invalid credentials
[3] ❌ Timeout for UID 4038272419
```

## 📊 Configuration Options

| Variable | Default | Description |
|----------|---------|-------------|
| `NICKNAME_BASE` | "Inazuma" | Base name for generated nicknames |
| `MAX_CONCURRENT` | 10 | Maximum simultaneous API requests |
| `TIMEOUT_SECONDS` | 15 | Request timeout duration |
| `ACCOUNTS_FILE` | "guest-accounts.json" | Path to account credentials file |

## 🔒 Security Notes

- Keep your `guest-accounts.json` file secure
- The script uses HTTPS for API communication
- Passwords are stored as hashes in the JSON file

## 🐛 Troubleshooting

**Common Issues:**
- `FileNotFoundError`: Ensure `guest-accounts.json` exists in the same directory
- `ImportError`: Run `pip install -r requirements.txt` to install dependencies
- Timeout errors: Increase `TIMEOUT_SECONDS` or check your internet connection

## 📝 License

This project is provided for educational purposes. Please use responsibly and in accordance with the terms of service of the platform you're interacting with.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

---

**Note**: Make sure you have proper authorization to modify the accounts you're working with. Use this tool responsibly and in compliance with all applicable terms of service.
