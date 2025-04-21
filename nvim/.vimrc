"Plugins"
let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin('~/.vim/plugged')
Plug 'kylechui/nvim-surround'
" Lsp Manager
Plug 'williamboman/mason.nvim'
Plug 'williamboman/mason-lspconfig.nvim'
Plug 'neovim/nvim-lspconfig'
" Autocomplete
Plug 'hrsh7th/cmp-nvim-lsp'
Plug 'hrsh7th/cmp-buffer'
Plug 'FelipeLema/cmp-async-path'
Plug 'hrsh7th/cmp-cmdline'
Plug 'hrsh7th/nvim-cmp'
Plug 'L3MON4D3/LuaSnip', {'tag': 'v2.*', 'do': 'make install_jsregexp'} 
Plug 'windwp/nvim-autopairs'
Plug 'micangl/cmp-vimtex'
" Linter
Plug 'mfussenegger/nvim-lint'
" Theme
Plug 'nordtheme/vim'
Plug 'vim-airline/vim-airline'
" Misc
Plug 'phaazon/hop.nvim'
Plug 'rlue/vim-barbaric'
Plug 'preservim/vim-markdown'
Plug 'lervag/vimtex'
Plug 'github/copilot.vim'
Plug 'LoricAndre/OneTerm.nvim'
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim', { 'tag': '0.1.2' }
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'MunifTanjim/nui.nvim'
" markdown
Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app && npx --yes yarn install' }
Plug 'chentoast/marks.nvim'
call plug#end()

:lua require'hop'.setup()
nmap <leader>w :HopWord<CR>
imap <leader>w :HopWord<CR>

let g:vim_markdown_folding_disabled = 1

set tabstop=2
set softtabstop=2
set shiftwidth=2
set expandtab

set spelllang=en_us
set spell

"Latex"
let g:tex_flavor = 'latex'
let g:vimtex_quickfix_mode = 0
let g:vimtex_view_general_viewer = 'zathura'
let g:vimtex_view_method = 'zathura'
let g:vimtex_compiler_progname = 'nvr'
let g:vimtex_compiler_method = 'latexmk'

"Color Scheme"
set t_Co=256 
set background=dark
colorscheme nord
syntax on

"FileEncoding"
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8

"LineNumber"
set nu
set number

"Cursor Line"
set cul

"Mouse Support"
set selection=exclusive
set selectmode=mouse,key
set mouse=a

"Appearance and Functionality"
set showmatch
set tabstop=2
set shiftwidth=2
set autoindent
set laststatus=2
set ruler
filetype plugin indent on
set ttimeout
set ttimeoutlen=0
set matchtime=0

"For savedconfig"
set modeline
set modelines=5
