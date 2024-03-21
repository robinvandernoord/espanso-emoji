# Espanso HTML Entities

[espanso](https://espanso.org) config to replace HTML entities with the unicode character.

## Usage
First [install and set up espanso](https://espanso.org/docs/get-started/).  
Run `build.py` (no dependencies). This outputs `html.yml`. Place this yaml file in `.config/espanso/match/packages/html.yml`.  
Now you can type HTML entities like `&check;` and espanso will convert them to the right character: `✓`

See [HTML: The Living Standard - 13.2: Named character references](https://html.spec.whatwg.org/dev/named-characters.html#named-character-references) for a list of available shortcuts.

The list is also available [as a json file](https://html.spec.whatwg.org/entities.json).

