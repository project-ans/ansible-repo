#!/usr/bin/env python3

import os
import sys
from nextcloud import NextCloud

def upload_file(local_file_path, remote_file_path):
    NEXTCLOUD_URL = os.getenv("NEXTCLOUD_URL")
    USERNAME = os.getenv("NEXTCLOUD_USERNAME")
    PASSWORD = os.getenv("NEXTCLOUD_PASSWORD")

    # Inicjalizacja obiektu NextCloud
    nc = NextCloud(
        endpoint=NEXTCLOUD_URL,
        user=USERNAME,
        password=PASSWORD,
        session_options={"verify": True}
    )

    try:
        response = nc.upload_file(local_file_path, remote_file_path)
        if response.status_code in (200, 201, 204):
            print(f"Plik został pomyślnie przesłany: {remote_file_path}")
        else:
            print(f"Nie udało się przesłać pliku. Status: {response.status_code}")
    except Exception as e:
        print(f"Błąd podczas przesyłania pliku: {e}")

if __name__ == "__main__":
    """
    Wywołanie: python3 nextcloud_upload.py [LOCAL_FILE_PATH] [REMOTE_FILE_PATH]

    przykład:
    python3 nextcloud_upload.py /tmp/kopia.cfg Documents/kopia.cfg
    """
    if len(sys.argv) != 3:
        print("Użycie: python3 nextcloud_upload.py [sciezka_pliku_lokalnie] [sciezka_pliku_na_nextcloud]")
        sys.exit(1)

    local_file = sys.argv[1]
    remote_file = sys.argv[2]

    upload_file(local_file, remote_file)
