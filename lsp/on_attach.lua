-- 1. Astronvim Manual https://astronvim.com/Configuration/config_options,
-- said lsp.on_attach customize in user/lsp/on_attach
-- 2 . Hereis the lsp_signature configraion howto
-- https://github.com/ray-x/lsp_signature.nvim

-- return function(client, bnfnr)
-- end

return function()
  require('lsp_signature').on_attach({
    bind = true,
    handler_opts = {
      border = "rounded"
    }
  })
end
