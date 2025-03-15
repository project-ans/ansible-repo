import os
import sys
from nextcloud_client import Client

# Pobranie zmiennych środowiskowych
NEXTCLOUD_URL = os.getenv("NEXTCLOUD_URL")
NEXTCLOUD_USERNAME = os.getenv("NEXTCLOUD_USERNAME")
NEXTCLOUD_PASSWORD = os.getenv("NEXTCLOUD_PASSWORD")

# Sprawdzenie argumentów
if len(sys.argv) != 2:
    print("Usage: python3 upload_to_nextcloud.py <backup_file>")
    sys.exit(1)

backup_file = sys.argv[1]
filename = os.path.basename(backup_file)

# Połączenie z Nextcloud
nc = Client(NEXTCLOUD_URL)
nc.login(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD)

# Sprawdzenie folderu "backups"
backup_folder = "/backups/"
if not nc.file_exists(backup_folder):
    nc.mkdir(backup_folder)

# Przesyłanie pliku na Nextcloud
remote_path = f"{backup_folder}{filename}"
nc.put_file(remote_path, backup_file)

print(f"Backup {filename} uploaded successfully to Nextcloud at {remote_path}")
