## For vnpy project 

The neovim is dedicated for the vnpy project, it is better to install all 
the python enviroment related plugins directly withi venv vnpy, so manual 
install the following package with pip.

- debuggy: pip install debuggy
- pylsp: pip install python-lsp-server

## Common plugins could install by :MasonInstall come with Astronvim
- autopep8 
  - work with pylsp can support autoformat on save.

## Extra plugins added in user/init.lua
- {"tmhedberg/SimplyFold"} 
  - for pyton folding support
- {"mfusseger/nvim-dap"} 
  - General debug api for neovim
  - debuggy use the api to support python
  - by now Astronvim did not integreted the plugin.
  
## Features:

- python autoformat onsave with pep8 not flake8 [done]
- python pylsp (python-lsp-sever) version 1.60 [done]
- debug by neo-dap support by debuggy

## Comments:
- Choose pylsp but not pright
  - pyright can not corrent use "gd", no time to figure out.
