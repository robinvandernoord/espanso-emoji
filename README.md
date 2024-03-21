# Espanso Emoji

[espanso](https://espanso.org) config to replace Emoji shortcodes with the unicode character.

## Usage
First [install and set up espanso](https://espanso.org/docs/get-started/).  
Run `build.py` (no dependencies). This outputs `emoji.yml`. Place this yaml file in `.config/espanso/match/packages/emoji.yml`.  
Now you can type emoji like `:raccoon:` and espanso will convert them to the right character: `🦝`

See [github/gemoji](https://github.com/github/gemoji/blob/master/db/emoji.json) for a list of available emoji.
Both the 'aliases' and 'tags' are registered, as well as any custom aliases in 'aliases.json'.
