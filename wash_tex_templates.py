FRONT = r"""

\documentclass[11pt, a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[top=0.7 in,bottom=1in, left=0.4 in, right=1 in]{geometry}


\setlength{\arrayrulewidth}{0.5mm}
\setlength{\tabcolsep}{18pt}
\renewcommand{\arraystretch}{1.5}



\begin{document}
	
\thispagestyle{empty}
	

\begin{tabular}{ |p{2.7cm}|p{3.5cm}|p{3.5cm}|p{3.5cm}|  }
	
	\hline
	
	\multicolumn{4}{|c|}{\textbf{Washing Machine Slots}} \\
	\hline
	
	Date & 7:00am-11:00am & 2:00pm-6:00pm & 9:00pm-1:00am \\
	\hline

"""

## middle
#  & &  & \\
# \hline

BACK = r"""
\end{tabular}


\end{document}

"""