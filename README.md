# astronvimUserCustom

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
$ nvim +PackerSync
$ git clone git@github.com:laowalter/astronvimUserCustom.git ~/.config/nvim/lua/user
```

#### Basic Setup

```neovim
:LspInstall pyls 
```
