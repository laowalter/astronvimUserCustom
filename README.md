# astronvimUserCustom

https://astronvim.github.io/

## Install astronvim

### Prepare

```
$ emerge rgrep
$ rm -fr ~/.local/share/nvim
$ rm -fr ~/.cache/nvim
$ rm -fr ~/.config/nvim
```

### Install

```bash
$ git config --global --add url."git@github.com:".insteadOf "https://github.com/"
$ git clone https://github.com/AstroNvim/AstroNvim ~/.config/nvim
$ nvim
$ # Do NOT use nvim +PackerSync from command line
$ # Just open nvim and install :PackerSync command.
$ # Be SURE to wait until all the packages completely installed.
```

```bash
$ git clone git@github.com:laowalter/astronvimUserCustom.git ~/.config/nvim/lua/user
```

### Basic Setup

### Finally

start up nvim:

#### use :Mason to install the following:

- autopep8
- bash-language-server
- codespell
- debuggpy
- gopls
- html-lsp
- lua-language-server
- misspell
- prettier
- python-lsp-server
- stylua

#### use :TSInstall to install the following:

- c
- python
- bash
- html
- javascript
- go
- markdown
