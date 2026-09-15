"""Verify a downloaded public release without third-party Python packages."""
from pathlib import Path
import hashlib, csv, sys, zipfile
archive = Path(sys.argv[1] if len(sys.argv) > 1 else 'pages2k-audit-site.zip')
expected = 'db1f4a61685207f1641d1dd0f6b6bcf0060ca5e9b71627ff1217496959eb3352'
actual = hashlib.file_digest(archive.open('rb'), 'sha256').hexdigest()
assert actual == expected, f'Archive hash mismatch: {actual}'
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None, 'ZIP CRC failure'
    rows = list(csv.DictReader(z.read('PUBLICATION_MANIFEST.csv').decode().splitlines()))
    for row in rows:
        data = z.read(row['path'])
        assert len(data) == int(row['bytes']), row['path']
        assert hashlib.sha256(data).hexdigest() == row['sha256'], row['path']
print(f'PASS: archive SHA256, ZIP CRC and {len(rows)} manifest entries.')
