
" Plugins {{{

call plug#begin('~/.vim/plugged')
    
    Plug 'preservim/nerdtree'
    Plug 'jasonccox/vim-wayland-clipboard'
    Plug 'vim-airline/vim-airline'

call plug#end()

" }}}


" Vim Settings {{{

set nocompatible
filetype on
filetype plugin on
filetype indent on
syntax on
set relativenumber
set shiftwidth=4
set tabstop=4
set expandtab
set nobackup
set scrolloff=10
set nowrap
set incsearch
set ignorecase
set smartcase
set showcmd
set showmode
set showmatch
set hlsearch
set history=1000
set wildmenu
set wildmode=list:longest
set wildignore=*.docx,*.jpg,*.png,*.gif,*.pdf,*.pyc,*.exe,*.flv,*.img,*.xlsx"
" set shell=fish
set shell=powershell
set foldmethod=marker
set mouse=n
set background=dark

set gfn=Hack_Nerd_Font_Mono:h12:cANSI:qDRAFT
colorscheme desert

" }}}


" Mappings {{{

" NerdTree Keybinds
nnoremap <leader>n : NERDTreeToggle<CR>

" }}}


" Sources {{{
" From https://www.freecodecamp.org/news/vimrc-configuration-guide-customize-your-vim-editor/
" }}}
