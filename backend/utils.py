
# UTILITY MODULE
# 1. PDF + JSON Export
# 2. Google Maps & Street View rendering
# 3. Token deduction & user auth simulation

import json
from reportlab.pdfgen import canvas

def export_trace_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f)

def export_trace_pdf(data, path):
    c = canvas.Canvas(path)
    c.drawString(100, 750, "InvisoGuard Trace Report")
    for i, (k, v) in enumerate(data.items()):
        c.drawString(100, 730 - 20*i, f"{k}: {v}")
    c.save()

def simulate_token_deduction(current_tokens):
    return max(0, current_tokens - 1)
