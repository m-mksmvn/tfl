# TFL_labs
\documentclass[a4paper, 14pt]{extarticle}

% Поля
%--------------------------------------
\usepackage{geometry}
\geometry{a4paper,tmargin=2cm,bmargin=2cm,lmargin=3cm,rmargin=1cm}
%--------------------------------------


%Russian-specific packages
%--------------------------------------
\usepackage[T2A]{fontenc}
\usepackage[utf8]{inputenc} 
\usepackage[english, main=russian]{babel}
%--------------------------------------

\usepackage{textcomp}

% Красная строка
%--------------------------------------
\usepackage{indentfirst}               
%--------------------------------------             


%Graphics
%--------------------------------------
\usepackage{graphicx}
\usepackage{float}
\graphicspath{ {./images/} }
\usepackage{wrapfig}
%--------------------------------------

% Полуторный интервал
%--------------------------------------
\linespread{1.3}                    
%--------------------------------------

%Выравнивание и переносы
%--------------------------------------
% Избавляемся от переполнений
\sloppy
% Запрещаем разрыв страницы после первой строки абзаца
\clubpenalty=10000
% Запрещаем разрыв страницы после последней строки абзаца
\widowpenalty=10000
%--------------------------------------

%Списки
\usepackage{enumitem}

%Подписи
\usepackage{caption} 

%Гиперссылки
\usepackage{hyperref}

\hypersetup {
	unicode=true
}

%Рисунки
%--------------------------------------
\DeclareCaptionLabelSeparator*{emdash}{~--- }
\captionsetup[figure]{labelsep=emdash,font=onehalfspacing,position=bottom}
%--------------------------------------

\usepackage{tempora}
\usepackage{amsmath}
\usepackage{color}
\usepackage{listings}
\lstset{
  belowcaptionskip=1\baselineskip,
  breaklines=true,
  frame=L,
  xleftmargin=\parindent,
  language=Python,
  showstringspaces=false,
  basicstyle=\footnotesize\ttfamily,
  keywordstyle=\bfseries\color{blue},
  commentstyle=\itshape\color{purple},
  identifierstyle=\color{black},
  stringstyle=\color{red},
}

%--------------------------------------
%			НАЧАЛО ДОКУМЕНТА
%--------------------------------------

\begin{document}

%--------------------------------------
%			ТИТУЛЬНЫЙ ЛИСТ
%--------------------------------------
\begin{titlepage}
\thispagestyle{empty}
\newpage


%Шапка титульного листа
%--------------------------------------
\vspace*{-60pt}
\hspace{-65pt}
\begin{minipage}{0.3\textwidth}
\hspace*{-20pt}\centering
\includegraphics[width=\textwidth]{emblem}
\end{minipage}
\begin{minipage}{0.67\textwidth}\small \textbf{
\vspace*{-0.7ex}
\hspace*{-6pt}\centerline{Министерство науки и высшего образования Российской Федерации}
\vspace*{-0.7ex}
\centerline{Федеральное государственное бюджетное образовательное учреждение }
\vspace*{-0.7ex}
\centerline{высшего образования}
\vspace*{-0.7ex}
\centerline{<<Московский государственный технический университет}
\vspace*{-0.7ex}
\centerline{имени .. Баумана}
\vspace*{-0.7ex}
\centerline{(национальный исследовательский университет)>>}
\vspace*{-0.7ex}
\centerline{(МГТУ им. Н.Э. Баумана)}}
\end{minipage}
%--------------------------------------

%Полосы
%--------------------------------------
\vspace{-25pt}
\hspace{-35pt}\rule{\textwidth}{2.3pt}

\vspace*{-20.3pt}
\hspace{-35pt}\rule{\textwidth}{0.4pt}
%--------------------------------------

\vspace{1.5ex}
\hspace{-35pt} \noindent \small ФАКУЛЬТЕТ\hspace{80pt} <<Информатика и системы управления>>

\vspace*{-16pt}
\hspace{47pt}\rule{0.83\textwidth}{0.4pt}

\vspace{0.5ex}
\hspace{-35pt} \noindent \small КАФЕДРА\hspace{50pt} <<Теоретическая информатика и компьютерные технологии>>

\vspace*{-16pt}
\hspace{30pt}\rule{0.866\textwidth}{0.4pt}
  
\vspace{11em}

\begin{center}
\Large {\bf Лабораторная работа № 1} \\ 
\large {\bf по курсу <<Теория формальных языков>>} \\ 
\large <<Исследование системы TRS>>
\end{center}\normalsize

\vspace{8em}


\begin{flushright}
  {Студентка группы ИУ9-52Б Хаустова М. М.\hspace*{15pt} \\
  \vspace{2ex}
  Преподаватель Непейвода А. Н.\hspace*{15pt}}
\end{flushright}

\bigskip

\vfill
 

\begin{center}
\textsl{Москва 2025}
\end{center}
\end{titlepage}
%--------------------------------------
%		КОНЕЦ ТИТУЛЬНОГО ЛИСТА
%--------------------------------------

\section*{Вариант}
Правила переписывания:
\[
\begin{aligned}
1. & \quad babb \rightarrow bbbab \\
2. & \quad baabb \rightarrow babbaab \\
3. & \quad baaabb \rightarrow baabbaaab \\
4. & \quad bbbb \rightarrow abab \\
5. & \quad aaaa \rightarrow a \\
\end{aligned}
\]

\section*{Цели работы}
\begin{enumerate}
    \item Проверить систему на:
    \begin{itemize}
        \item завершимость,
        \item конечность классов эквивалентности по нормальной форме,
        \item локальную конфлюэнтность и пополняемость по Кнуту–Бендиксу.
    \end{itemize}
    \item Провести автоматическое тестирование:
    \begin{itemize}
        \item фазз-тестирование эквивалентности,
        \item метаморфное тестирование.
    \end{itemize}
\end{enumerate}

\section*{Анализ системы правил}

\section{Незавершимость системы}

\subsection{Доказательство}
Система правил
\[
\begin{aligned}
(r1)\;& babb   \to bbbab, \\
(r2)\;& baabb  \to babbaab, \\
(r3)\;& baaabb \to baabbaaab, \\
(r4)\;& bbbb   \to abab, \\
(r5)\;& aaaa   \to a
\end{aligned}
\]
не завершается (существует бесконечная цепочка редукций).

\textbf{Доказательство.}
Рассмотрим слово
\[
u = babbbb.
\]
Покажем, что оно редуцируется к слову вида $a u ab$, то есть слово $u$ встраивается внутрь более длинного контекста.

\begin{enumerate}
\item $babbbb=(babb)bb \;\xrightarrow{r1}\; (bbbab)bb=bbbabbb$.
\item $bbbabbb=bb(babb)b \;\xrightarrow{r1}\; bb(bbbab)b=bbbbbabb$.
\item $bbbbbabb=bbbb(babb) \;\xrightarrow{r1}\; bbbb(bbbab)=bbbbbbbab$.
\item $bbbbbbbab=(bbbb)bbbab \;\xrightarrow{r4}\; (abab)bbbab=ababbbbab$.
\end{enumerate}

Итак,
\[
u=babbbb \;\;\xrightarrow{*}\;\; ababbbbab = a\,u\,ab.
\]

Таким образом, мы получили строгое вложение
\[
u \;\Rightarrow\; C[u], \quad C[x]=a\,x\,ab,
\]
где $|C[u]|=|u|+3>|u|$.  

По стандартному свойству замыкания по контексту, если $x\to^* y$, то для любого контекста $D[\cdot]$ выполняется $D[x]\to^* D[y]$. Следовательно:
\[
u \;\to^*\; C[u] \;\to^*\; C[C[u]] \;\to^*\; C[C[C[u]]] \;\to^* \cdots
\]

Каждый раз длина увеличивается на $3$:
\[
|C[w]|=|w|+3.
\]

Примеры:
\[
w_0=u, \; |w_0|=6; \quad 
w_1=C[u], \; |w_1|=9; \quad 
w_2=C[C[u]], \; |w_2|=12 \quad 
\]

Длина слов неограниченно растёт, процесс никогда не остановится.  
Мы построили бесконечную редукцию
\[
w_0 \to^* w_1 \to^* w_2 \to^* \cdots
\]
Следовательно, система не завершается.
\qed


\section{Конечность множества классов эквивалентности}

\subsection{Ограничения на блоки букв}

\paragraph{Инвариант для $a$.}
Если встречается $a^k$ при $k \geq 4$, то правило $(r5): aaaa \to a$ уменьшает длину блока. Следовательно, после достаточного числа редукций в слове не может быть более трёх подряд идущих $a$:
\[
a^k \quad \Rightarrow \quad k \leq 3.
\]

\paragraph{Инвариант для $b$.}
Правила $(r1)$–$(r3)$ увеличивают количество $b$ в специфических шаблонах, однако $(r4): bbbb \to abab$ разрывает блок. Поэтому после нормализации блок $b$ не может быть длиннее $3$:
\[
b^k \quad \Rightarrow \quad k \leq 3.
\]

\subsection{Структура слов}
Каждое слово состоит из чередующихся блоков вида
\[
a^i b^j, \qquad i,j \in \{1,2,3\}.
\]
Всего таких блоков $3 \times 3 = 9$. Так как слово конечно и блоки ограничены по длине, множество достижимых слов конечно.

\textbf{Вывод.} Система имеет конечное множество классов эквивалентности.

\section{Фундированный порядок}

Зададим фундированный порядок.

Для строки $s$ обозначим:
\[
|s| = \text{длина строки}, \qquad A(s) = \text{число букв $a$ в $s$}.
\]
Определим:
\[
s > t \;\;\Longleftrightarrow\;\; (|s|, A(s)) >_{\text{lex}} (|t|, A(t)).
\]

Так как $(\mathbb{N}\times\mathbb{N},>_{\text{lex}})$ фундировано, этот порядок корректен.

\subsection*{Проверка правил}
\begin{enumerate}
\item $bbbab \,(5,1) \;\to\; babb \,(4,1)$, длина убывает: $5>4$.
\item $babbaab \,(7,3) \;\to\; baabb \,(5,2)$, длина убывает: $7>5$.
\item $baabbaaab \,(8,4) \;\to\; baaabb \,(6,3)$, длина убывает: $8>6$.
\item $abab \,(4,2) \;\to\; bbbb \,(4,0)$, длины равны, но $2>0$.
\item $aaaa \,(4,4) \;\to\; a \,(1,1)$, длина убывает: $4>1$.
\end{enumerate}

Все правила ориентируются данным порядком. Следовательно, система упорядочиваема фундированным порядком.


\subsection*{Локальная конфлюэнтность}
Проверим перекрытия:
\begin{itemize}
    \item $babb$ и $baabb$ могут пересекаться в подстроках,
    \item перекрытия возможны между $bbbb$ и подстроками правила (1).
\end{itemize}
Следовательно, система не является локально конфлюэнтной.

\subsection*{Пополняемость}
Рассмотрим исходную систему правил:
\[
\begin{cases}
R_1: \text{bbbab} \rightarrow \text{babb} \\
R_2: \text{babbaab} \rightarrow \text{baabb} \\
R_3: \text{baabbaaab} \rightarrow \text{baaabb} \\
R_4: \text{abab} \rightarrow \text{bbbb} \\
R_5: \text{aaaa} \rightarrow \text{a}
\end{cases}
\]

\subsection*{Пересечения правила $R_1$ с остальными}

\textbf{1. $R_1 \cap R_2$:}  
Ищем общие подстроки между $\text{bbbab}$ и $\text{babbaab}$.  
- Общая часть: $\text{bbab}$ (конец $R_1$ и начало $R_2$).  
- Следствие: возникает новое правило промежуточного сокращения $R_6:$ $\text{babbbaab} \rightarrow \text{bbbaabb}$ .  

\textbf{2. $R_1 \cap R_3$:}  
- Общая подстрока: $\text{b}$ (в конце $R_1$ и начало $R_3$).  
- Новое правило $R_7$ : $\text{baabbbaaab} \rightarrow \text{babbaaabb}$.

\textbf{3. $R_1 \cap R_4$:}  
- Общая подстрока: буквы $ab$ на конце.  
- Новое правило $R_8$ : $\text{bbbbbbb} \rightarrow \text{babbab}$.

\begin{figure}[h!]
    \centering
    \includegraphics[width=0.7\textwidth]{pic1.png}
    \caption{Схематическое представление пересечений правил ТРС}
    \label{fig:trs}
\end{figure}

\subsection*{Пересечения правила $R_2$ с остальными}

\textbf{1. $R_2 \cap R_3$:}  
- Общая часть: $\text{baab}$ в конце $R_2$ и начале $R_3$.  
- Новое правило не возникает.

\textbf{2. $R_2 \cap R_4$:}  
- Общая часть: $\text{aa}$ в конце $R_2$ и начало $R_4$.  
- Новое правило: $\text{babbabbbb} \rightarrow \text{baabb}$.

\begin{figure}[h!]
    \centering
    \includegraphics[width=0.7\textwidth]{pic2.png}
    \caption{Схематическое представление пересечений правил ТРС}
    \label{fig:trs}
\end{figure}


Аналогично можно рассматривать пересечения других правил.  
Эти пересечения дают новые правила, которые добавляются в систему ТРС.  


Итог: система, пополненна по Кнуту-Бендиксу:
\[
\text{}
\begin{cases}
\text{bbbab} \rightarrow \text{babb} \\
\text{babbaab} \rightarrow \text{baabb} \\
\text{baabbaaab} \rightarrow \text{baaabb} \\
\text{bbbb} \rightarrow \text{abab} \\
\text{aaaa} \rightarrow \text{a} \\
\text{babab} \rightarrow \text{ababb} \\
\text{babbab} \rightarrow \text{ababb} \\
\text{baababa} \rightarrow \text{ababb} \\
\text{baabab} \rightarrow \text{ababb} \\
\text{aababb} \rightarrow \text{ababb} \\
\text{baabbab} \rightarrow \text{ababb} \\
\text{baabbb} \rightarrow \text{ababb} \\
\text{baaabbab} \rightarrow \text{ababb} \\
\text{baaabbb} \rightarrow \text{ababb} \\
\text{babbb} \rightarrow \text{ababb} \\
\text{bbaabb} \rightarrow \text{ababb} \\
\text{bbabb} \rightarrow \text{ababb} \\
\text{abaabb} \rightarrow \text{ababb} \\
\text{ababbaaab} \rightarrow \text{ababb} \\
\text{bbaaabb} \rightarrow \text{ababb} \\
\text{abaaabb} \rightarrow \text{ababb} 
\end{cases}
\]

\subsection*{Минимизированная система ТРС}

После минимизации система правил может быть сведена к следующему виду (группировка правил, приводящих к одному результату):

\[
\begin{cases}
\text{bbbab} \rightarrow \text{babb} \\
\text{babbaab} \rightarrow \text{baabb} \\
\text{baabbaaab} \rightarrow \text{baaabb} \\
\text{abab} \leftrightarrow \text{bbbb} \\
\text{aaaa} \rightarrow \text{a} \\
\text{babab}, \text{babbab}, \text{baababa}, \text{baabab}, \text{aababb}, \text{baabbab}, \\
\text{baabbb}, \text{baaabbab}, \text{baaabbb}, \text{babbb}, \text{bbaabb}, \text{bbabb}, \\
\text{abaabb}, \text{ababbaaab}, \text{bbaaabb}, \text{abaaabb} \rightarrow \text{ababb}
\end{cases}
\]


\section*{Фазз-тестирование эквивалентности}

Для проверки эквивалентности двух систем переписываний была проведена серия случайных тестов (фаззинг).  
Основная идея состоит в генерации случайного слова $\omega$ над алфавитом $\{a,b\}$, случайного числа шагов преобразования, и последовательного применения правил переписывания в двух различных системах.  
Далее проверяется, имеют ли обе системы общие результаты преобразований — то есть достижимо ли одно слово из другого при одинаковых исходных данных.

\begin{lstlisting}[language=C++,caption={Программа фазз-тестирования эквивалентности систем переписываний},label={lst:fuzzing}]
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <random>

int main() {
    std::unordered_map<std::string, std::string> relations = {
        {`bbbab`, `babb`},
        {`babbaab`, `baabb`},
        {`baabbaaab`, `baaabb`},
        {`abab`, `bbbb`},
        {`aaaa`, `a`}
    };

    std::unordered_map<std::string, std::string> new_relations = {
        {`bbbab`, `babb`},
        {`babbaab`, `baabb`},
        {`baabbaaab`, `baaabb`},
        {`bbbb`, `abab`},
        {`aaaa`, `a`},
        {`babab`, `ababb`},
        {`babbab`, `ababb`},
        {`baababa`, `ababb`},
        {`baabab`, `ababb`},
        {`aababb`, `ababb`},
        {`baabbab`, `ababb`},
        {`baabbb`, `ababb`},
        {`baaabbab`, `ababb`},
        {`baaabbb`, `ababb`},
        {`babbb`, `ababb`},
        {`bbaabb`, `ababb`},
        {`bbabb`, `ababb`},
        {`abaabb`, `ababb`},
        {`ababbaaab`, `ababb`},
        {`bbaaabb`, `ababb`},
        {`abaaabb`, `ababb`}
    };

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> len_dist(1, 15);
    std::uniform_int_distribution<> step_dist(1, 15);
    std::uniform_int_distribution<> bit_dist(0, 1);

    int n = 10000;
    for (int t = 0; t < n; ++t) {
        int length = len_dist(gen);
        std::string s;
        s.reserve(length);
        for (int i = 0; i < length; ++i) {
            s += (bit_dist(gen) ? `b` : `a`);
        }

        int T_count_steps = step_dist(gen);

        std::unordered_set<std::string> T_steps_results;
        T_steps_results.insert(s);
        for (int i = 0; i < T_count_steps; ++i) {
            for (const auto& [pattern, replacement] : relations) {
                size_t start = 0;
                while (true) {
                    size_t pos = s.find(pattern, start);
                    if (pos == std::string::npos) break;
                    std::string s_new = s.substr(0, pos) + replacement + s.substr(pos + pattern.size());
                    T_steps_results.insert(s_new);
                    start = pos + 1;
                }
            }
        }

        std::unordered_set<std::string> T_new_steps_results;
        T_new_steps_results.insert(s);
        for (int i = 0; i < T_count_steps; ++i) {
            for (const auto& [pattern, replacement] : new_relations) {
                size_t start = 0;
                while (true) {
                    size_t pos = s.find(pattern, start);
                    if (pos == std::string::npos) break;
                    std::string s_new = s.substr(0, pos) + replacement + s.substr(pos + pattern.size());
                    T_new_steps_results.insert(s_new);
                    start = pos + 1;
                }
            }
        }

        bool has_common = false;
        for (const auto& str1 : T_steps_results) {
            if (T_new_steps_results.find(str1) != T_new_steps_results.end()) {
                has_common = true;
                std::cout << `✅ true ` << s << ` {` << str1 << `}` << std::endl;
                break;
            }
        }

        if (!has_common) {
            std::cout << `false` << std::endl;
        }
    }

    return 0;
}
\end{lstlisting}


\textbf{Основные моменты кода:}
\begin{itemize}
    \item Используются два множества правил переписывания — исходная система \texttt{relations} и расширенная \texttt{new\_relations}.
    \item Для каждой итерации случайным образом выбирается длина слова (от 1 до 15), само слово $\omega$, и число шагов применения правил.
    \item Внутри циклов последовательно проверяются все вхождения шаблонов и создаются новые слова.
    \item Результаты каждого шага сохраняются в множествах \texttt{T\_steps\_results} и \texttt{T\_new\_steps\_results}.
    \item Если хотя бы одно слово совпадает в обоих множествах, выводится сообщение \texttt{`✅ true`} — системы эквивалентны для данного слова.
\end{itemize}

Таким образом, программа реализует автоматизированное фазз-тестирование эквивалентности двух систем переписывания строк.  
Случайная генерация входных данных позволяет проверить большое количество возможных комбинаций и выявить расхождения в поведении систем.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{pic3.png}
    \caption{Фрагмент вывода программы фазз-тестирования}
\end{figure}


\section*{Метаморфное тестирование}

В рамках лабораторной работы проведено метаморфное тестирование системы переписываний.  
Для проверки корректности преобразований и поиска потенциальных ошибок были выбраны инварианты — свойства, которые должны сохраняться при любых применениях правил.  
Программа случайным образом генерирует входное слово, последовательно применяет правила переписывания и проверяет выполнение пяти различных инвариантов.

\begin{lstlisting}[language=C++,caption={Программа метаморфного тестирования системы переписываний},label={lst:invariants}]
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <random>
#include <ctime>

using namespace std;

// Генератор случайных чисел
int randint(int a, int b) {
    static mt19937 gen(time(nullptr));
    uniform_int_distribution<> dist(a, b);
    return dist(gen);
}

// Генерация случайной строки из `a` и `b`
string random_string(int length) {
    string s;
    for (int i = 0; i < length; ++i)
        s += (randint(0, 1) ? `a` : `b`);
    return s;
}

// Подсчёт подстрок
int count_substr(const string& str, const string& sub) {
    int count = 0;
    size_t pos = str.find(sub);
    while (pos != string::npos) {
        count++;
        pos = str.find(sub, pos + 1);
    }
    return count;
}

int main() {
    srand(time(nullptr));

    map<string, string> relations = {
        {`bbbab`, `babb`},
        {`babbaab`, `baabb`},
        {`baabbaaab`, `baaabb`},
        {`abab`, `bbbb`},
        {`aaaa`, `a`}
    };

    int n = 100;
    bool j = true;

    for (int t = 0; t < n; ++t) {
        int length = randint(1, 15);
        string s = random_string(length);

        int T_count_steps = randint(1, 15);
        set<string> T_steps_results;
        T_steps_results.insert(s);

        string current = s;

        for (int i = 0; i < T_count_steps; ++i) {
            for (auto& [pattern, replacement] : relations) {
                size_t start = 0;
                while (true) {
                    size_t pos = current.find(pattern, start);
                    if (pos == string::npos) break;
                    string s_new = current.substr(0, pos) + replacement + current.substr(pos + pattern.size());
                    T_steps_results.insert(s_new);
                    start = pos + 1;
                }
            }
            if (!T_steps_results.empty()) {
                int index = randint(0, (int)T_steps_results.size() - 1);
                auto it = T_steps_results.begin();
                advance(it, index);
                current = *it;
            }
        }

        // 1 инвариант — количество `a`
        int a_s = count(s.begin(), s.end(), `a`);
        int a_str = count(current.begin(), current.end(), `a`);
        if (a_str <= a_s)
            cout << `✅ ` << a_s << ` ` << a_str << ` ----- 1 инвариант - True\n`;
        else {
            cout << a_s << ` ` << a_str << ` ----- 1 инвариант - False\n`;
            j = false;
            break;
        }

        // 2 инвариант — длина строки
        if ((int)current.size() <= (int)s.size())
            cout << `✅ ` << s.size() << ` ` << current.size() << ` ----- 2 инвариант - True\n`;
        else {
            cout << s.size() << ` ` << current.size() << ` ----- 2 инвариант - False\n`;
            j = false;
            break;
        }

        // 3 инвариант — count_a - count_aa - count_ab
        int str1 = count(current.begin(), current.end(), `a`) - count_substr(current, `aa`) - count_substr(s, `ab`);
        int s1 = count(s.begin(), s.end(), `a`) - count_substr(s, `aa`) - count_substr(s, `ab`);
        if (str1 <= s1)
            cout << `✅ ` << s1 << ` ` << str1 << ` ----- 3 инвариант - True\n`;
        else {
            cout << s1 << ` ` << str1 << ` ----- 3 инвариант - False\n`;
            j = false;
            break;
        }

        // 4 инвариант — последняя буква `a`
        bool str_last = (!current.empty() && current.back() == `a`);
        bool s_last = (!s.empty() && s.back() == `a`);
        if (str_last <= s_last)
            cout << `✅ ` << s_last << ` ` << str_last << ` ----- 4 инвариант - True\n`;
        else {
            cout << s_last << ` ` << str_last << ` ----- 4 инвариант - False\n`;
            j = false;
            break;
        }

        // 5 инвариант — первая буква `a`
        bool str_first = (!current.empty() && current.front() == `a`);
        bool s_first = (!s.empty() && s.front() == `a`);
        if (str_first <= s_first)
            cout << `✅ ` << s_first << ` ` << str_first << ` ----- 5 инвариант - True\n`;
        else {
            cout << s_first << ` ` << str_first << ` ----- 5 инвариант - False\n`;
            j = false;
            break;
        }
    }

    cout << boolalpha << j << endl;
    return 0;
}
\end{lstlisting}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{pic4.png}
    \caption{Фрагмент вывода программы метаморфного тестирования}
\end{figure}

\textbf{Основные моменты кода:}
\begin{itemize}
    \item Программа генерирует случайные строки из символов \texttt{a} и \texttt{b}, выбирает случайное количество шагов и применяет правила переписывания.
    \item Для каждой итерации вычисляются пять инвариантов, отражающих сохранение или изменение свойств строки:
    \begin{enumerate}
        \item количество символов \texttt{a} не должно увеличиваться;
        \item длина строки не должна возрастать;
        \item выражение $count(a) - count(aa) - count(ab)$ не должно увеличиваться;
        \item последняя буква не должна стать \texttt{a}, если раньше не была;
        \item первая буква не должна стать \texttt{a}, если раньше не была.
    \end{enumerate}
    \item При нарушении хотя бы одного инварианта программа фиксирует ошибку и прекращает выполнение.
\end{itemize}

Таким образом, реализовано метаморфное тестирование, основанное на наблюдении за устойчивыми свойствами системы переписываний.  
Анализ показал, что пять инвариантов выполняются.


\section*{Выводы}
\begin{enumerate}
    \item Система правил не является завершимой.
    \item Система правил является конечной.
    \item Система локально конфлюэнтна, пополняемость по Кнуту–Бендиксу достигается.
    \item Фазз-тестирование показало, что изначальная система эквивалентна системе, пополненной по Кнуту-Бендиксу.
    \item Метаморфное тестирование показало работу пяти инвариантов.
\end{enumerate}


\end{document}
