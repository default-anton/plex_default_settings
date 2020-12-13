## Requirements

Python 3.8+

## Installation

<div class="termy">

```console
$ pip install plex_default_settings
---> 100%
Successfully installed plex_default_settings
```

</div>

## Usage

### Commands

<div class="termy">
  
```console
$ plex_default_settings --help
Usage: plex_default_settings [OPTIONS] COMMAND [ARGS]...

Options:
  --verbose / --no-verbose        [default: False]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.

Commands:
  dub  Set the default dubs for every episode of the show.
  sub  Set the default subtitles for every episode of the show.
```

</div>

### Setting default subtitles for every episode of a show

<div class="termy">
  
```console
$ plex_default_settings sub --help
Usage: plex_default_settings sub [OPTIONS] SHOW LANG

  Set the default subtitles for every episode of the show.

Arguments:
  SHOW  Show title  [required]
  LANG  Language code is defined by the ISO-639-1 (2-letter) or ISO-639-2/B
        (3-letter) standard. See links below

        https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes,
        https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes  [required]


Options:
  --username TEXT    Your Plex username  [required]
  --password TEXT    Your Plex password  [required]
  --servername TEXT  Plex server name  [required]
  --help             Show this message and exit.
```

</div>

### Setting default dubs for every episode of a show

<div class="termy">
  
```console
$ plex_default_settings dub --help
Usage: plex_default_settings dub [OPTIONS] SHOW LANG

  Set the default dubs for every episode of the show.

Arguments:
  SHOW  Show title  [required]
  LANG  Language code is defined by the ISO-639-1 (2-letter) or ISO-639-2/B
        (3-letter) standard. See links below

        https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes,
        https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes  [required]


Options:
  --username TEXT    Your Plex username  [required]
  --password TEXT    Your Plex password  [required]
  --servername TEXT  Plex server name  [required]
  --help             Show this message and exit.
```

</div>

## Example

### Set jpn dubs for every episode in the show "Hokuto No Ken Fan-Kai"

<div class="termy">
  
```console
$ plex_default_settings dub \
  --username "${USERNAME}" \
  --password "${PASSWORD}" \
  --servername 'Linux Media Server' \
  'Hokuto No Ken Fan-Kai' jpn
Updating episodes  [####################################]  100%
Success!
```

</div>

### Set eng subs for every episode in the show "Hokuto No Ken Fan-Kai"

<div class="termy">
  
```console
$ plex_default_settings sub \
  --username "${USERNAME}" \
  --password "${PASSWORD}" \
  --servername 'Linux Media Server' \
  'Hokuto No Ken Fan-Kai' eng
Updating episodes  [####################################]  100%
Success!
```

</div>
