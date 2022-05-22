FRONT = r"""

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
	

\begin{tabular}{ |p{2.7cm}|p{3.5cm}|p{3.5cm}|p{3.5cm}|  }
	
	\hline
	
	\multicolumn{4}{|c|}{\textbf{\Large Washing Machine {\it \large{(BOSCH)}} Slots}} \\
	\hline
	
	\textbf{Date} & \textbf{7:00am-11:00am} & \textbf{2:00pm-6:00pm} & \textbf{9:00pm-1:00am} \\
	\hline

"""

## middle
#  & &  & \\
# \hline

BACK = r"""
\end{tabular}


\end{document}

"""