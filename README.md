
# InvisoGuard Reverse Video Identity Tracing (With Precompiled dlib)

## Deployment Instructions (for Render or Local)

This package uses `dlib` for face recognition. Render deployment fails when building `dlib` from source.
To avoid that, use a precompiled `.whl` version of `dlib`:

### ✅ Install Precompiled dlib (Python 3.11 + Linux x86_64)
Download compatible `.whl` from:
https://github.com/RPi-Distro/python-dlib/releases

Then install manually via pip:
```
pip install dlib-19.24.0-cp311-cp311-manylinux_2_17_x86_64.whl
```

### 📦 Then install the rest normally:
```
pip install -r requirements.txt
```

## Run the App
```
python app.py
```

## Includes:
- Live face detection (OpenCV + dlib)
- Placeholder iris scan logic
- Simulated trace metadata (GPS, device ID, timestamp)
- Full UI with Admin / Authority roles
- PDF generation and trace voucher receipt
- Responsive, mobile-ready pages
