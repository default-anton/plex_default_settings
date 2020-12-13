from typing import Generator

import typer
from plexapi.exceptions import NotFound
from plexapi.media import MediaPart
from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
from plexapi.video import Show

app = typer.Typer()

username = typer.Option(..., help="Your Plex username")
password = typer.Option(..., help="Your Plex password")
servername = typer.Option(..., help="Plex server name")
show = typer.Argument(..., help="Show title")
lang = typer.Argument(
    ...,
    help="""Language code is defined by the ISO-639-1 (2-letter) or ISO-639-2/B (3-letter) standard. See links below

https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes, https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes""")

GLOBAL_OPTIONS = {'verbose': False}


@app.command()
def sub(username: str = username,
        password: str = password,
        servername: str = servername,
        show: str = show,
        lang: str = lang):
    """Set the default subtitles for every episode of the show."""
    account = MyPlexAccount(username, password)
    plex: PlexServer = account.resource(servername).connect()

    try:
        not_found_subs_count = 0
        for part in _get_media_parts(plex, show):
            is_found = False
            for sub in part.subtitleStreams():
                if not sub.forced and sub.languageCode == lang:
                    part.setDefaultSubtitleStream(sub)
                    is_found = True
                    break
            if not is_found:
                not_found_subs_count += 1
                if GLOBAL_OPTIONS['verbose']:
                    typer.echo(f'Subtitles for "{lang}" not found for file: {part.file}', err=True)

        if not_found_subs_count != 0:
            typer.echo(f'{not_found_subs_count} subs were not found', err=True)
            raise typer.Abort()
    except NotFound as e:
        typer.echo("Show, media item, or device is not found.", err=True)
        typer.echo(e, err=True)
        raise typer.Abort()

    typer.echo('Success!')


@app.command()
def dub(username: str = username,
        password: str = password,
        servername: str = servername,
        show: str = show,
        lang: str = lang):
    """Set the default dubs for every episode of the show."""
    account = MyPlexAccount(username, password)
    plex: PlexServer = account.resource(servername).connect()

    try:
        not_found_dubs_count = 0
        for part in _get_media_parts(plex, show):
            is_found = False
            for audio in part.audioStreams():
                if audio.languageCode == lang:
                    part.setDefaultAudioStream(audio)
                    is_found = True
                    break
            if not is_found:
                not_found_dubs_count += 1
                if GLOBAL_OPTIONS['verbose']:
                    typer.echo(f'Audio for "{lang}" not found for file: {part.file}', err=True)

        if not_found_dubs_count != 0:
            typer.echo(f'{not_found_dubs_count} dubs were not found', err=True)
            raise typer.Abort()
    except NotFound as e:
        typer.echo("Show, media item, or device is not found.", err=True)
        typer.echo(e, err=True)
        raise typer.Abort()

    typer.echo('Success!')


@app.callback()
def set_verbose(verbose: bool = typer.Option(False)):
    GLOBAL_OPTIONS['verbose'] = verbose


def _get_media_parts(plex: PlexServer, show_title: str) -> Generator[MediaPart, None, None]:
    show: Show = plex.library.section('TV Shows').get(show_title)
    with typer.progressbar(show.episodes(), label='Updating episodes', show_eta=False) as progress:
        for episode in progress:
            episode = episode.reload()
            yield from episode.iterParts()


if __name__ == "__main__":
    app()
