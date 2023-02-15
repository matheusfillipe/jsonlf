# jsonlf

This is a json line formarter. It expects a valid json on stdin and outputs it pretty-printed and uses [pygments](https://pygments.org) for highlighting. It will also attempt to format python tracebacks.

## Installation

```sh
pip install jsonlf
```

## Usage

```sh
some_command_that_logs_json_lines | jsonlf
```

You can use pygments styles listed here: https://pygments.org/styles/
Just pass their names as the first argument. Example:


```sh
some_command_that_logs_json_lines | jsonlf emacs
```
