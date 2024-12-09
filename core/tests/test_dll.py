import ctypes
import os

dll_path = '/Users/hamstray/MSFS-Plugin/pysimconnect/simconnect/SimConnect.dll'
print(f"Attempting to load DLL from: {dll_path}")

try:
    dll = ctypes.WinDLL(dll_path)
    print("DLL loaded successfully")
except Exception as e:
    print(f"Failed to load DLL: {e}")
