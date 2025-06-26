How to Add ESP32 Support to Arduino IDE**

1. Launch the **Arduino IDE** on your system.
2. Navigate to **File > Preferences**.
3. In the **“Additional Board Manager URLs”** field, paste this link:
   `https://dl.espressif.com/dl/package_esp32_index.json`
4. Click **OK** to save the changes.
5. Now go to **Tools > Board > Boards Manager**.
6. Type **ESP32** in the search bar, then install **“ESP32 by Espressif Systems”**.
7. Wait for the installation to finish.
8. From **Tools > Board**, select the appropriate ESP32 board you’re using.
9. Plug your ESP32 into the PC via USB cable.
10. Under **Tools > Port**, select the right COM port.
11. That’s it! Now you’re all set to write and upload code to your ESP32 board.
