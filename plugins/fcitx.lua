return {
  {
    "lilydjwg/fcitx.vim",
    init = function() -- init function runs before the plugin is loaded
      vim.g.fcitx5_remote = 1
    end,
  },
}
