import tkinter as tk
from tkinter import messagebox
from config.presets import load_presets, save_presets
from core.simconnect import SimConnectManager

class FlightRepositionApp:
    def __init__(self, root):
        self.simconnect = SimConnectManager()
        self.presets = load_presets()

        self.root = root
        self.root.title("MSFS Flight Reposition Tool")

        # Custom Input Section
        tk.Label(root, text="Latitude:").grid(row=0, column=0)
        self.lat_entry = tk.Entry(root)
        self.lat_entry.grid(row=0, column=1)

        tk.Label(root, text="Longitude:").grid(row=1, column=0)
        self.lon_entry = tk.Entry(root)
        self.lon_entry.grid(row=1, column=1)

        tk.Label(root, text="Altitude (ft):").grid(row=2, column=0)
        self.alt_entry = tk.Entry(root)
        self.alt_entry.grid(row=2, column=1)

        tk.Label(root, text="Heading (°):").grid(row=3, column=0)
        self.hdg_entry = tk.Entry(root)
        self.hdg_entry.grid(row=3, column=1)

        tk.Label(root, text="Airspeed (knots):").grid(row=4, column=0)
        self.spd_entry = tk.Entry(root)
        self.spd_entry.grid(row=4, column=1)

        tk.Button(root, text="Reposition Aircraft", command=self.reposition_aircraft).grid(row=5, column=0, columnspan=2)

        # Preset Section
        tk.Label(root, text="Presets:").grid(row=6, column=0, columnspan=2)

        self.preset_frame = tk.Frame(root)
        self.preset_frame.grid(row=7, column=0, columnspan=2)
        self.update_presets()

    def reposition_aircraft(self):
        try:
            lat = float(self.lat_entry.get())
            lon = float(self.lon_entry.get())
            alt = float(self.alt_entry.get())
            hdg = float(self.hdg_entry.get())
            spd = float(self.spd_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values.")
            return

        if not messagebox.askyesno("Confirm", "Are you sure you want to reposition the aircraft?"):
            return

        self.simconnect.connect()
        self.simconnect.reposition_aircraft(lat, lon, alt, hdg, spd)
        self.simconnect.disconnect()

    def update_presets(self):
        for widget in self.preset_frame.winfo_children():
            widget.destroy()

        for name, values in self.presets.items():
            tk.Button(self.preset_frame, text=name, command=lambda v=values: self.use_preset(v)).pack()

    def use_preset(self, values):
        lat, lon, alt, hdg, spd = values
        self.lat_entry.delete(0, tk.END)
        self.lat_entry.insert(0, lat)
        self.lon_entry.delete(0, tk.END)
        self.lon_entry.insert(0, lon)
        self.alt_entry.delete(0, tk.END)
        self.alt_entry.insert(0, alt)
        self.hdg_entry.delete(0, tk.END)
        self.hdg_entry.insert(0, hdg)
        self.spd_entry.delete(0, tk.END)
        self.spd_entry.insert(0, spd)
