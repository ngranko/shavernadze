import statistics
import paramParser
import params.printColors as printColors
from csvExporter import CsvExporter
from exceptions import ParamError
from dataHoarder import DataHoarder
from params.districts import districtList

def usage():
    print('%susage: main.py --searchVal=<search value>%s' % (printColors.BOLD, printColors.ENDC))

def main():
    try:
        searchVal = paramParser.getParamValue('searchVal')
    except ParamError as err:
        usage()
        exit(2)

    with CsvExporter() as exporter:
        for district in districtList:
            data = DataHoarder(district.get('lat', 0), district.get('lng', 0)).loadData(searchVal)
            exporter.write(data)

main()
