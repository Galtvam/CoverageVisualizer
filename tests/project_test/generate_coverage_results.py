import coverage
import pytest
from xml.dom import minidom

cov = coverage.Coverage()
cov.start()

pytest.main(['-x', 'tests', '-vv'])

cov.stop()
cov.xml_report()

mydoc = minidom.parse('coverage.xml')
coverage = mydoc.getElementsByTagName('coverage')

print('total of statements: '+coverage[0].attributes['lines-valid'].value)
print('total of statements covered: '+coverage[0].attributes['lines-covered'].value)
print('total rate: '+coverage[0].attributes['line-rate'].value)





