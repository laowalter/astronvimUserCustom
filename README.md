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
$ nvim +PackerSync
$ git clone git@github.com:laowalter/astronvimUserCustom.git ~/.config/nvim/lua/user
```

### Basic Setup

#### Install python lsp server

```neovim
:LspInstall pyls 
```

#### A language

1. lsp server 
  ```neovim
  :LspInstall pyls 
  ```

2. Language parser
  
  ```neovim
  :TSInstall python
  ```
3. Custom config in ~/.config/nvim/lua/user/init.lua
  
  See the init.lua line between 192 and 204.

### Feature

  - File explorer with **Neo-tree**
  - Autocompletion with **Cmp**
  - Git integration with **Gitsigns**
  - Statusline with **Heirline**
  - Terminal with **Toggleterm**
  - Fuzzy finding with **Telescope**
  - Syntax highlighting with **Treesitter**
  - Formatting and linting with **Null-ls**
  - Language Server Protocol with *Navtive lspConfig*

### mysetup

MasonInstall python-lsp-serverMason 
MasonInstall lua-language-server


### Understanding Manual[https://astronvim.github.io/Recipes/advanced_lsp]

```
return {
}
```

in user/init.lua means:


```
local config = {

}
return config
```


After Install flake8, with LspInfo can show null-ls worked as an attach server.
