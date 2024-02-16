require('mason').setup()
require("mason-lspconfig").setup({
    ensure_installed = { "lua_ls", "html" },
	})
local coq = require('coq')
--local capabilities = require('cmp_nvim_lsp').default_capabilities()
local capabilities = coq.lsp_ensure_capabilities()

--require('lspconfig').html.setup {}
--require('lspconfig').lua_ls.setup {}
--require('lspconfig').tailwindcss.setup {}

require('lspconfig')['html'].setup {
	filetypes = { 'html', 'blade', 'php' },
	capabilities = capabilities,
	init_options = {
		configurationSection = { "html", "css", "javascript", "php" },
		embeddedLanguages = {
			css = true,
			javascript = true,
			php = true
		},
		provideFormatter = true
	}
}
require('lspconfig')['lua_ls'].setup {
	capabilities = capabilities
}
require('lspconfig')['tailwindcss'].setup {
	capabilities = capabilities
}
require('lspconfig')['intelephense'].setup {
	capabilities = capabilities
}
require('lspconfig')['pyright'].setup {
	capabilities = capabilities
}
require('lspconfig')['phpactor'].setup {
	capabilities = capabilities
}
require('lspconfig')['eslint'].setup {
	capabilities = capabilities
}
