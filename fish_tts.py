"""
Fish Audio TTS Generator
Stimme einmal setzen, Text eingeben, MP3 generieren.
"""

import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os
import requests
import threading
from datetime import datetime

# When frozen as .exe, use the folder next to the exe — not inside it
if getattr(sys, "frozen", False):
    _BASE = os.path.dirname(sys.executable)
else:
    _BASE = os.path.dirname(os.path.abspath(__file__))

CONFIG_FILE = os.path.join(_BASE, "config.json")
OUTPUT_DIR  = os.path.join(_BASE, "output")
API_URL     = "https://api.fish.audio/v1/tts"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ── Config laden/speichern ─────────────────────────────────────────────────────

def load_config() -> dict:
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"api_key": "", "voice_id": "", "bitrate": 128}


def save_config(cfg: dict):
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=2)


# ── API ────────────────────────────────────────────────────────────────────────

def generate_mp3(api_key: str, voice_id: str, text: str, bitrate: int) -> bytes:
    r = requests.post(
        API_URL,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={"text": text, "reference_id": voice_id, "format": "mp3", "mp3_bitrate": bitrate},
        timeout=30,
    )
    r.raise_for_status()
    return r.content


# ── GUI ────────────────────────────────────────────────────────────────────────

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fish Audio TTS")
        self.resizable(False, False)
        self.configure(bg="#1e1e2e")

        self.cfg = load_config()
        self._build_ui()

    def _build_ui(self):
        PAD = dict(padx=12, pady=6)
        BG  = "#1e1e2e"
        FG  = "#cdd6f4"
        ENTRY_BG = "#313244"
        ACC  = "#89b4fa"
        BTN  = "#45475a"

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TLabel",      background=BG, foreground=FG, font=("Segoe UI", 10))
        style.configure("TEntry",      fieldbackground=ENTRY_BG, foreground=FG, insertcolor=FG)
        style.configure("Accent.TButton", background=ACC, foreground="#1e1e2e",
                        font=("Segoe UI", 10, "bold"))
        style.map("Accent.TButton", background=[("active", "#74c7ec")])
        style.configure("TButton",     background=BTN, foreground=FG, font=("Segoe UI", 9))
        style.map("TButton",           background=[("active", "#585b70")])

        # ── API Key ──
        f1 = tk.Frame(self, bg=BG)
        f1.pack(fill="x", **PAD)
        ttk.Label(f1, text="Fish Audio API Key").pack(anchor="w")
        self.api_key_var = tk.StringVar(value=self.cfg.get("api_key", ""))
        e_key = ttk.Entry(f1, textvariable=self.api_key_var, width=52, show="•")
        e_key.pack(fill="x", pady=(2, 0))
        e_key.bind("<FocusOut>", lambda _: self._save_settings())

        # ── Voice ID ──
        f2 = tk.Frame(self, bg=BG)
        f2.pack(fill="x", **PAD)
        ttk.Label(f2, text="Voice ID (Fish Audio Reference ID)").pack(anchor="w")
        row = tk.Frame(f2, bg=BG)
        row.pack(fill="x", pady=(2, 0))
        self.voice_id_var = tk.StringVar(value=self.cfg.get("voice_id", ""))
        ttk.Entry(row, textvariable=self.voice_id_var, width=44).pack(side="left")
        ttk.Button(row, text="💾 Speichern", command=self._save_settings).pack(side="left", padx=(6, 0))

        # ── Text ──
        f3 = tk.Frame(self, bg=BG)
        f3.pack(fill="x", **PAD)
        ttk.Label(f3, text="Text").pack(anchor="w")
        self.text_box = tk.Text(
            f3, height=6, width=52,
            bg=ENTRY_BG, fg=FG, insertbackground=FG,
            relief="flat", font=("Segoe UI", 10),
            wrap="word", padx=6, pady=6,
        )
        self.text_box.pack(fill="x", pady=(2, 0))

        # ── Buttons ──
        f4 = tk.Frame(self, bg=BG)
        f4.pack(fill="x", **PAD)
        self.gen_btn = ttk.Button(
            f4, text="🎵 MP3 Generieren", style="Accent.TButton",
            command=self._generate,
        )
        self.gen_btn.pack(side="left")
        self.open_btn = ttk.Button(
            f4, text="📁 Output-Ordner", command=self._open_output,
        )
        self.open_btn.pack(side="left", padx=(8, 0))

        # ── Status ──
        self.status_var = tk.StringVar(value="Bereit.")
        tk.Label(self, textvariable=self.status_var,
                 bg=BG, fg="#a6e3a1",
                 font=("Segoe UI", 9), anchor="w").pack(fill="x", padx=12, pady=(0, 4))

        # ── Ko-fi ──
        kofi = tk.Label(self, text="☕ Support on Ko-fi", bg=BG, fg="#f38ba8",
                        font=("Segoe UI", 9, "underline"), cursor="hand2", anchor="w")
        kofi.pack(fill="x", padx=12, pady=(0, 10))
        kofi.bind("<Button-1>", lambda _: __import__("webbrowser").open("https://ko-fi.com/mikshade"))

    def _save_settings(self):
        self.cfg["api_key"]  = self.api_key_var.get().strip()
        self.cfg["voice_id"] = self.voice_id_var.get().strip()
        save_config(self.cfg)
        self.status_var.set("✅ Einstellungen gespeichert.")

    def _open_output(self):
        os.startfile(OUTPUT_DIR)

    def _generate(self):
        api_key  = self.api_key_var.get().strip()
        voice_id = self.voice_id_var.get().strip()
        text     = self.text_box.get("1.0", "end").strip()

        if not api_key:
            messagebox.showerror("Fehler", "Bitte API Key eingeben.")
            return
        if not voice_id:
            messagebox.showerror("Fehler", "Bitte Voice ID eingeben.")
            return
        if not text:
            messagebox.showerror("Fehler", "Bitte Text eingeben.")
            return

        self.gen_btn.config(state="disabled")
        self.status_var.set("⏳ Generiere MP3…")
        self.update()

        def worker():
            try:
                mp3 = generate_mp3(api_key, voice_id, text, self.cfg.get("bitrate", 128))
                ts  = datetime.now().strftime("%Y%m%d_%H%M%S")
                out = os.path.join(OUTPUT_DIR, f"tts_{ts}.mp3")
                with open(out, "wb") as f:
                    f.write(mp3)
                self.after(0, lambda: self._done(out, mp3))
            except Exception as e:
                self.after(0, lambda: self._error(str(e)))

        threading.Thread(target=worker, daemon=True).start()

    def _done(self, path: str, _mp3=None):
        self.gen_btn.config(state="normal")
        self.status_var.set(f"✅ Gespeichert: {os.path.basename(path)}")

    def _error(self, msg: str):
        self.gen_btn.config(state="normal")
        self.status_var.set(f"❌ Fehler: {msg}")
        messagebox.showerror("API Fehler", msg)


if __name__ == "__main__":
    App().mainloop()
