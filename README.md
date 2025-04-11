<p align="center">
  <a href="https://snipp.gg"><img src="https://cdn.snipp.gg/logo_light.png" alt="Snipp Logo" width="158" /></a>
</p>

# Snipp + ShadowPlay

A simple Python package that automatically uploads NVIDIA ShadowPlay clips to [Snipp](https://snipp.gg), making your gaming highlight sharing seamless.

## 🎯 Purpose

This package is built **exclusively for use with [Snipp](https://snipp.gg)**. It streamlines your workflow by automatically uploading your clips and copying shareable links to your clipboard.

## 🚀 Features

- Monitors your ShadowPlay video folder for new clips
- Uploads clips to Snipp via the Snipp API
- Copies the shareable URL to your clipboard automatically

## ⚙️ Requirements

- Python 3.8 or higher
- NVIDIA ShadowPlay (with local clip saving enabled)
- A valid API key from [Snipp Console](https://snipp.gg/settings/console)

Dependencies (automatically installed with the package):
- `requests`
- `pyperclip`
- `watchdog`
- `colorama`

## 💪 Installation

```bash
pip install snipp
```

## 🔐 Configuration

1. **Get your API Key**  
   Visit the [Snipp Console](https://snipp.gg/settings/console) and generate a key.

2. **Set your API Key**  
   Either:
   - Export it as an environment variable:
     ```bash
     export SNIPP_API_KEY=your-api-key
     ```
   - Or save it to a file:
     ```bash
     echo "your-api-key" > ~/.snipp_uploader
     ```

## ▶️ Usage

Once installed and configured, run:

```bash
snipp-shadowplay
```

The script will start watching your `~/Videos` folder and upload new `.mp4` files automatically.

## ✅ Usage Policy

- This package is **authorised solely for use with Snipp**.
- **Do not modify it to interact with other services**. Violations may lead to API key revocation or account suspension.

## 🤝 Contributing

We welcome suggestions and improvements for better integration with Snipp:

- Open an issue
- Submit a pull request that adheres to our [Terms of Service](https://snipp.gg/terms)

## 📄 Licence

MIT Licence © 2025 Snipp. See [LICENCE](LICENCE) for full details.

## ⚠️ Disclaimer

This package is provided "as is" and only for use with [Snipp](https://snipp.gg). Users must adhere to the [Terms of Service](https://snipp.gg/terms).