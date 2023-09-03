local map = vim.keymap
vim.g.mapleader = ","

map.set('n','<C-n>',':Neotree float toggle<CR>')
map.set('n','<leader>a','<Plug>(coc-codeaction-selected)')

vim.api.nvim_create_autocmd('FileType', {
	pattern = 'python',
	callback = function ()	
		map.set('','<F9>',[[<esc>:w<CR>:exec '!python3' shellescape(@%,1)<CR>]])
	end
})

map.set('n','<C-s>','<Plug>MarkdownPreview')
map.set('n','<M-s>','<Plug>MarkdownPreviewStop')
map.set('n','<C-p>','<Plug>MarkdownPreviewToggle')
map.set('n','<C-j>','<C-w>j')
map.set('n','<C-k>','<C-w>k')
map.set('n','<C-h>','<C-w>h')
map.set('n','<C-l>','<C-w>l')
