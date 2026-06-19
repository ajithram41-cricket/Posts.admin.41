# 🇮🇳 Posts.admin.41 — Python Projects

A collection of Python projects including an animated Indian flag simulation and a WhatsApp automation bot.

---

## 📁 Projects

### 1. 🏳️ India Flag with Pole (`india flag with pole.py`)

An animated, waving Indian national flag rendered using **Pygame**. The flag features accurate colors, a realistic wave animation, and a detailed Ashoka Chakra with all 24 spokes.

#### ✨ Features
- Real-time waving animation using sine wave mathematics
- Accurate tricolor stripes — Saffron, White, and India Green
- Detailed **Ashoka Chakra** with 24 tapered spokes and inner hub
- 3D-styled flagpole with golden finial and wooden shading
- Smooth 60 FPS rendering
- Press `ESC` or close window to exit

#### 🖥️ Requirements
- Python 3.x
- `pygame`

#### 📦 Installation
```bash
pip install pygame
```

#### ▶️ Run
```bash
python "india flag with pole.py"
```

#### 📸 Preview
The simulation opens an 800×650 window displaying the Indian flag waving on a pole with a light grey background.

---

### 2. 💬 WhatsApp Bot (`whatsapp bot.py`)

A command-line **WhatsApp automation tool** powered by `pywhatkit`. It lets you send messages, images, and bulk messages to contacts or groups — all from your terminal.

#### ✨ Features
- Send a message to a single contact (scheduled 1 minute ahead)
- Send **bulk messages** to multiple contacts
- Send **images with captions**
- Send messages to **WhatsApp groups**
- Interactive menu-driven interface

#### 🖥️ Requirements
- Python 3.x
- `pywhatkit`
- WhatsApp Web must be **logged in** on your default browser

#### 📦 Installation
```bash
pip install pywhatkit
```

#### ▶️ Run
```bash
python "whatsapp bot.py"
```

#### 📋 Menu Options
| Option | Action |
|--------|--------|
| 1 | Send message to a single contact |
| 2 | Send bulk messages to multiple contacts |
| 3 | Send an image to a contact |
| 4 | Send a message to a group |
| 5 | Exit |

#### ⚠️ Notes
- Phone numbers must include the country code (e.g., `+919876543210` for India).
- Messages are scheduled **1 minute in the future** — keep the browser open.
- A 15-second delay is added between bulk messages to avoid issues.
- To message a group, you need the **Group ID** from WhatsApp Web.

---

## 🛠️ Tech Stack

| Library | Purpose |
|---------|---------|
| `pygame` | Graphics & animation for the flag |
| `pywhatkit` | WhatsApp Web automation |
| `datetime`, `time`, `math`, `sys` | Standard Python libraries |

---

## 📂 File Structure

```
Posts.admin.41/
├── india flag with pole.py   # Animated Indian flag using Pygame
├── whatsapp bot.py           # WhatsApp automation bot
└── README.md
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
