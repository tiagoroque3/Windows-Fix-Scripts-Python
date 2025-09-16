# Windows Fix Scripts (Python)

This repository contains **Python utility scripts** to quickly fix common Windows issues related to audio, Bluetooth, and Quick Settings.

## Included Scripts

- **`fix_quick_settings.py`**  
  Restarts `explorer.exe` to resolve occasional glitches with Windows Quick Settings.

- **`restart_audio_services.py`**  
  Restarts the audio services (`AudioEndpointBuilder` and `Audiosrv`) when sound stops working.

- **`reset_bluetooth_devices.py`**  
  Disables and removes Bluetooth devices via PowerShell and triggers a new device scan with `pnputil`.

---

## Requirements

- **Python 3.7+** installed on Windows  
- **Administrator privileges** (scripts will auto-elevate if needed)  
- **PowerShell** (pre-installed on Windows 10/11)  
- For the Bluetooth script: support for `Get-PnpDevice`, `Disable-PnpDevice`, `Remove-PnpDevice` cmdlets

---

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/tiagoroque3/Windows-Fix-Scripts-Python.git
   cd Windows-Fix-Scripts-Python
   ```

2. Run the desired script:
   ```bash
   python fix_quick_settings.py
   python restart_audio_services.py
   python reset_bluetooth_devices.py
   ```

⚠️ **Note:** All scripts require administrator privileges. If run without, they will request elevation automatically.

---

## Motivation

These scripts were created to quickly solve common Windows problems without rebooting the system. Originally written in **Batch (.bat)**, they were rewritten in **Python** for better flexibility and readability.

---

## License

This project is distributed under the MIT License.  
Feel free to use, modify, and share.
