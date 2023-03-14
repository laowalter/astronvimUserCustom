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

#### Install python lsp server

lsp + autoformat on save.

```neovim
1. TSInstall python
1. Use Mason to install python-lsp-server
2. pip install pycodestyle 
3. set pycodestyle in user/init.lua
  -- Add overrides for LSP server settings, the keys are the name of the server
  ["server-settings"] = {
      pylsp = {
          settings = {
              pylsp = {
                  plugins = {
                      pycodestyle = {
                          ignore = { 'W391', 'W503' },
                          maxLineLength = 160
                      }
                  }
              }
          }
      }
  },

```

### how file full path on status line.

1. plugins/init.lua

### Finally

start up nvim:

use :Parksync to install simpolfold add in user/init.lua
use :TSinstall to install python bash c
use :Mason to install:

1. python-lsp-server
2. autopep8
