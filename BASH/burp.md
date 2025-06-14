## **Burp Suite Loader Setup on Kali Linux**

### **Run from Terminal**

To start Burp Suite Loader from the terminal:

```bash
java -jar /home/kali/BurpSuitePro/BurpLoader.jar
```



###  **Create a Desktop Shortcut (Launcher)**

To launch Burp Suite from your application menu:

1. **Open a terminal** and run:

   ```bash
   nano ~/.local/share/applications/burp-loader.desktop
   ```

2. **Paste the following content:**

   ```ini
   [Desktop Entry]
   Name=BurpSuite Loader
   Exec=java -jar /home/kali/BurpSuitePro/BurpLoader.jar
   Icon=utilities-terminal
   Terminal=true
   Type=Application
   Categories=Utility;
   ```

3. **Optional Customizations:**

   * Set `Terminal=false` if you don’t want it to open in a terminal window.
   * Replace `Icon=utilities-terminal` with a path to a custom icon, e.g.:

     ```ini
     Icon=/home/kali/BurpSuitePro/burp.png
     ```


4. **Make the shortcut executable:**

   ```bash
   chmod +x ~/.local/share/applications/burp-loader.desktop
   ```

Your shortcut will now appear in your application menu as **“BurpSuite Loader”**.

