return {
  "pysan3/fcitx5.nvim",
  cond = vim.fn.executable "fcitx5-remote" == 1,
  event = { "ModeChanged" },

  config = function()
    local en = "keyboard-us"
    local cn = "pinyin"
    require("fcitx5").setup {
      imname = {
        norm = en,
        ins = en,
        cmd = en,
      },
      remember_prior = true,
    }
  end,
}
