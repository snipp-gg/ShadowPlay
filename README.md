# Snipp + ShadowPlay

A simple Python package that automatically uploads [NVIDIA ShadowPlay](https://www.nvidia.com/en-ph/geforce/geforce-experience/shadowplay/) clips to [Snipp](https://snipp.gg), making your gaming highlight sharing seamless.

## 🎯 Purpose

This package is built **exclusively for use with [Snipp](https://snipp.gg)**. It automatically uploads your clips and copies shareable links to your clipboard. This package is designed to be used with [NVIDIA ShadowPlay](https://www.nvidia.com/en-ph/geforce/geforce-experience/shadowplay/).

## 🚀 Features

- Monitors your ShadowPlay video folder for new clips
- Uploads clips to Snipp via the API
- Copies the shareable URL to your clipboard automatically

## ⚙️ Requirements

- Python 3.8 or higher (preferably not the Microsoft Store version)
- NVIDIA ShadowPlay (with clip saving enabled)
- A valid API key from the [Snipp Console](https://snipp.gg/settings/console)

Dependencies (automatically installed with the package):
- `requests`
- `pyperclip`
- `watchdog`
- `colorama`

## 💪 Installation

```cmd
pip install snipp
```

## 🔐 Configuration

1. **Get your API Key:**  
   Visit the [Snipp Console](https://snipp.gg/settings/console) and generate a key.

2. **Set your API Key:**  
   Set your API Key as an environment variable in **Command Prompt** or **PowerShell** as an **Administrator**:
    ```cmd
    setx SNIPP_API_KEY YOUR_API_KEY
    ```

## ▶️ Usage

Once installed and configured, run:

```cmd
snipp
```

The script will start watching your `~/Videos` folder and upload new `.mp4` files automatically.

## ✅ Usage Policy

- This package is **authorised solely for use with Snipp**.
- **Do not modify it to interact with other services**. Violations may lead to API key revocation or account suspension.

## 🤝 Contributing

We welcome suggestions and improvements for better integration with Snipp:

- Open an issue
- Submit a pull request that adheres to our [Terms of Service](https://snipp.gg/terms) and [Privacy Policy](https://snipp.gg/privacy)

## 📄 Licence

MIT Licence © 2025 Snipp. See [LICENCE](LICENCE) for full details.

## ⚠️ Disclaimer

This package is provided "as is" and only for use with [Snipp](https://snipp.gg). Users must adhere to the [Terms of Service](https://snipp.gg/terms) and the [Privacy Policy](https://snipp.gg/privacy).