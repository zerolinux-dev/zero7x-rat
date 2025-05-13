import tkinter as tk
import subprocess
from tkinter import messagebox
import os

PASSWORD = "zero7x"

class Zero7xRAT:
    def __init__(self, root):
        self.root = root
        self.root.title("Zero7x RAT - Shadow Edition")
        self.root.geometry("720x600")
        self.root.config(bg="black")

        self.login_screen()

    def login_screen(self):
        self.login_frame = tk.Frame(self.root, bg="black")
        self.login_frame.pack(expand=True)

        tk.Label(self.login_frame, text="Enter Master Password", fg="red", bg="black", font=("Cebra", 18, "bold")).pack(pady=10)
        self.password_entry = tk.Entry(self.login_frame, show="*", font=("Courier", 14), width=25, bg="#222", fg="white")
        self.password_entry.pack(pady=10)
        tk.Button(self.login_frame, text="Unlock", command=self.check_password, bg="darkred", fg="white", font=("Cebra", 12)).pack(pady=10)

    def check_password(self):
        if self.password_entry.get() == PASSWORD:
            self.login_frame.destroy()
            self.build_ui()
        else:
            messagebox.showerror("Access Denied", "Wrong password. Access denied!")
            self.root.destroy()

    def build_ui(self):
        tk.Label(self.root, text="Zero7x RAT - Shadow Edition", fg="red", bg="black", font=("Cebra", 22, "bold")).pack(pady=20)
        tk.Label(self.root, text="Choose your Gate of Destruction", fg="red", bg="black", font=("Cebra", 16)).pack(pady=10)

        sections = [
            "1. Phantom Recon (Photon)",
            "2. Brute King (BruteX)",
            "3. NetReaper (Bettercap)",
            "4. Payload Factory (msfvenom)",
            "5. Dark Exploit (searchsploit)",
            "6. Social Ghost (ZPhisher)",
            "7. Zombie Injector (Venom)",
            "8. Wiper X (Hydra)"
        ]

        for i, name in enumerate(sections, 1):
            tk.Button(self.root, text=name, width=50, bg="#111", fg="white", font=("Cebra", 13, "bold"),
                      command=lambda i=i: self.activate_tool(i)).pack(pady=5)

        tk.Button(self.root, text="00. Exit to Hell", width=40, bg="darkred", fg="white", font=("Cebra", 13, "bold"),
                  command=self.root.quit).pack(pady=20)

    def activate_tool(self, number):
        messagebox.showinfo("Zero7x", f"Opening Gate {number} ...")
        method = getattr(self, f"gate_{number}", None)
        if method:
            method()
        else:
            messagebox.showerror("Error", "Tool not yet summoned!")

    def install_and_run(self, name, git_url, folder, run_cmd):
        messagebox.showinfo("Zero7x", f"Installing {name}...")
        script = f"""
        mkdir -p Tools
        cd Tools
        sudo pacman -Syu --noconfirm
        sudo pacman -S --noconfirm git python python-pip gcc make nmap hydra metasploit exploitdb bettercap
        rm -rf {folder}
        git clone {git_url}
        cd {folder}
        {run_cmd}
        """
        subprocess.call(script, shell=True)

    def gate_1(self):
        self.install_and_run("Photon", "https://github.com/s0md3v/Photon.git", "Photon",
            "python -m venv venv && source venv/bin/activate && pip install -r requirements.txt --break-system-packages && python photon.py -h")

    def gate_2(self):
        self.install_and_run("BruteX", "https://github.com/1N3/BruteX.git", "BruteX", "bash brutex")

    def gate_3(self):
        from tkinter import simpledialog
        iface = simpledialog.askstring("Network Interface", "Enter network interface (e.g. eth0, wlan0):")
        if iface:
            command = f"sudo bettercap -iface {iface}"
            subprocess.call(command, shell=True)
        else:
            messagebox.showwarning("Cancelled", "No interface provided.")

    def gate_4(self):
        subprocess.call("msfvenom -h", shell=True)

    def gate_5(self):
        subprocess.call("searchsploit", shell=True)

    def gate_6(self):
        self.install_and_run("ZPhisher", "https://github.com/htr-tech/zphisher.git", "zphisher", "bash zphisher.sh")

    def gate_7(self):
        self.install_and_run("Venom", "https://github.com/r00t-3xp10it/venom.git", "venom", "bash venom.sh")

    def gate_8(self):
        script = """
        mkdir -p Tools
        cd Tools
        sudo pacman -Syu --noconfirm
        sudo pacman -S --noconfirm git gcc make
        rm -rf thc-hydra
        git clone https://github.com/vanhauser-thc/thc-hydra.git
        cd thc-hydra
        sed -i 's/void alarming()/void alarming(int sig)/' hydra-mod.c
        ./configure && make && ./hydra
        """
        subprocess.call(script, shell=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = Zero7xRAT(root)
    root.mainloop()
