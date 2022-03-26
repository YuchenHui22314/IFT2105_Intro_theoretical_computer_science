if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <silent> <C-Tab> =UltiSnips#ListSnippets()
snoremap <silent>  "_c
xnoremap <silent> 	 :call UltiSnips#SaveLastVisualSelection()gvs
snoremap <silent> 	 :call UltiSnips#ExpandSnippetOrJump()
snoremap  "_c
nnoremap ,w :w 
xnoremap ,w :w 
onoremap ,w :w 
xmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
vnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(expand((exists("g:netrw_gx")? g:netrw_gx : '<cfile>')),netrw#CheckIfRemote())
snoremap <silent> <Del> "_c
snoremap <silent> <BS> "_c
snoremap <silent> <C-Tab> :call UltiSnips#ListSnippets()
nnoremap <silent> <Plug>(startify-open-buffers) :call startify#open_buffers()
inoremap <silent> 	 =UltiSnips#ExpandSnippetOrJump()
inoremap ,w :w
inoremap jj `^
let &cpo=s:cpo_save
unlet s:cpo_save
set autoindent
set background=dark
set backspace=indent,eol,start
set errorfile=~/diro/2105/devoir2/main.log
set fileencodings=ucs-bom,utf-8,default,latin1
set helplang=en
set nomodeline
set printoptions=paper:a4
set ruler
set runtimepath=~/.vim,~/.vim/plugged/vim-startify,~/.vim/plugged/vimtex,~/.vim/plugged/ultisnips,/var/lib/vim/addons,/usr/share/vim/vimfiles,/usr/share/vim/vim80,/usr/share/vim/vimfiles/after,/var/lib/vim/addons/after,~/.vim/plugged/vimtex/after,~/.vim/plugged/ultisnips/after,~/.vim/after
set shortmess=filnxtToOI
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc,.sty,.cls,.fdb_latexmk,.fls,.pdf,.synctex.gz
set window=38
" vim: set ft=vim :
