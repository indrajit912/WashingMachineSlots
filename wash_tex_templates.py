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