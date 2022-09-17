# mOve

A very simple tool to quickly move arround commonly used directories on your *nix systems. The letter 'O' is capitalized because the primary command to run this program is `o`, which means 'move' or 'open'. 

## Description

With this program, you can tag the current directory with `o + <tag>` and navigate back to that directory from anywhere via `o <tag>`. 

## Getting Started

### Dependencies

- A *nix operating system
- Python3 (including the following packages: json, argparse, pathlib)

### Installing

To install mOve, clone this directory to `/path/to/mOve` (e.g. `${HOME}/local/source/mOve`) and paste the following texts into your SHELL initialization file (.bashrc, .zshrc, etc)

``` shell
# >>> mOve initialize >>>
export MOVE_ROOT="/path/to/mOve"
export MOVE_JSON="${HOME}/.config/mOve/projects.json"
source "${MOVE_ROOT}/source.rc"
# <<< mOve initialize <<<
```

### Executing program

To start to use thie program, first go to a directory and do `o + <tag>` (replace <tag> with a tag you want to assign to this directory). Now, go to any directory and a simple `o <tag>` will bring you back to the tagged directory. More options including updating, removing, and printing the tags are available. `o -h` for a short documentation.

### Usage in vifm

I use this program inside vifm apart from in terminal. To make mOve work in vifm, you have to put the setup source script inside the unlogin shell configuration file (e.g. .zshenv/.bashenv on macOS). At last, I have the following in my `vifmrc`:

```
command! o :execute 'cd' system('${MOVE_ROOT}/getdir.py %a 2> /dev/null')
nnoremap o :o<space>
command! moveadd !o + %a %d
```

After these setups, you can execute a simple `o<space>em` to navigate to the directory that is  tagged with `emacs`. 

## Help

## Authors

Contributors names and contact info

ChongChjong He (che1234 @ umd.edu) (https://www.astro.umd.edu/~chongchong/)

## Version History

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [nnn](https://github.com/jarun/nnn)

