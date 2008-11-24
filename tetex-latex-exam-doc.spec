Summary:	Documentation of exam documentclass
Summary(hu.UTF-8):	Az exam dokumentumosztály dokumentációja
Name:		tetex-latex-exam-doc
Version:	20080618
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
URL:		http://www-math.mit.edu/~psh/#ExamCls
# we don't need the examdoc.dvi because it's shipped with tetex-doc-latex
Source0:	http://www-math.mit.edu/~psh/exam/examdoc.tex
# Source0-md5:	e771547c36e897cc79a5da53676189f6
Source1:	http://www-math.mit.edu/~psh/exam/examdoc.pdf
# Source1-md5:	f4f60059de1a00a5d561fad9f46bb5e4
Requires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Documentation of exam documentclass.

%description -l hu.UTF-8
Az exam dokumentumosztály dokumentációja.

%prep
# empty

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/exam
install %{SOURCE0} %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/exam

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/texmf/doc/latex/exam/examdoc.*
