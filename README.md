# snipp-shadowplay

A Python package that automatically uploads [NVIDIA ShadowPlay](https://www.nvidia.com/en-ph/geforce/geforce-experience/shadowplay/) clips to [Snipp](https://snipp.gg).

## Features

- Monitors your ShadowPlay video folder for new clips
- Uploads clips to Snipp via the API
- Copies the shareable URL to your clipboard automatically

## Requirements

- Python 3.9 or higher
- NVIDIA ShadowPlay (with clip saving enabled)
- A valid API key from the [Snipp Console](https://snipp.gg/settings/console)

Dependencies (automatically installed):
- `requests`
- `pyperclip`
- `watchdog`
- `colorama`

## Installation

```bash
pip install snipp-shadowplay
```

## Configuration

1. **Get your API Key:**
   Visit the [Snipp Console](https://snipp.gg/settings/console) and generate a key.

2. **Set your API Key:**
   Set your API key as an environment variable:
   ```cmd
   setx SNIPP_API_KEY YOUR_API_KEY
   ```

   Or save it to a config file at `~/.snipp_uploader`.

## Quick Start

Once installed and configured, run:

```cmd
snipp
```

The script will start watching your `~/Videos` folder and upload new `.mp4` files automatically. Shareable URLs are copied to your clipboard on each successful upload.

## Error Handling

- Files exceeding 1 GB are skipped automatically
- Upload errors are logged with status codes and messages
- The watcher waits for clips to finish saving before uploading

## Contributing

We welcome suggestions and improvements:

- Open an issue
- Submit a pull request that adheres to our [Terms of Service](https://snipp.gg/terms) and [Privacy Policy](https://snipp.gg/privacy)

## Usage Policy

This package is authorised solely for use with Snipp. Do not modify it to interact with other services. Violations may lead to API key revocation or account suspension.

## License

MIT License © 2026 Snipp. See [LICENCE](LICENCE) for full details.