import os
import time
from colorama import Fore, Style

def wait_for_file_completion(file_path, timeout=60, interval=0.5, stable_checks=3):
  """Wait for a file to finish being written to disk.

  Waits until the file size remains stable for ``stable_checks`` consecutive
  checks spaced ``interval`` seconds apart, or until ``timeout`` seconds have
  elapsed.
  """
  start_time = time.time()
  last_size = -1
  stable_count = 0

  print(f"{Fore.LIGHTYELLOW_EX}[INFO] Waiting for clip to finish saving...{Style.RESET_ALL}")

  while time.time() - start_time < timeout:
    if not os.access(file_path, os.R_OK):
      time.sleep(interval)
      continue

    current_size = os.path.getsize(file_path)
    if current_size > 0 and current_size == last_size:
      stable_count += 1
      if stable_count >= stable_checks:
        return True
    else:
      stable_count = 0

    last_size = current_size
    time.sleep(interval)

  return False