FRONT = r"""
% Author: Indrajit Ghosh
% Title: Washing Machine Slots

\documentclass[11pt, a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[top=0.7 in,bottom=1in, left=0.4 in, right=1 in]{geometry}

\usepackage{hyperref}
\hypersetup{
	pdftitle={Washing Machine Slots for RS Hostel, ISIBc},
	pdfauthor={Indrajit Ghosh},
	pdfsubject={Washing Machine},
	pdfcreationdate={\today},
	pdfcreator={MikTex},
	pdfkeywords={ISI},
}


\setlength{\arrayrulewidth}{0.5mm}
\setlength{\tabcolsep}{18pt}
\renewcommand{\arraystretch}{1.5}



\begin{document}
\thispagestyle{empty}
	
\centering

\begin{tabular}{ |p{2.5cm}|p{2.6cm}|p{2.6cm}|p{2.6cm}|p{2.6cm}|  }
	
	\hline
	
	\multicolumn{5}{|c|}{\textbf{\Large Washing Machine {\it \large{(BOSCH)}} Slots}} \\
	\hline
	
	\textbf{Date} & \textbf{07:00-10:30} & \textbf{11:30-15:00} & \textbf{16:00-19:30} & \textbf{20:30-00:00} \\
	\hline

"""

## middle
#  & &  & \\
# \hline

BACK = r"""
\end{tabular}


\end{document}

"""

DIAGBOX_STY = r"""
%%
%% This is file `diagbox.sty',
%% generated with the docstrip utility.
%%
%% The original source files were:
%%
%% diagbox.dtx  (with options: `package')
%% 
%% This is a generated file.
%% 
%% Copyright (C) 2011 by Leo Liu <leoliu.pku@gmail.com>
%% --------------------------------------------------------------------------
%% This work may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either version 1.3
%% of this license or (at your option) any later version.
%% The latest version of this license is in
%%   http://www.latex-project.org/lppl.txt
%% and version 1.3 or later is part of all distributions of LaTeX
%% version 2005/12/01 or later.
%% 
\NeedsTeXFormat{LaTeX2e}[1999/12/01]
\ProvidesPackage{diagbox}
    [2011/11/23 v2.0 Making table heads with diagonal lines]
\RequirePackage{keyval}
\RequirePackage{pict2e}
\RequirePackage[nomessages]{fp}
\newbox\diagbox@boxa
\newbox\diagbox@boxb
\newbox\diagbox@boxm
\newdimen\diagbox@wd
\newdimen\diagbox@ht
\newdimen\diagbox@sepl
\newdimen\diagbox@sepr
\define@key{diagbox}{width}{%
  \setlength{\diagbox@wd}{#1}}
\define@key{diagbox}{height}{%
  \setlength{\diagbox@ht}{#1}}
\define@key{diagbox}{trim}{%
  \@tfor\@reserveda:=#1\do{%
    \ifcsname diagbox@sep\@reserveda\endcsname
      \setlength{\csname diagbox@sep\@reserveda\endcsname}{\z@}%
    \else
      \PackageError{diagbox}{Unknown trim option `#1'.}{l, r, lr and rl are supported.}%
    \fi}}
\define@key{diagbox}{dir}{%
  \def\diagbox@dir{#1}%
  \unless\ifcsname diagbox@dir@#1\endcsname
    \PackageError{diagbox}{Unknown direction `#1'.}{NW, NE, SW, SE are supported.}%
    \def\diagbox@dia{NW}%
  \fi}
\let\diagbox@dir@SE\relax
\let\diagbox@dir@SW\relax
\let\diagbox@dir@NE\relax
\let\diagbox@dir@NW\relax
\def\diagbox@pict{%
  \unitlength\p@
  \begin{picture}
    (\strip@pt\dimexpr\diagbox@wd-\diagbox@sepl-\diagbox@sepr\relax,\strip@pt\diagbox@ht)
    (\strip@pt\diagbox@sepl,0)
      \@nameuse{diagbox@\diagbox@part @pict@\diagbox@dir}
  \end{picture}}
\def\diagbox@double@pict@SE{%
  \put(0,0) {\makebox(0,0)[bl]{\box\diagbox@boxa}}
  \put(\strip@pt\diagbox@wd,\strip@pt\diagbox@ht) {\makebox(0,0)[tr]{\box\diagbox@boxb}}
  \Line(0,\strip@pt\diagbox@ht)(\strip@pt\diagbox@wd,0)}
\let\diagbox@double@pict@NW\diagbox@double@pict@SE
\def\diagbox@double@pict@NE{%
  \put(0,\strip@pt\diagbox@ht) {\makebox(0,0)[tl]{\box\diagbox@boxa}}
  \put(\strip@pt\diagbox@wd,0) {\makebox(0,0)[br]{\box\diagbox@boxb}}
  \Line(0,0)(\strip@pt\diagbox@wd,\strip@pt\diagbox@ht)}
\let\diagbox@double@pict@SW\diagbox@double@pict@NE
\def\diagbox@double#1#2#3{%
  \begingroup
  \diagbox@wd=\z@
  \diagbox@ht=\z@
  \diagbox@sepl=\tabcolsep
  \diagbox@sepr=\tabcolsep
  \def\diagbox@part{double}%
  \setkeys{diagbox}{dir=NW,#1}%
  \setbox\diagbox@boxa=\hbox{%
    \begin{tabular}{@{\hspace{\diagbox@sepl}}l@{}}#2\end{tabular}}%
  \setbox\diagbox@boxb=\hbox{%
    \begin{tabular}{@{}r@{\hspace{\diagbox@sepr}}}#3\end{tabular}}%
  \ifdim\diagbox@wd=\z@
    \ifdim\wd\diagbox@boxa>\wd\diagbox@boxb
      \diagbox@wd=\dimexpr2\wd\diagbox@boxa+\diagbox@sepl+\diagbox@sepr\relax
    \else
      \diagbox@wd=\dimexpr2\wd\diagbox@boxb+\diagbox@sepl+\diagbox@sepr\relax
    \fi
  \fi
  \ifdim\diagbox@ht=\z@
    \diagbox@ht=\dimexpr\ht\diagbox@boxa+\dp\diagbox@boxa+\ht\diagbox@boxb+\dp\diagbox@boxb\relax
  \fi
  $\vcenter{\hbox{\diagbox@pict}}$%
  \endgroup}
\def\diagbox@triple@setbox@NW#1#2#3{%
  \setbox\diagbox@boxa=\hbox{%
    \begin{tabular}{@{\hspace{\diagbox@sepl}}l@{}}#1\end{tabular}}%
  \setbox\diagbox@boxm=\hbox{%
    \begin{tabular}{@{\hspace{\diagbox@sepl}}l@{}}#2\end{tabular}}%
  \setbox\diagbox@boxb=\hbox{%
    \begin{tabular}{@{}r@{\hspace{\diagbox@sepr}}}#3\end{tabular}}}
\let\diagbox@triple@setbox@SW\diagbox@triple@setbox@NW
\def\diagbox@triple@setbox@SE#1#2#3{%
  \setbox\diagbox@boxa=\hbox{%
    \begin{tabular}{@{\hspace{\diagbox@sepl}}l@{}}#1\end{tabular}}%
  \setbox\diagbox@boxm=\hbox{%
    \begin{tabular}{@{}r@{\hspace{\diagbox@sepr}}}#2\end{tabular}}%
  \setbox\diagbox@boxb=\hbox{%
    \begin{tabular}{@{}r@{\hspace{\diagbox@sepr}}}#3\end{tabular}}}
\let\diagbox@triple@setbox@NE\diagbox@triple@setbox@SE
\def\diagbox@triple@pict@NW{%
  \put(0,0)   {\makebox(0,0)[bl]{\box\diagbox@boxa}}
  \put(0,\y)  {\makebox(0,0)[tl]{\box\diagbox@boxm}}
  \put(\x,\y) {\makebox(0,0)[tr]{\box\diagbox@boxb}}
  \Line(0,\yym)(\x,0)
  \Line(\xm,\y)(\x,0)}
\def\diagbox@triple@pict@NE{%
  \put(0,\y)  {\makebox(0,0)[tl]{\box\diagbox@boxa}}
  \put(\x,\y) {\makebox(0,0)[tr]{\box\diagbox@boxm}}
  \put(\x,0)  {\makebox(0,0)[br]{\box\diagbox@boxb}}
  \Line(0,0)(\xxm,\y)
  \Line(0,0)(\x,\yym)}
\def\diagbox@triple@pict@SW{%
  \put(0,\y) {\makebox(0,0)[tl]{\box\diagbox@boxa}}
  \put(0,0)  {\makebox(0,0)[bl]{\box\diagbox@boxm}}
  \put(\x,0) {\makebox(0,0)[br]{\box\diagbox@boxb}}
  \Line(0,\ym)(\x,\y)
  \Line(\xm,0)(\x,\y)}
\def\diagbox@triple@pict@SE{%
  \put(0,0)   {\makebox(0,0)[bl]{\box\diagbox@boxa}}
  \put(\x,0)  {\makebox(0,0)[br]{\box\diagbox@boxm}}
  \put(\x,\y) {\makebox(0,0)[tr]{\box\diagbox@boxb}}
  \Line(0,\y)(\xxm,0)
  \Line(0,\y)(\x,\ym)}
\def\diagbox@triple#1#2#3#4{%
  \begingroup
  \diagbox@wd=\z@
  \diagbox@ht=\z@
  \diagbox@sepl=\tabcolsep
  \diagbox@sepr=\tabcolsep
  \def\diagbox@part{triple}%
  \setkeys{diagbox}{dir=NW,#1}%
  \@nameuse{diagbox@triple@setbox@\diagbox@dir}{#2}{#3}{#4}%
  \edef\xa{\strip@pt\wd\diagbox@boxa}%
  \edef\ya{\strip@pt\dimexpr\ht\diagbox@boxa+\dp\diagbox@boxa\relax}%
  \edef\xb{\strip@pt\wd\diagbox@boxb}%
  \edef\yb{\strip@pt\dimexpr\ht\diagbox@boxb+\dp\diagbox@boxb\relax}%
  \edef\xm{\strip@pt\wd\diagbox@boxm}%
  \edef\ym{\strip@pt\dimexpr\ht\diagbox@boxm+\dp\diagbox@boxm\relax}%
  \FPneg\bi\yb
  \FPadd\ci\xb\xm  \FPneg\ci\ci
  \FPmul\di\xm\yb
  \FPadd\bj\ya\ym  \FPneg\bj\bj
  \FPneg\cj\xa
  \FPmul\dj\xa\ym
  \FPsub\u\dj\di
  \FPupn{v}{bj ci * bi cj * -}%
  \FPupn{delta}{bi dj * bj di * - cj ci - * 4 * %
    v u + copy * %
    - 2 swap root}%
  \ifdim\diagbox@wd=\z@
    \FPupn{x}{2 bj bi - delta v u - + / /}%
    \diagbox@wd=\x\p@
  \else
    \edef\x{\strip@pt\diagbox@wd}%
  \fi
  \ifdim\diagbox@ht=\z@
    \FPupn{y}{2 cj ci - delta v u + - / /}%
    \diagbox@ht=\y\p@
  \else
    \edef\y{\strip@pt\diagbox@ht}%
  \fi
  \FPsub\xxm\x\xm
  \FPsub\yym\y\ym
  $\vcenter{\hbox{\diagbox@pict}}$%
  \endgroup}
\newcommand\diagbox[3][]{%
  \@ifnextchar\bgroup
    {\diagbox@triple{#1}{#2}{#3}}{\diagbox@double{#1}{#2}{#3}}}
\expandafter\xdef\csname ver@slashbox.\@pkgextension\endcsname{9999/99/99}
\def\slashbox{%
  \def\diagbox@slashbox@options{dir=SW,}%
  \slashbox@}
\def\backslashbox{%
  \def\diagbox@slashbox@options{dir=NW,}%
  \slashbox@}
\newcommand\slashbox@[1][]{%
  \ifx\relax#1\relax\else
    \edef\diagbox@slashbox@options{%
      \unexpanded\expandafter{\diagbox@slashbox@options}%
      \unexpanded{width=#1,}}%
  \fi
  \slashbox@@}
\newcommand\slashbox@@[3][]{%
  \edef\diagbox@slashbox@options{%
    \unexpanded\expandafter{\diagbox@slashbox@options}%
    \unexpanded{trim=#1,}}%
  \expandafter\diagbox\expandafter[\diagbox@slashbox@options]{#2}{#3}}
\endinput
%%
%% End of file `diagbox.sty'.
"""