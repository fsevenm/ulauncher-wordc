# Ulauncher Word Counter

> a [ulauncher](https://ulauncher.io/) extension to count words, alpha-words, characters and sentences.

## Screenshots
TBD

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python >= 2.7

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```https://github.com/fsevenm/ulauncher-wordc```
 

## Development

```shell script
git clone https://github.com/fsevenm/ulauncher-wordc
ln -s <clone_location> ~/.local/share/ulauncher/extensions/ulauncher-wordc
```

To start debugging the extension, run these debugging script:
```shell script
# run in different Terminal tab
ulauncher --no-extensions --dev -v
# run in different Terminal tab, you need to change PYTHONPATH value based on your local python config, change the USERNAME to yours
VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/ulauncher-wordc PYTHONPATH=/usr/lib/python3/dist-packages /usr/bin/python3 /home/USERNAME/.local/share/ulauncher/extensions/ulauncher-wordc/main.py
```

When you made any changes to `main.py` or the other assets, you need to re-run debugging scripts above.

## Todos
- [ ] Add gif preview (or screenshot)
- [ ] Add ability to count paragraphs

## License 

MIT @ Ayub Aswad
