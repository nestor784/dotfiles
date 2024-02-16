local map = vim.keymap
vim.g.mapleader = ","

-- nvim-tree
map.set('n','<C-n>',':NvimTreeToggle<CR>')

-- disable ctrl-z
vim.cmd('nnoremap <c-z> <nop>')

-- autocmd python
vim.api.nvim_create_autocmd('FileType', {
	pattern = 'python',
	callback = function ()	
		map.set('','<F9>',[[<esc>:w<CR>:exec '!python3' shellescape(@%,1)<CR>]])
	end
})

-- markdown kinbings
--map.set('n','<C-s>','<Plug>MarkdownPreview')
--map.set('n','<M-s>','<Plug>MarkdownPreviewStop')
--map.set('n','<C-p>','<Plug>MarkdownPreviewToggle')

-- navigation shortcut
map.set('n','<C-j>','<C-w>j')
map.set('n','<C-k>','<C-w>k')
map.set('n','<C-h>','<C-w>h')
map.set('n','<C-l>','<C-w>l')

-- telescope bindigns
local builtin = require('telescope.builtin')
map.set('n', '<leader>ff', builtin.find_files, {})
map.set('n', '<leader>fg', builtin.live_grep, {})
map.set('n', '<leader>fb', builtin.buffers, {})
map.set('n', '<leader>fh', builtin.help_tags, {})
map.set('n', '<leader>fls', builtin.treesitter, {})
map.set('n', '<leader>ldef', builtin.lsp_definitions, {})
map.set('n', '<leader>limp', builtin.lsp_implementations, {})
map.set('n', '<leader>lref', builtin.lsp_references, {})

-- lsp-saga keybindings review https://nvimdev.github.io/lspsaga/

-- snips keybindings
vim.cmd[[
imap <expr> <Tab> snippy#can_expand_or_advance() ? '<Plug>(snippy-expand-or-advance)' : '<Tab>'
imap <expr> <S-Tab> snippy#can_jump(-1) ? '<Plug>(snippy-previous)' : '<S-Tab>'
smap <expr> <Tab> snippy#can_jump(1) ? '<Plug>(snippy-next)' : '<Tab>'
smap <expr> <S-Tab> snippy#can_jump(-1) ? '<Plug>(snippy-previous)' : '<S-Tab>'
xmap <Tab> <Plug>(snippy-cut-text)
]]
