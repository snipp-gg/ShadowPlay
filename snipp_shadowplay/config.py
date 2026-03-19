import os

def get_api_key():
  """Retrieve the Snipp API key from the environment or a config file."""
  key = os.getenv("SNIPP_API_KEY")
  if key:
    return key

  config_path = os.path.expanduser("~/.snipp_uploader")
  if os.path.exists(config_path):
    with open(config_path) as f:
      key = f.read().strip()
    if key:
      return key

  raise RuntimeError(
    "No API key found. Set the SNIPP_API_KEY environment variable or "
    "put your key in ~/.snipp_uploader"
  )