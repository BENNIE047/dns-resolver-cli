# 🌐 DNS Resolver CLI

A simple and lightweight command-line tool to resolve website domain names to their IP addresses.

## 📖 Overview

DNS Resolver CLI is a Python-based utility that allows you to quickly look up the IP address of any website. It uses Python's built-in `socket` library to perform DNS resolution and provides a clean, user-friendly interface.

## ✨ Features

- 🔍 Quick DNS resolution for any domain
- 🧹 Automatic input cleaning (removes `http://`, `https://`, and `www.`)
- ✅ Clear success/error messaging
- 🚀 No external dependencies required
- 💻 Cross-platform compatibility (Windows, macOS, Linux)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/BENNIE047/dns-resolver-cli.git
   cd dns-resolver-cli
   ```

2. **Ensure Python is installed:**
   This tool requires Python 3.x. Check your Python version:
   ```bash
   python --version
   ```

## 🚀 Usage

Run the script from your terminal:

```bash
python dns_resolver.py
```

### Example Session

```
🌐 WEBSITE TO IP ADDRESS RESOLVER
----------------------------------
Enter a website name (e.g., google.com): google.com
✅ The IP address of google.com is: 142.250.185.46
```

### Input Formats Supported

The tool accepts domains in various formats:
- `google.com`
- `www.google.com`
- `https://google.com`
- `http://www.google.com`

All formats are automatically cleaned and processed correctly.

## 📝 How It Works

1. **Input Cleaning**: Removes common URL prefixes (`http://`, `https://`, `www.`)
2. **DNS Lookup**: Uses Python's `socket.gethostbyname()` to resolve the domain
3. **Result Display**: Shows the IP address or an error message if resolution fails

## 🔧 Code Structure

```python
get_ip_address(hostname)  # Performs DNS lookup
clean_input(user_input)   # Sanitizes user input
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**BENNIE047**
- GitHub: [@BENNIE047](https://github.com/BENNIE047)

## 🙏 Acknowledgments

- Built with Python's standard library
- Inspired by the need for quick DNS lookups

## 📞 Support

If you encounter any issues or have questions, please [open an issue](https://github.com/BENNIE047/dns-resolver-cli/issues) on GitHub.

---

⭐ If you find this tool helpful, please consider giving it a star!
