dependency=idl/XnpDate.rdb generate_xml.py npdate.py

idl/XnpDate.rdb : idl/XnpDate.idl
	. /usr/lib/libreoffice/sdk/setsdkenv_unix.sh && \
	idlc -I /usr/lib/libreoffice/sdk/idl $< && \
	regmerge $@ /UCR idl/XnpDate.urd 

manifest.txt: ${dependency} generate_xml.py
	python generate_xml.py

build : ${dependency} manifest.xml description.xml CalcAddIn.xcu 
	mkdir -p build/META-INF
	cp -r $^ build
	cat npdate.py ../datebs/datebs.py | tee build/npdate.py
	cp build/manifest.xml build/META-INF
	cd build; zip -r datenp.oxt *

.PHONY : clean
clean :
	rm -r idl/XnpDate.urd idl/XnpDate.rdb build/*	
