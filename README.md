# mod-pword-gen

A modular command-line password generator and profile vault, written in Python.

> **Status: work in progress.** Core generation works; viewing/editing the vault and saving to disk are still being built.

## What it does

Passwords are built from **blocks** that you can rearrange. Each block is either a few random characters or a word drawn from a word list. The current default order is:

```
[2 hex chars] + [English word, 6–8 letters] + [2 digits] + [1 symbol]
e.g.  a3building27!
```

After generating a password you can regenerate it or keep it. If you keep it, you attach it to a **profile** (account, username, tags). The profile can be new or one that already exists.

## Features

- **Secure randomness**: everything is chosen with Python's `secrets` module, not `random`
- **Modular blocks**: character generators in `gen_functions.py`:
  | Function | Characters |
  |---|---|
  | `gen_hexadec` | Hexadecimal (`0-9a-fA-F`) |
  | `gen_hexacosa` | Letters + digits |
  | `gen_num` | Digits |
  | `gen_spchar` | All punctuation |
  | `gen_punc` | Punctuation minus brackets, slashes, commas, etc. |
  | `gen_nonalpha` | Digits + punctuation |
- **Word lists**
  - English: built from the `english-words` package (`web2` set) and cached as `en_wordlist.json` on first run
  - Japanese: built from `jp_dict.csv` (JLPT vocabulary), converted to Hepburn romaji with `pykakasi`, and cached as `jp_wordlist.csv` (currently disabled in `pword_config.py`)
- **Profile vault**: each profile has an account, username, password and tags
- **Search/filter**: by account, username, password, or tags (multiple tags with `AND` / `OR`)

## Requirements

- Python 3
- Packages:
  ```bash
  pip install english-words pykakasi
  ```

## Usage

```bash
python main.py
```

The first run creates any word-list caches that don't exist yet. After that, the main menu offers:

```
[c]reate profile/password   [v]iew saved passwords   [e]dit saved passwords   [ex]it
```

## Configuration

Edit `pword_config.py`:

- **`char_list`**: which character blocks go in a password and how many characters each has, e.g. `[gen_num, 2]`
- **`init_list`**: which word lists to build or load. Uncomment the `jp_wordlist.csv` line to turn on Japanese words.

To add a custom word list, write an `init_*()` function that saves a filtered list (length-checked, one word per row) to a `.json` or `.csv` file, then add `[filename, init_func]` to `init_list`.

Block order is set in `order_el()` in `aux_functions.py`. While `testing = True` the default order above is used. Set it to `False` to choose the order interactively.

## Project structure

| File | Role |
|---|---|
| `main.py` | Entry point. Builds caches, loads the preset vault, runs the main loop |
| `main_functions.py` | Main menu and routing |
| `user_functions.py` | Generate-and-assign flow |
| `aux_functions.py` | File I/O, CSV cleaning, password assembly, view/filter, translation |
| `input_functions.py` | Prompts with input checking |
| `gen_functions.py` | Random character generators |
| `pword_config.py` | Word-list setup and block configuration |
| `account_class.py` | `Profile` class |
| `preset_vault.py` | Sample profiles for testing |
| `jp_dict.csv` | Raw Japanese vocabulary source (expression, reading, meaning, tags) |
| `logs.txt` / `code_log` | Development time log |

## Roadmap

- [ ] Save and load the vault to/from a file
- [ ] View and edit saved profiles from the menu
- [ ] Interactive block customization and saved presets
- [ ] Simple GUI that shows saved passwords
- [ ] Re-enable the Japanese word list
