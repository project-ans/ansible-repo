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
