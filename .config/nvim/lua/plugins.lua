return require('packer').startup(function()
	-- plugin-manager
	use 'wbthomason/packer.nvim'
	-- theme
	use "rafamadriz/neon"
	-- auto-session
	use { 'rmagatti/auto-session',
		config = function() 
			require("auto-session").setup {
      log_level = "error",
      auto_session_suppress_dirs = { "~/", "~/Projects", "~/Downloads", "/"},
			}
		end
	}
	-- comment
	use { 'numToStr/Comment.nvim',
    config = function()
			require('Comment').setup()
    end
	}
	-- guess-indent
	use { 'nmac427/guess-indent.nvim',
		config = function()
			require('guess-indent').setup {} 
		end
	}
	-- autopairs
	use { "windwp/nvim-autopairs",
    config = function()
			require("nvim-autopairs").setup {} 
		end
	}
	-- treesitter
	use { 'nvim-treesitter/nvim-treesitter',
		run = ':TSUpdate'
	}
	-- lualine
	use { 'nvim-lualine/lualine.nvim',
		requires = { 'nvim-tree/nvim-web-devicons', opt = false }
	}
	-- nvim-tree
	use { 'nvim-tree/nvim-tree.lua',
		requires = { 'nvim-tree/nvim-web-devicons', opt = false}
	}
	-- web dev icons
	use 'nvim-tree/nvim-web-devicons'
	-- mason, mason-config, nvim-lspconfig
	use { 'williamboman/mason.nvim',
		'williamboman/mason-lspconfig.nvim',
    'neovim/nvim-lspconfig'
	}
	-- telescope and dependencies
	use 'nvim-telescope/telescope.nvim'
	use 'nvim-lua/plenary.nvim'
	-- telescope improve plugins
	use {
		'nvimdev/lspsaga.nvim',
    after = 'nvim-lspconfig',
    config = function()
        require('lspsaga').setup({})
    end,
	}

	-- autocompletion core
	use {
		'hrsh7th/cmp-nvim-lsp',
		'hrsh7th/cmp-buffer',
		'hrsh7th/cmp-path',
		'hrsh7th/cmp-cmdline',
		'hrsh7th/nvim-cmp'
	}

	-- snips
	use {
		'dcampos/nvim-snippy',
		'dcampos/cmp-snippy',
		'honza/vim-snippets'
	}
	
	-- coq
	use 'ms-jpq/coq_nvim'

end)
