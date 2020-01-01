" => General ===================================================================
set history=500

" Enable filetype plugins
filetype plugin on
filetype indent on


" => VIM user interface ========================================================
set number
set ruler
set hid
set backspace=eol,start,indent
set whichwrap+=<,>,h,l
set ignorecase
set smartcase
set hlsearch
set incsearch
set lazyredraw
set magic
set showmatch
set mat=2
set showcmd
set wrapscan
set matchtime=3
set list
set autoindent
set hidden
set ttyfast
set cursorline
set cursorcolumn
set colorcolumn=80

" No annoying sound on errors
set noerrorbells
set novisualbell
set t_vb=
set tm=500
set belloff=all
set vb t_vb=

" => Colors and Fonts ==========================================================
colorscheme molokai
set t_Co=256
set encoding=utf8
set ffs=unix,dos,mac
set fileencoding=utf-8
set fileencodings=utf-8,iso-2022-jp,euc-jp,sjis

" => Files, backups and undo ===================================================
set noswapfile
set nobackup
set nowb

" => Text, tab and indent related
set expandtab
set smarttab
set shiftwidth=4
set tabstop=4
set softtabstop=0
set lbr
set tw=500
set ai
set si
set wrap


" => Moving windows
map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-h> <C-W>h
map <C-l> <C-W>l

" => Status line
set laststatus=2
set cmdheight=3

" => Tab line
set showtabline=2
set guioptions-=e

" => Custom Key Mappings
Mappings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Like windows keymapping
inoremap <C-v>                  <C-r>*
inoremap <C-e>                  <End>
vnoremap <C-C>                  "+y
nnoremap <C-a>                  ggVG
nnoremap <C-e>                  <End>

" Tab control
nnoremap <C-t>                  :tabe<cr>
nnoremap <C-tab>                :tabnext<cr>
nnoremap <C-S-tab>              :tabprevious<cr>

" => For Plugin

" Vim doc - Ja
set helplang=ja

" QuickRun for Python
let g:quickrun_config = {}
let g:quickrun_config.python = {'command': 'python3'}

" indentLine
let g:indentLine_setColors = 0
let g:indentLine_color_term = 239
