local g = vim.g

g.coc_global_extensions = {
	'coc-lua',
	'coc-css',
	'coc-html',
	'coc-htmldjango',
	'coc-clangd',
	'coc-python',
	'coc-prettier',
	'coc-eslint',
	'coc-json',
	'coc-json',
	'coc-emmet',
	'coc-snippets',
	'coc-spell-checker',
	'coc-cspell-dicts',
}

local keyset = vim.keymap.set
keyset("n", "<leader>.", "<Plug>(coc-codeaction)", {})
keyset("n", "<leader>l", ":CocCommand eslint.executeAutofix<CR>", {})
keyset("n", "gd", "<Plug>(coc-definition)", {silent = true})
keyset("n", "K", ":call CocActionAsync('doHover')<CR>", {silent = true, noremap = true})
keyset("n", "<leader>rn", "<Plug>(coc-rename)", {})
keyset("n", "<leader>f", ":CocCommand prettier.formatFile<CR>", {noremap = true})
keyset("i", "<C-Space>", "coc#refresh()", { silent = true, expr = true })
keyset("i", "<TAB>", "coc#pum#visible() ? coc#pum#next(1) : '<TAB>'", {noremap = true, silent = true, expr = true})
keyset("i", "<S-TAB>", "coc#pum#visible() ? coc#pum#prev(1) : '<C-h>'", {noremap = true, expr = true})
keyset("i", "<CR>", "coc#pum#visible() ? coc#pum#confirm() : '<C-G>u<CR><C-R>=coc#on_enter()<CR>'", {silent = true, expr = true, noremap = true})
vim.o.hidden = true
vim.o.backup = false
vim.o.writebackup = false
vim.o.updatetime = 300
