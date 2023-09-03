return require('packer').startup(function()
	-- packer
	use 'wbthomason/packer.nvim'
	
	-- devicons
	use 'nvim-tree/nvim-web-devicons'

	-- colorscheme
	-- use 'sainnhe/gruvbox-material'
	use 'folke/tokyonight.nvim'

	-- lua line
	use {   'nvim-lualine/lualine.nvim',
		requires = { 'nvim-tree/nvim-web-devicons', opt = true }
	}
	-- Plugins can have post-install/update hooks
  	use {'iamcco/markdown-preview.nvim',
	      ft = "markdown",
	      run = ":call mkdp#util#install()",
	      config = function() vim.g.mkdp_auto_start = 1 end}
	
	-- Git in neovim
	use 'tpope/vim-fugitive' 

	--Diff viewer git
	use "sindrets/diffview.nvim" 

	-- Syntax language highlighting
	use { 'nvim-treesitter/nvim-treesitter', run = ':TSUpdate' }

	-- Tree toogle and git status 
	-- use 'nvim-tree/nvim-tree.lua'
	use {
		"nvim-neo-tree/neo-tree.nvim",
		    branch = "v3.x",
		    requires = { 
		      "nvim-lua/plenary.nvim",
		      "nvim-tree/nvim-web-devicons",
		      "MunifTanjim/nui.nvim",
    			}
  	}

	-- Generate lorem ipsum text
	use { "derektata/lorem.nvim" }

	-- Plenary
	use "nvim-lua/plenary.nvim"

	--Autocompletado de codigo
	use {'neoclide/coc.nvim', branch = 'release'}

	-- Usar relative and absolute numbers
	use 'nkakouros-original/numbers.nvim'

	-- Vimtex
	use 'lervag/vimtex'

	-- Templates
	use {'pianocomposer321/project-templates.nvim', run=':PackerUpdate'}

	-- Terminal 
	use {"akinsho/toggleterm.nvim", tag = '*', config = function()
  			require("toggleterm").setup()
		end}
end)
