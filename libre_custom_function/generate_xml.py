# XML generation for DoobieDoo OOo Calc Add-in example.
# Created by jan@biochemfusion.com April 2009.

# A unique ID for the add-in.
addin_id = "np.com.maharjansujit.npdate"
addin_version = "0.3"
addin_displayname = "Convert date from AD to BS and vice versa"
addin_publisher_link = "https://maharjansujit.com.np/projects/datebpy"
addin_publisher_name = "Sujit Maharjan"

# description.xml
#
#

desc_xml = open('description.xml', 'w')

desc_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
desc_xml.write('<description xmlns="http://openoffice.org/extensions/description/2006" \n')
desc_xml.write('xmlns:d="http://openoffice.org/extensions/description/2006" \n')
desc_xml.write('xmlns:xlink="http://www.w3.org/1999/xlink"> \n' + '\n')
desc_xml.write('<dependencies> \n')
desc_xml.write('	<OpenOffice.org-minimal-version value="2.4" d:name="OpenOffice.org 2.4"/> \n')
desc_xml.write('</dependencies> \n')
desc_xml.write('\n')
desc_xml.write('<identifier value="' + addin_id + '" /> \n')
desc_xml.write('<version value="' + addin_version + '" />\n')   
desc_xml.write('<display-name><name lang="en">' + addin_displayname + '</name></display-name>\n')
desc_xml.write('<publisher><name xlink:href="' + addin_publisher_link + '" lang="en">' + addin_publisher_name + '</name></publisher>\n')
desc_xml.write('\n')
desc_xml.write('</description> \n')

desc_xml.close

def add_manifest_entry(xml_file, file_type, file_name):
	xml_file.write('<manifest:file-entry manifest:media-type="application/vnd.sun.star.' + file_type + '" \n')
	xml_file.write('	manifest:full-path="' + file_name + '"/> \n')

# manifest.xml
#
# List of files in package and their types.

manifest_xml = open('manifest.xml', 'w')

manifest_xml.write('<manifest:manifest>\n');
add_manifest_entry(manifest_xml, 'uno-typelibrary;type=RDB', 'XnpDate.rdb')
add_manifest_entry(manifest_xml, 'configuration-data', 'CalcAddIn.xcu')
add_manifest_entry(manifest_xml, 'uno-component;type=Python', 'npdate.py')
#add_manifest_entry(manifest_xml, 'uno-component;type=Python', 'datebs.py')
manifest_xml.write('</manifest:manifest> \n')

manifest_xml.close

# CalcAddIn.xcu
#
#

# instance_id references the named UNO component instantiated by Python code (that is my understanding at least).
instance_id = "np.com.maharjansujit.npDate.python.npDateImpl"
# Name of the corresponding Excel add-in if you want to share documents across OOo and Excel.
excel_addin_name = "npDate.xlam"

def define_function(xml_file, function_name, description, parameters):
	xml_file.write('  <node oor:name="' + function_name + '" oor:op="replace">\n')
	xml_file.write('    <prop oor:name="DisplayName"><value xml:lang="en">' + function_name + '</value></prop>\n')
	xml_file.write('    <prop oor:name="Description"><value xml:lang="en">' + description + '</value></prop>\n')
	xml_file.write('    <prop oor:name="Category"><value>Add-In</value></prop>\n')
	#xml_file.write('    <prop oor:name="CompatibilityName"><value xml:lang="en">AutoAddIn.DoobieDo.' + function_name + '</value></prop>\n')
	xml_file.write('    <node oor:name="Parameters">\n')

	for p, desc in parameters:
		# Optional parameters will have a displayname enclosed in square brackets.
		p_name = p.strip("[]")		
		xml_file.write('      <node oor:name="' + p_name + '" oor:op="replace">\n')
		xml_file.write('        <prop oor:name="DisplayName"><value xml:lang="en">' + p_name + '</value></prop>\n')
		xml_file.write('        <prop oor:name="Description"><value xml:lang="en">' + desc + '</value></prop>\n')
		xml_file.write('      </node>\n')

	xml_file.write('    </node>\n')
	xml_file.write('  </node>\n')

#
calcaddin_xml = open('CalcAddIn.xcu', 'w')

calcaddin_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
calcaddin_xml.write('<oor:component-data xmlns:oor="http://openoffice.org/2001/registry" xmlns:xs="http://www.w3.org/2001/XMLSchema" oor:name="CalcAddIns" oor:package="org.openoffice.Office">\n')
calcaddin_xml.write('<node oor:name="AddInInfo">\n')
calcaddin_xml.write('<node oor:name="' + instance_id + '" oor:op="replace">\n')
calcaddin_xml.write('<node oor:name="AddInFunctions">\n')

define_function(calcaddin_xml, \
	'dateToAD', 'converts date in BS to AD', \
	[('[date]', 'Date in BS')])
define_function(calcaddin_xml, \
	'dateToBS', 'converts date in BS to AD', \
	[('[date]', 'Date in AD')])
#define_function(calcaddin_xml, \
#	'echo', 'echo test', \
#	[('text', 'string')])
#define_function(calcaddin_xml, \
#	'greet', 'greets', \
#	[])
define_function(calcaddin_xml, \
                'BSMonth','extracts month from the BS date string',
                [('date','Date in BS')])
define_function(calcaddin_xml, \
                'BSMonthString','extracts month from the BS date string',
                [('date','Date in BS')])
define_function(calcaddin_xml, \
                'BSMonthNepali','extracts month from the BS date string',
                [('date','Date in BS')])
define_function(calcaddin_xml, \
                'BSFinancialYear','extracts financial year from the BS date string',
                [('date','Date in BS')])
define_function(calcaddin_xml, \
                "BSadd","add specific day, month, year to BS date",
                [('date',"date in BS"),("day","no of days"),("month","no of month"),("year","no of year")])

calcaddin_xml.write('</node>\n')
calcaddin_xml.write('</node>\n')
calcaddin_xml.write('</node>\n')
calcaddin_xml.write('</oor:component-data>\n')

calcaddin_xml.close

# Done
