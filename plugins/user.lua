return {
  -- You can also add new plugins here as well:
  -- Add plugins, the lazy syntax
  -- "andweeb/presence.nvim",
  -- {
  --   "ray-x/lsp_signature.nvim",
  --   event = "BufRead",
  --   config = function()
  --     require("lsp_signature").setup()
  --   end,
  -- },
  { "sainnhe/sonokai" }, -- installed by me.

  {
    "glepnir/template.nvim",
    cmd = { "Template" },
    config = function()
      require("template").setup {
        temp_dir = "~/.config/nvim/lua/user/templates/",
        author = "Walter Guo",
        email = "Walter@eliglad.com",
      }
    end,
  },
  {
    "rebelot/heirline.nvim",
    opts = function(_, opts)
      local status = require "astronvim.utils.status"
      opts.statusline = {
        -- statusline
        hl = { fg = "fg", bg = "bg" },
        status.component.mode { mode_text = { padding = { left = 1, right = 1 } } }, -- add the mode text
        status.component.git_branch(),
        status.component.file_info { filename = { modify = ":~" }, file_modified = false },
        status.component.git_diff(),
        status.component.diagnostics(),
        status.component.cmd_info(),
        status.component.fill(),
        status.component.lsp(),
        status.component.treesitter(),
        status.component.nav(),
        status.component.builder(),
        -- remove the 2nd mode indicator on the right
      }
      -- return the final configuration table
      return opts
    end,
  },

  -- Old version
  -- heirline = function(config)
  --   config[1][3] = astronvim.status.component.file_info { filename = { modify = ":~" } }
  --   return config
  -- end
}
