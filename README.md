# Windows Fix Scripts

Simple **Batch** utilities to quickly resolve common Windows hiccups — without a full reboot.  
Includes fixes for **Quick Settings / Explorer**, **Windows Audio**, and **Bluetooth**.

> ⚠️ **Safety & Admin**
> - Read the code before running. Use at your own risk.
> - Some scripts require **Administrator** privileges (they will ask for elevation).

---

## ✨ Scripts

| Script | Fixes | Requires Admin | How to run |
| --- | --- | --- | --- |
| `Fix-Quick-Settings.bat` | Restarts `explorer.exe` to solve Quick Settings/Taskbar/Start glitches. | No | Double-click or run in a normal terminal. |
| `Restart-Audio.bat` | Restarts **Windows Audio** services to fix sound issues (muted/no device). | Yes | Run from an **elevated** terminal or right-click → “Run as administrator”. |
| `Reset-Bluetooth.bat` | Disables/enables Bluetooth adapter to recover from pairing/driver problems. | Yes | Run from an **elevated** terminal or right-click → “Run as administrator”. |

---

## 📦 Download

- **Source code**: clone this repo.  
- **Ready-to-run ZIP**: see Releases (contains only the `/scripts` folder).

---

## 🚀 Usage

### 1) Fix Quick Settings / Explorer
```bat
:: Double-click or:
scripts\Fix-Quick-Settings.bat
```
What it does:
- Kills `explorer.exe`
- Relaunches the shell
- **Note:** File Explorer windows will restart fresh.

### 2) Restart Windows Audio
```bat
:: Requires elevated terminal (Run as administrator)
scripts\Restart-Audio.bat
```
What it does:
- Stops & starts `Windows Audio` (and related) services
- Restores audio without reboot when devices vanish or hang

### 3) Reset Bluetooth Adapter
```bat
:: Requires elevated terminal (Run as administrator)
scripts\Reset-Bluetooth.bat
```
What it does:
- Disables/enables the Bluetooth adapter via system tools
- **Note:** You may need to re-pair devices in edge cases.

---

## 🛠 Tech

- Windows **Batch (.bat)**
- Tested on Windows 10/11

## 🔒 Permissions

- Only `Restart-Audio` and `Reset-Bluetooth` need admin rights.
- Scripts do **not** change system policies or registry (beyond service/device restart).

## 🧾 License

MIT — see `LICENSE`.

## 🙌 Author

- Tiago Roque — [LinkedIn](linkedin.com/in/tiagodcroque) • [GitHub](https://github.com/tiagoroque3)
