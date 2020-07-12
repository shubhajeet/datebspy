dependency=CalcAddIn.xcu idl/XnpDate.rdb description.xml npDate.py

idl/XnpDate.rdb : idl/XnpDate.idl
	. /usr/lib/libreoffice/sdk/setsdkenv_unix.sh && \
	idlc -I /usr/lib/libreoffice/sdk/idl $< && \
	regmerge $@ /UCR idl/XnpDate.urd 

manifest.txt: ${dependency} generate.py
	python generate_xml.py

build : ${dependency} manifest.txt
	mkdir -p build/META-INF
	cp ${dependency} build
	cp manifest.xml build/META-INF
	cd build; zip -r NepalDataScrapper.oxt *

.PHONY : clean
clean :
	rm -r idl/XnpDate.urd idl/XnpDate.rdb build/*	
